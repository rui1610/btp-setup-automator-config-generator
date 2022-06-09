from libs.python.helperGeneric import getEnvVariableValue
from libs.python.helperLog import initLogger
from libs.python.helperJinja2 import renderTemplateWithJson
from libs.python.helperJson import getJsonFromFile
import logging


log = logging.getLogger(__name__)

CATEGORIES = {}
CATEGORIES["SERVICE"] = ["SERVICE", "ELASTIC_SERVICE", "PLATFORM", "CF_CUP_SERVICE"]
CATEGORIES["APPLICATION"] = ["APPLICATION"]
CATEGORIES["ENVIRONMENT"] = ["ENVIRONMENT"]

FOLDER_OUTPUT_USECASES = "./output/usecases/"
FOLDER_OUTPUT_WORKFLOWS = "./.github/workflows/"
FOLDER_OUTPUT_DOCS = "./docs/"
FOLDER_TEMPLATES = "./templates/"


class BTPUSECASE_GEN:
    def __init__(self):
        self.myemail = getEnvVariableValue("BTPSA_PARAM_MYEMAIL")
        self.mypassword = getEnvVariableValue("BTPSA_PARAM_MYPASSWORD")
        self.globalaccount = getEnvVariableValue("BTPSA_PARAM_GLOBALACCOUNT")
        self.templatefoler = "./"
        self.btpcliapihostregion = "eu10"
        self.loginmethod = "basicAuthentication"
        self.logcommands = False
        self.region = "us10"
        self.envvariables = None
        self.logfile = "./log/generator.log"
        self.metadatafile = "./log/generator_metadata.json"

        initLogger(self)

    def fetchEntitledServiceList(self, mainDataJsonFile):

        result = fetchDataFromConfigFile(self, mainDataJsonFile)
        self.entitledServices = result

    # def applyServiceListOnTemplate(self, templateFile, targetFilename):

    #     serviceList = self.entitledServices
    #     renderTemplateWithJson(templateFile, targetFilename, serviceList)
    #     log.success("applied SAP BTP service list on template file >" + templateFile + "< and created the target file >" + targetFilename + "<")

    def createBtpServiceTests(self, region):
        btpservicelist = self.entitledServices.get("btpservicelist")

        serviceCategoryFilter = ["SERVICE", "APPLICATION", "ENVIRONMENT"]

        listUsecaseFiles = []
        for category in btpservicelist:
            if category.get("name") in serviceCategoryFilter:
                print("CHECKING " + category.get("name"))
                for service in category.get("list"):
                    serviceList = []
                    print(" - now service " + service.get("name"))
                    for plan in service.get("servicePlans"):
                        item = {}
                        item["category"] = category.get("name")
                        item["service"] = service.get("name")
                        item["plan"] = plan.get("name")
                        item["jsonschemarefs"] = plan.get("jsonschemarefs")
                        supportedInRegion = False
                        for datacenter in plan.get("dataCenters"):
                            thisRegion = datacenter.get("region")
                            if thisRegion == region:
                                supportedInRegion = True
                        if supportedInRegion:
                            serviceList.append(item)

                    if serviceList and len(serviceList) > 0:
                        filePatternName = region + "/" + category.get("name") + "-" + service.get("name")

                        usecasefile = FOLDER_OUTPUT_USECASES + filePatternName + "-usecase.json"
                        templateFilename = FOLDER_TEMPLATES + "usecases/USECASE.JSON"
                        renderTemplateWithJson(templateFilename, usecasefile, {"serviceList": serviceList})

                        parametersfile = FOLDER_OUTPUT_USECASES + filePatternName + "-parameters.json"
                        templateFilename = FOLDER_TEMPLATES + "usecases/PARAMETERS.JSON"
                        subaccountname = "BTPSA int test " + category.get("name")
                        usecasefile = "https://raw.githubusercontent.com/rui1610/btp-setup-automator-config-generator/main/output/usecases/" + filePatternName + "-usecase.json"
                        thisItem = {"usecasefile": usecasefile, "subaccountname": subaccountname, "region": region}
                        renderTemplateWithJson(templateFilename, parametersfile, thisItem)

                        urlParameterFile = "https://raw.githubusercontent.com/rui1610/btp-setup-automator-config-generator/main/output/usecases/" + filePatternName + "-parameters.json"
                        parametersParameterFile = {}
                        parametersParameterFile["usecasefile"] = usecasefile
                        parametersParameterFile["region"] = region
                        parametersParameterFile["category"] = category.get("name")
                        parametersParameterFile["service"] = service.get("name")
                        parametersParameterFile["parameterfile"] = urlParameterFile
                        listUsecaseFiles.append(parametersParameterFile)

        templateFilename = FOLDER_TEMPLATES + "workflows/BTP-SERVICES-TEST.yml"
        targetFilename = FOLDER_OUTPUT_WORKFLOWS + "btp-test-" + region + ".yml"
        renderTemplateWithJson(templateFilename, targetFilename, {"region": region, "usecasetestlist": listUsecaseFiles})

    def createPageServiceDetails(self):
        btpservicelist = self.entitledServices.get("btpservicelist")

        # Create a detailed page for each service
        for category in btpservicelist:
            for service in category.get("list"):
                targetFilename = FOLDER_OUTPUT_DOCS + "services/" + service.get("name") + ".md"
                templateFilename = FOLDER_TEMPLATES + "docs/SERVICE-DETAILS.MD"
                renderTemplateWithJson(templateFilename, targetFilename, {"service": service, "category": category})

        # Create the root file with links to the detailed pages
        targetFilename = FOLDER_OUTPUT_DOCS + "free-tier.md"
        templateFilename = FOLDER_TEMPLATES + "docs/SERVICE-FREE-TIER.MD"
        renderTemplateWithJson(templateFilename, targetFilename, {"btpservicelist": btpservicelist})

        # Create the root file with links to the detailed pages
        targetFilename = FOLDER_OUTPUT_DOCS + "service-overview.md"
        templateFilename = FOLDER_TEMPLATES + "docs/SERVICE-OVERVIEW.MD"
        renderTemplateWithJson(templateFilename, targetFilename, {"btpservicelist": btpservicelist})

        # Create the root file with links to the detailed pages
        targetFilename = FOLDER_OUTPUT_DOCS + "index.md"
        templateFilename = FOLDER_TEMPLATES + "docs/INDEX.MD"
        renderTemplateWithJson(templateFilename, targetFilename, {"btpservicelist": btpservicelist})


def fetchDataFromConfigFile(btpusecase_gen, mainDataJsonFile):

    result = getJsonFromFile(None, mainDataJsonFile)
    btpservicelist = result["btpservicelist"]
    btpenums = result["btpenums"]

    thisResult = {"btpservicelist": btpservicelist, "btpenums": btpenums}
    return thisResult
