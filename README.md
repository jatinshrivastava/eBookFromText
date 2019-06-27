# eBookFromText
##Problem
Our software predominantly deals with automatic creation of presentation slide when an input text which is extracted from messaging platform like WhatsApp is provided to the software. Therefore it is very useful in senarios where ppt is required to be generated from the message list. It is designed in such a way that our software first recognises timestamp within the txt input provided and then extract any quote or message precedding that time stamp. Also pattern recognises multiline messages and print those messsages as well. certian specific messsages like some website links and "This message was deleted" will be avoided into the final presentaion as these message pattern will be neglected by the software.

#Prerequisites
This sodftware is not very demanding and requires only the installation of python into the pc and also user needs to be fimilar with the commands that are required for operation within this software. Also the input file should be in the same directory as that of software.

Below is the command required for pptx generation:
  python orchestrataor.py <inputfile_name> <Outputfile_name.pptx>
