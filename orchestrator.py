import re
import sys
import json
from chatParser import WhatsAppChatParser
from slideGenerator import SlideGenerator 

def main():
    chatparser = WhatsAppChatParser(sys.argv[1])
    generator = SlideGenerator('output.pptx')
    
    while True:
        try:
           generator.addSlide(chatparser.getNextQuote())
        except:
           break
    generator.save()  
    

main()
