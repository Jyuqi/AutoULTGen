## Users can choose to generate config xml in different 2 ways.

- cmdconfiggen.py :  From xml generated from mhw.h file(in htoxml folder) , filter useless infomation and create target xml. 

- webgenxml.py extracts user config xml from bspec webpage

After one of above options, use cmdclassgen.py to expand each cmd field in c++. (readxml c++ part is defined in readxml folder)
