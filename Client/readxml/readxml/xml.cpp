// readxml.cpp : This file contains the 'main' function. Program execution begins and ends there.
// xml is used to deal with unified cmd config xml file

#include "xml.h"

int xml::readconfig(const char* filename)
{
    //load config xml file
    if (!doc.load_file(filename)) return -1;
}

void xml::printallfield(const char* testname, const char* cmdname, const char* fieldname )
{
    //print all attributes of one cmd
    pugi::xml_node testnode = doc.child(testname);
    for (pugi::xml_node classnode : testnode.children())
    {
        pugi::xml_node fieldnode = classnode.child(cmdname).child(fieldname);
            for (pugi::xml_attribute attr : fieldnode.attributes())
            {
                std::cout << " " << attr.name() << "=" << attr.value();
            }
            std::cout << std::endl;
    }
}



int xml::getfield(const char* testname, const char* cmdname, const char* fieldname, const char* subfieldname)
{   
    // parse xml files, to get dwo.field0
    pugi::xml_node testnode = doc.child(testname);
    for (pugi::xml_node classnode : testnode.children())
    {   
        pugi::xml_node fieldnode = classnode.child(cmdname).child(fieldname);
        //std::cout<<fieldnode.attribute(subfieldname).value();
        fieldvalue = fieldnode.attribute(subfieldname).as_int();
    }
    return fieldvalue;

}


bool xml::validate(int input, int saved, bool m_fieldToValidate=true) 
{
    //validate input value with data saved in xml
    if(m_fieldToValidate)
    {
        if (input == saved)
        {
            std::cout << "Equal!" << std::endl;
            return true;
        }
        std::cout << "Not equal!" << std::endl;
        return false;
    }
    
    std::cout<<"No need to validate!"<<std::endl;
    return true;
    
}


int main()
{
    xml xml1;
    xml1.readconfig("config_mhw_vdbox_vdenc_hwcmd_g12_tglhp.h.xml");
    //xml1.printallfield("TestName", "VDENC_PIPE_MODE_SELECT_CMD", "DW0");
    int fieldvalue = xml1.getfield("TestName", "VDENC_PIPE_MODE_SELECT_CMD", "DW0", "CommandType");
    std::cout << fieldvalue << std::endl;
    //validate
    int input;
    std::cin >> input;
    xml1.validate(input, xml1.fieldvalue, false);

}

