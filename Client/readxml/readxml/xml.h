// xml is used to deal with unified cmd config xml file
#include "pch.h"
#include "pugixml.hpp"
#include <iostream>
#include <string>
#include <vector>
#include <list>
class xml
{
public:
    pugi::xml_document doc;
    int fieldvalue;
    int readconfig(const char* testname);
    void printallfield(const char* testname, const char* cmdname, const char* fieldname);
    int getfield(const char* testname, const char* cmdname, const char* fieldname, const char* subfieldname);
    bool validate(int input, int saved, bool m_fieldToValidate);
};