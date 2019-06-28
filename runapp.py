import sys
import json
import os.path
from os import path
from texttoppt.orchestrator import TextToPPTOrchestrator 

try:
    if(path.exists('config.json')):
        with open('config.json') as config_file:
            data = json.load(config_file)
        author = data['messagesFrom']
        shapeType = data['shapeType']
        fontSize = int(data['fontSize'])
        left = float(data['left'])
        top = float(data['top'])
        width = float(data['width'])
        height = float(data['height'])
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
