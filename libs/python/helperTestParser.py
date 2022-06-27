import logging
import glob
import re

log = logging.getLogger(__name__)

TEST_INPUTFOLDER = "./test/input"
TEST_OUTPUTFOLDER = "./test/output"


class BTPUSECASE_TESTRESULT:
    def __init__(self, content):
        self.testResult = None
        self.testMessage = None
        self.serviceName = None
        self.servicePlan = None
        self.parameterFile = None
        self.usecaseFile = None
        self.errorMessages = None

        if "[error]" in content:
            message = content.split("[error]")
            self.testResult = "FAILED"
            self.testMessage = message[1]
        else:
            self.testResult = "SUCCESS"

        for line in content.split("\n"):
            searchString = "ERROR "
            if searchString in line:
                message = line.split(searchString)
                if len(message) > 0:
                    errorMessageRaw = message[1]
                    if self.errorMessages is None:
                        self.errorMessages = errorMessageRaw.strip()
                    else:
                        self.errorMessages = self.errorMessages + "\n" + errorMessageRaw.strip()

            searchString = "INFO "
            if searchString in line:
                message = line.split(searchString)
                if len(message) > 0:
                    thisMessage = message[1].split(" : ")
                    if len(thisMessage) > 0 and "usecasefile" in thisMessage[1]:
                        thisString = escape_ansi(thisMessage[2])
                        self.usecaseFile = thisString
                    if len(thisMessage) > 0 and "parameterfile" in thisMessage[1]:
                        thisString = escape_ansi(thisMessage[2])
                        self.usecaseFile = thisString

            searchString = "Assign entitlement for"
            if searchString in line:
                message = line.split(searchString)
                if len(message) > 0:
                    serviceSplitter = message[1].split(" and plan ")
                    matches = re.search('>(.*?)<', serviceSplitter[0])
                    if self.serviceName is None:
                        self.serviceName = matches.group(1)
                    matches = re.search('>(.*?)<', serviceSplitter[1])
                    if self.servicePlan is None:
                        self.servicePlan = matches.group(1)

    def __iter__(self):
        pass


def getTestInputs():
    result = []
    for filename in glob.iglob(TEST_INPUTFOLDER + '**/*.txt', recursive=True):
        with open(filename, 'r') as f:
            content = f.read()
            blocks = content.split("[group]")
            for block in blocks:
                if "Run ./btpsa " in block:
                    thisResult = BTPUSECASE_TESTRESULT(block)
                    result.append(thisResult)
    return result


def escape_ansi(line):
    ansi_escape = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', str(line))
