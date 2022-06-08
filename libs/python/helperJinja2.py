from pathlib import Path
import jinja2
import logging
import os

log = logging.getLogger(__name__)


def renderTemplateWithJson(templateFilename, targetFilename, parameters):

    templateFolder = os.path.dirname(templateFilename)
    templateBasename = os.path.basename(templateFilename)

    templateLoader = jinja2.FileSystemLoader(searchpath=templateFolder)
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template(templateBasename)

    renderedText = template.render(parameters)  # this is where to put args to the template renderer

    # create folder for target file, if folder not existing
    pathTargetFilename = os.path.dirname(targetFilename)
    Path(pathTargetFilename).mkdir(parents=True, exist_ok=True)

    with open(targetFilename, 'w') as f:
        f.write(renderedText)
