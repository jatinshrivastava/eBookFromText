import re
import sys
import json
from chatParser import WhatsAppChatParser
from slideGenerator import SlideGenerator 

def main():
    if ( len(sys.argv) < 3 ):
        print("Please specify the exportfile and desired output filename\n Usage: " + sys.argv[0] + " <chatexportFile> <pptfilename> " )
        return
    chatparser = WhatsAppChatParser(sys.argv[1])
    generator = SlideGenerator(sys.argv[2])
    
    while True:
        try:
           generator.addSlide(chatparser.getNextQuote())
        except:
           break
    generator.save()  
    

main()
