import re
import sys
from chatParser import WhatsAppChatParser

def testThatWeCanExtractMultiLineMessage():
    test_name = "testThatWeCanExtractMultiLineMessage"
    input_file = "testcase1.txt"
    #print(input_text)
    expected_output_text = "Ignorance is bliss\n\n"
    expected_output_text += "Its so painful to be aware of negative effects of my own actions\n\n"
    expected_output_text += "Still falling victim of this uncontrolled mind\n"
    #print(expected_output_text)

    chatparser = WhatsAppChatParser(input_file)
    actual_output = chatparser.getNextQuote()
    #print(actual_output)

    if ( actual_output == expected_output_text ):
        print(test_name + ": SUCCESS")
    else:
        print(test_name + ": FAIL" + "\n\n\tEXPECTED: " + expected_output_text + "\n\n\tACTUAL: " + actual_output)



def testThatDeletedMessagesAreIgnored():
    input_file = "deletedLinesTestData.txt"
    expected_output_text = "Quote 2\n"
    test_name = "testThatDeletedMessagesAreIgnored"

    chatparser = WhatsAppChatParser(input_file)
    first_quote = chatparser.getNextQuote()
    second_quote = chatparser.getNextQuote()

    actual_output = second_quote
    if ( actual_output == expected_output_text ):
        print(test_name + ": SUCCESS")
    else:
        print(test_name + ": FAIL" + "\n\n\tEXPECTED: " + expected_output_text + "\n\n\tACTUAL: " + actual_output)


def runTestSuite():
    testThatWeCanExtractMultiLineMessage()
    testThatDeletedMessagesAreIgnored()

runTestSuite()
