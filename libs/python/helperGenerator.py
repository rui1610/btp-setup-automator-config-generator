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
        self.btpcliapihostregion = "eu10"
        self.region = "us10"
        self.logfile = "./log/generator.log"

    def fetchEntitledServiceList(self, mainDataJsonFile):
        self.entitledServices = getJsonFromFile(None, mainDataJsonFile)
        btpservicelist = self.entitledServices.get("btpservicelist")
        for category in btpservicelist:
            for service in category.get("list"):
                addJsonSchemaRefIntoServicePlan(service, self.entitledServices)

    def createBtpServiceTests(self, region):
        btpservicelist = self.entitledServices.get("btpservicelist")

        serviceCategoryFilter = ["SERVICE", "APPLICATION", "ENVIRONMENT"]

        for category in btpservicelist:
            listUsecaseFiles = []
            if category.get("name") in serviceCategoryFilter:
                print("CHECKING " + category.get("name"))
                for service in category.get("list"):
                    print(" - now service " + service.get("name"))
                    for plan in service.get("servicePlans"):
                        serviceList = []
                        item = {}
                        item["category"] = category.get("name")
                        item["service"] = service.get("name")
                        item["plan"] = plan.get("name")
                        item["jsonschemaproperties"] = plan.get("jsonschemaproperties")
                        supportedInRegion = False
                        for datacenter in plan.get("dataCenters"):
                            thisRegion = datacenter.get("region")
                            if thisRegion == region:
                                supportedInRegion = True
                        if supportedInRegion:
                            serviceList.append(item)

                        if serviceList and len(serviceList) > 0:
                            filePatternName = region + "/" + category.get("name") + "-" + service.get("name") + "-" + plan.get("name")

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
                            parametersParameterFile["plan"] = plan.get("name")
                            parametersParameterFile["parameterfile"] = urlParameterFile
                            listUsecaseFiles.append(parametersParameterFile)

            templateFilename = FOLDER_TEMPLATES + "workflows/BTP-SERVICES-TEST.yml"

            targetFilename = FOLDER_OUTPUT_WORKFLOWS + "test-" + category.get("name").lower() + "s-" + region + ".yml"
            renderTemplateWithJson(templateFilename, targetFilename, {"region": region, "category": category.get("name").lower(), "usecasetestlist": listUsecaseFiles})

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


def addJsonSchemaRefIntoServicePlan(service, mainJsonData):

    if service:
        for plan in service.get("servicePlans"):
            if plan.get("jsonschemarefs"):
                for paremeter in plan.get("jsonschemarefs"):
                    parameterDefName = paremeter.get("name")
                    jsonSchemaDefs = mainJsonData.get("jsonSchemaDefs")
                    for thisName in jsonSchemaDefs:
                        if thisName == parameterDefName:
                            plan["jsonschemaproperties"] = jsonSchemaDefs.get(thisName)
