import sys
import json
import os.path
from os import path
from pptx.util import Inches, Pt
from pptx.enum.shapes import MSO_SHAPE
from texttoppt.orchestrator import TextToPPTOrchestrator 

try:
    if(path.exists('config.json')):
        with open('config.json') as config_file:
            data = json.load(config_file)
        author = data['messagesFrom']
        shapeType = data['shapeType']
        fontSize = int(data['fontSize'])
        left = Inches(float(data['left']))
        top = Inches(float(data['top']))
        width = Inches(float(data['width']))
        height = Inches(float(data['height']))
        shapemap = {}
        shapemap['rectangle'] = MSO_SHAPE.RECTANGLE
        shapemap['round rectangle'] = MSO_SHAPE.ROUNDED_RECTANGLE
        shapemap['curved ribbon'] = MSO_SHAPE.CURVED_UP_RIBBON
        orc = TextToPPTOrchestrator()
        orc.SetMessageAuthor(author)
        orc.SetShapeType(shapeType)
        orc.SetFontSize(fontSize)
        orc.SetShapeLeft(left)
        orc.SetShapeTop(top)
        orc.SetShapeWidth(width)
        orc.SetShapeHeight(height)
        orc.ConvertTextFileToPPT(sys.argv[1], sys.argv[2])
        
    else:
        orc = TextToPPTOrchestrator()
        orc.ConvertTextFileToPPT(sys.argv[1], sys.argv[2])
except:
        print("Please specify the exportfile and desired output filename\n Usage: " + sys.argv[0] + " <chatexportFile> <pptfilename> " )
