import json
import os
import sys
import requests
import logging

log = logging.getLogger(__name__)


def getJsonFromFile(self, filename):
    data = None
    foundError = False
    f = None

    if "http://" in filename or "https://" in filename:
        data = None
        try:
            thisRequest = requests.get(filename)
            data = json.loads(thisRequest.text)
        except Exception as e:
            log.error("please check the json file >" + filename + "<: " + str(e))
            sys.exit(os.EX_DATAERR)
        return data

    try:
        # Opening JSON file
        f = open(filename)
        # returns JSON object as a dictionary
        data = json.load(f)
    except IOError:
        message = "Can't open json file >" + filename + "<"
        if log is not None:
            log.error(message)
        else:
            print(message)
        foundError = True
    except ValueError as err:
        message = "There is an issue in the json file >" + filename + \
            "<. Issue starts on character position " + \
            str(err.pos) + ": " + err.msg
        if log is not None:
            log.error(message)
        else:
            print(message)
        foundError = True
    finally:
        if f is not None:
            f.close()

    if foundError is True:
        message = "Can't run the use case before the error(s) mentioned above are not fixed"
        if log is not None:
            log.error(message)
        else:
            print(message)
        sys.exit(os.EX_DATAERR)
    return data


def saveJsonToFile(filename, jsonData):
    with open(filename, 'w') as outfile:
        json.dump(jsonData, outfile, indent=2)
    return True
