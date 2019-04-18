#include "pch.h"
#include "pugixml.hpp"
#include <iostream>
#include <string>
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