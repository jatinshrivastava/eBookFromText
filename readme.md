# eBookFromText
## Problem
Our software predominantly deals with automatic creation of presentation slide when an input text which is extracted from a messaging platform like WhatsApp is provided to the software. Therefore it is very useful in scenarios where ppt is required to be generated from the message list. It is designed in such a way that our application first recognizes the timestamp within the text file provided. Then the application extracts any quote or message following that time stamp. Also, pattern recognizes multiline messages and print those messages as well. Certain specific messages like some website links and "This message was deleted" will be avoided into the final presentation as these message pattern will be neglected by the software.

## Prerequisites
This software is not very demanding and requires only the installation of python into the pc and also user needs to be familiar with the commands that are required for operation within this software. Also, the input file should be in the same directory as that of software.

Below is the command required for pptx generation:

       python runapp.py <inputfile_name.txt> <Outputfile_name.pptx>
  
## Features
Features of this application involved fully customization of shapes used within slides, font shapes,  colors, and the person whose quote needed to be extracted.

## Configuration
A json file is provided to make this software more adaptive and useful. This involves shape changes, extraction of certain person quote or the entire quote all these modifications can be made through json file.

## Who needs this software
This software is required when the chat is very long and required to be presented in a visually prominent manner.

## Working
Working of this software mainly required an input file with txt extension which should be placed in the same directory as software
User needs to be familiar with the commands required for the operation.
