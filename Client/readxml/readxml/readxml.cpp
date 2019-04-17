// readxml.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#define CMDFIELD(Field0)  pcmdReference->##Field0

//VdencPipeModeSelectCmd obj;
//Xxxclass::Test()
//{
//    Gtest::get test name
//        Obj->Initialize(testname);
//}
//
//Class XML
//{
//
//Read()
//}
//
//Read(testname, cmdname, fieldname, subfieldname)
//{
//    // Parse xml files, to get DWO.FIELD0
//}
//class VdencPipeModeSelectCmd : public GpuCmdItem<mhw_vdbox_vdenc_g12_tglhp::VDENC_PIPE_MODE_SELECT_CMD>
//{
//public:
//    VdencPipeModeSelectCmd() : GpuCmdItem() {};
//    ~VdencPipeModeSelectCmd() {};
//    bool validate();
//public:
//    Initialize()
//        CmdType m_reference;
//    CmdType m_fieldToValidate;
//
//};
//bool VdencPipeModeSelectCmd::validate()
//{
//    if (m_fieldToValidate.DW0.Pipeline != pCmd->DW0.Pipeline && m_fieldToValidate.DW0.Pipeline)
//        report error;
//    IF(
//}
//
//bool VdencPipeModeSelectCmd::Initialize(char *testname)
//{
//    //Find the xml
//    XML<cmdtype> xml(&m_reference, &m_field);
//    //Read xml to configure the cmd memeber
//    m_reference;
//    m_fieldToValidate,
//}



#include "pch.h"
#include "pugixml.hpp"
#include <iostream>
#include <string>

class xml
{
public:
    pugi::xml_document doc;
    int readconfig(const char* testname);
    void printallfield(const char* testname, const char* cmdname, const char* fieldname );
    pugi::char_t* getfield(const char* testname, const char* cmdname, const char* fieldname, const char* subfieldname);
};

int xml::readconfig(const char* testname)
{
    //load config xml file
    if (!doc.load_file(testname)) return -1;
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


pugi::char_t* xml::getfield(const char* testname, const char* cmdname, const char* fieldname, const char* subfieldname)
{
    // parse xml files, to get dwo.field0
    pugi::char_t fieldvalue[100] ;
    pugi::xml_node testnode = doc.child(testname);
    for (pugi::xml_node classnode : testnode.children())
    {   
        pugi::xml_node fieldnode = classnode.child(cmdname).child(fieldname);

        std::cout<<fieldnode.attribute(subfieldname).value();
        fieldvalue = fieldnode.attribute(subfieldname).value();

    }

    return fieldvalue;

}



int main()
{
    xml xml1;
    xml1.readconfig("config_mhw_vdbox_vdenc_hwcmd_g12_tglhp.h.xml");
    xml1.printallfield("TestName", "VDENC_PIPE_MODE_SELECT_CMD", "DW0");
    xml1.getfield("TestName", "VDENC_PIPE_MODE_SELECT_CMD", "DW0", "CommandType");

}

