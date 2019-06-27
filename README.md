# eBookFromText
## Problem
Our software predominantly deals with automatic creation of presentation slide when an input text which is extracted from messaging platform like WhatsApp is provided to the software. Therefore it is very useful in senarios where ppt is required to be generated from the message list. It is designed in such a way that our software first recognises timestamp within the txt input provided and then extract any quote or message precedding that time stamp. Also pattern recognises multiline messages and print those messsages as well. certian specific messsages like some website links and "This message was deleted" will be avoided into the final presentaion as these message pattern will be neglected by the software.

## Prerequisites
This sodftware is not very demanding and requires only the installation of python into the pc and also user needs to be fimilar with the commands that are required for operation within this software. Also the input file should be in the same directory as that of software.

Below is the command required for pptx generation:


  python orchestrataor.py <inputfile_name> <Outputfile_name.pptx>
  
## Features
Features of this application invoved fully customization of shapes used within slides,font shapes and colors,person whose quote needed to be extracted.

## Configuration
A jason file is provided to make this software more adaptive and useful. These involves shape changes , extraction of certain person quote or the entire quote all these modifications can me made through jason file.

## Who needs this software
This softwared is required when the chat is very long and required to be presented in visually prominent manner.

## Working
working of this software mainly required an input file with txt exension which should be placed in the same directory as software
User needs to be familiar with commands required for the operation.
