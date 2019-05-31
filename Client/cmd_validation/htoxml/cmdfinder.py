import os
import shutil
from ult_generator import header_parser
import pandas as pd
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import (
    Element, SubElement, XML, Comment
)
from ElementTree_pretty import prettify
import re

class CmdFinder(object):
    def __init__(self, source, gen, ringpath, ringfilename):
        self.source = source
        self.gen = gen
        self.ringpath = ringpath
        self.ringfilename = ringfilename   #could be ringcmd or vecs
        self.df_dic = {}
        self.full_ringinfo = []
        self.same = [['_ON_OFF','_CHECK'],['VEB','VEBOX'],['COST','COSTS'],['QMS','QM'],['IMAGE','IMG'],['WEIGHTSOFFSETS','WEIGHTS_OFFSETS']]
        self.ignored = ['CMD', 'COMMAND', 'OBJECT', 'MEDIA', 'STATE']
    
    def writexml(self, index = 0):
        #convert ringcmdinfo txt to df
        self.txt2df()
        self.extractdf()
        TestName = Element('TestName')  #create TestName as root node
        platform_group = SubElement(TestName, 'Platform', {'name': ''})
        
        for pair in self.full_ringinfo:
            #fullringcmd : [{'MI_LOAD_REGISTER_IMM': ['1108101d', '00000244']},...]
            for ringcmd, value_list in pair.items():
                platform_group = self.mapcmd(ringcmd, value_list, platform_group, index)
                index += 1
        print(prettify(TestName))

        with open( os.path.join(self.ringpath ,  "map" + self.ringfilename.strip(r'.txt') +".xml") , "w") as f:
            f.write(prettify(TestName))
        return prettify(TestName)
    
    def setbitfield(self, current_group, fieldname, bit_value, bit_l, bit_h, dw_no):
        #set bitfield attributes
        bitfield_group = SubElement(current_group, fieldname, {'default_value': bit_value, 
                                                                        'min_value': bit_value,
                                                                        'max_value': bit_value,
                                                                        'bitfield_l': bit_l,
                                                                        'bitfield_h': bit_h})   #set hex value , which represents defalt value of a bitfield
        
        if 'Address' in fieldname:
            bitfield_group.set('Address', 'Y')
            bitfield_group.set('CHECK', 'N')
        elif 'Reserved' in fieldname:
            bitfield_group.set('Address', 'N')
            bitfield_group.set('CHECK', 'N')
        elif dw_no == '0':
            bitfield_group.set('CHECK', 'N')
        else:
            bitfield_group.set('Address', 'N')
            bitfield_group.set('CHECK', 'Y')

        return current_group

    def mapcmd(self, ringcmd, value_list, node, index):
        # map each ringcmd
        # para source: search library path
        # para ringcmd: in ringcmdinfo cmd stringcmd, e.g.  "CMD_SFC_STATE_OBJECT"
        # para platform: platform_list = [8, 9, 10, 11, 12] represents gen8 to gen12; 
        #                If not set, defalt value 0 means search in all platforms and return the first match result
        # para value_list: hex stringcmd stream split in list,  eg. ['75010020', '00000041', '00ff00ff', '00000005', '00080350', '00ff00ff', '00000000', '00ff00ff', '00ff00ff', '00000000', '00000000', '00000000', '00000000', '000003ff', '00020000', '00020000', '00000000', '00f10000', '00000001', '00000000', '00e6b000', '00000001', '0000000e', '001b5000', '00000001', '0000000e', '00000000', '00000000', '00000000', '50000ffb', '00000000', '00000000', '00000000', '00000000']

        # return xml tree which map ringcmdinfo value in cmd struct definition
    
        #ringcmd_group = SubElement(platform_group, 'ringcmd', {'name' : ringcmd})  ##debug
        #convert hex stream to binary stream

        binv_list = [ bin(int(i, 16))[2:].zfill(32) for i in value_list ]   #each dword length = 32 bits(include leading 0)
        for r,d,f in os.walk(self.source):
            #filter test folder
            if r'\ult\agnostic\test' not in r:
                continue
            os.chdir(r)
            for thing in f:
                # find required cmd in xml file
                if thing.startswith('mhw_') and thing.endswith('.h.xml'):
                    if  self.gen == 'all' or self.gen != 'all' and str(self.gen) in thing:
                            tree = ET.parse(thing)
                            root = tree.getroot()
                            for Class in root.findall('class'):
                                for structcmd in Class.iter('struct'):
                                    # search cmd in all the local files
                                    if 'name' in structcmd.attrib and self.searchkword(ringcmd, structcmd.attrib['name']):
                                        #Class_group = SubElement(ringcmd_group, 'class', {'name' : Class.attrib['name']})  #debug
                                        structcmd_group = SubElement(node, 'CMD', {'name' : structcmd.attrib['name'],
                                                                                                'class' : Class.attrib['name'],
                                                                                                'index' : str(index)})
                                        dw_len = 0
                                        dw_no = ''
                                        for unionorcmd in structcmd.findall("./"):  #select all the direct children

                                            if unionorcmd.tag == 'union' and 'name' in unionorcmd.attrib and 'DW' in unionorcmd.attrib['name']:
                                                dw_no = unionorcmd.attrib['name'].strip('DW')
                                                val_str = self.findval(value_list, dw_no)['val_str']
                                                dword_group = SubElement(structcmd_group, 'dword', {'NO' : dw_no,
                                                                                                    'value': val_str})
                                                current_group = dword_group
                                                for s in unionorcmd.findall('struct'):
                                                    # 1 dword has several objs
                                                    if 'name' in s.attrib:
                                                        obj_group = SubElement(current_group, s.attrib['name'], {'value': val_str})
                                                        current_group = obj_group
                                                    for elem in s.findall("./"):
                                                        if 'name' in elem.attrib:
                                                            fieldname = elem.attrib['name']
                                                            if 'bitfield' in elem.attrib :
                                                                bit_item = elem.attrib['bitfield'].split(',')  #bitfield="0,  5"
                                                            else:
                                                                bit_item = []
                                                            bit_value, bit_l, bit_h = self.findbitval(binv_list, bit_item, dw_no)
                                                            current_group = self.setbitfield(current_group, fieldname, bit_value, bit_l, bit_h, dw_no)

                                                            #complement undefined dword length, for unmapped buffer stream
                                                            if fieldname == "DwordLength":
                                                                dw_len = int(bit_value,16) 

                                                    current_group = dword_group
                                            if unionorcmd.tag == 'otherCMD' and 'otherCMD' in unionorcmd.attrib:
                                                structcmd_group, dw_no = self.findcmd(structcmd_group, unionorcmd.attrib['otherCMD'], value_list, dw_no)

                                            if 'arraysize' in unionorcmd.attrib:


                                        #print(prettify(Result))
                                        #break
                                        if dw_len:
                                            if '_' in dw_no:
                                                dw_end = int(dw_no.split('_')[-1])
                                            else:
                                                dw_end = int(dw_no)
                                            if dw_end < dw_len:
                                                for i in range(dw_end+1, dw_len+2):
                                                    val_str = self.findval(value_list, str(i))['val_str']
                                                    dword_group = SubElement(structcmd_group, 'dword', {'NO' : str(i),
                                                                                                        'unmappedstr' : val_str})
                                        return node

        #cmd not found in local file
        ringcmd_group = SubElement(node, 'ringcmd', {'name' : ringcmd, 
                                                     'class' : 'not found' })
        return node

    def findcmd(self, node, cmd, value_list, base_dw_no):
        # find cmd according to name, append to node
        binv_list = [ bin(int(i, 16))[2:].zfill(32) for i in value_list ]   #each dword length = 32 bits(include leading 0)
        for r,d,f in os.walk(self.source):
            #filter test folder
            if r'\ult\agnostic\test' not in r:
                continue
            os.chdir(r)
            for thing in f:
                # find required cmd in xml file
                if thing.startswith('mhw_') and thing.endswith('.h.xml'):
                    if  self.gen == 'all' or self.gen != 'all' and str(self.gen) in thing:
                            tree = ET.parse(thing)
                            root = tree.getroot()
                            for Class in root.findall('class'):
                                for structcmd in Class.iter('struct'):
                                    # search cmd in all the local files
                                    if 'name' in structcmd.attrib and structcmd.attrib['name'] == cmd:
                            
                                        dw_len = 0
                                        dw_no = base_dw_no

                                        for unionorcmd in structcmd.findall("./"):  #select all the direct children
                                        
                                            if unionorcmd.tag == 'union' and 'name' in unionorcmd.attrib and 'DW' in unionorcmd.attrib['name']:
                                                dword_group = SubElement(node, 'dword', {'otherCMD': cmd,
                                                                                         'class' : Class.attrib['name']})
                                            
                                                dw_no = unionorcmd.attrib['name'].strip('DW')
                                                dic = self.findval(value_list, dw_no, base_dw_no)
                                                dw_no = dic['dw_no_new']

                                                dword_group.set('NO' , dw_no)
                                                dword_group.set('value', dic['val_str'])
                                                #dword_group = SubElement(structcmd_group, 'dword', {'NO' : dw_no,
                                                #                                                    'value': val_str})
                                                current_group = dword_group
                                                for s in unionorcmd.findall('struct'):
                                                    # 1 dword has several objs
                                                    if 'name' in s.attrib:
                                                        obj_group = SubElement(current_group, s.attrib['name'], {'value': val_str})
                                                        current_group = obj_group
                                                    for elem in s.findall("./"):
                                                        if 'name' in elem.attrib:
                                                            fieldname = elem.attrib['name']
                                                            if 'bitfield' in elem.attrib :
                                                                bit_item = elem.attrib['bitfield'].split(',')  #bitfield="0,  5"
                                                            else:
                                                                bit_item = []
                                                            bit_value, bit_l, bit_h = self.findbitval(binv_list, bit_item, dw_no)
                                                            current_group = self.setbitfield(current_group, fieldname, bit_value, bit_l, bit_h, dw_no)

                                                            #complement undefined dword length, for unmapped buffer stream
                                                            if fieldname == "DwordLength":
                                                                dw_len = int(bit_value,16) 

                                                    current_group = dword_group
                                            if unionorcmd.tag == 'otherCMD' and 'otherCMD' in unionorcmd.attrib:
                                                node, dw_no = self.findcmd(node, unionorcmd.attrib['otherCMD'], value_list, dw_no)
                                        return node, dw_no
        #cmd not found in local file
        dword_group = SubElement(node, 'dword', {'otherCMD': cmd,
                                                 'class' : 'not found'})
        return node, base_dw_no

    def extractdf(self, dfname = 'all'):
        #dfname options:
        #           'all': search in all the dfs
        #           'ContextRestore': search in ContextRestore portion
        #           'Workload': search in Workload portion
    
        #fullringcmd : [{'MI_LOAD_REGISTER_IMM': ['1108101d', '00000244']},...]
    
        df = self.df_dic[dfname]
        for i in df.index:
            #ringcmd = []
            self.full_ringinfo.append({df.loc[i,"Description"]:[x for x in df.loc[i,"Header":].values.tolist() if str(x) != 'nan']}) 
            #ringcmd.append([x for x in df.loc[i,"Header":].values.tolist() if str(x) != 'nan'])
            #full_ringinfo.append(ringcmd)
        return self.full_ringinfo

    def h2xml(self):
        parser_list = []
        for r,d,f in os.walk(self.source):
            #modify target file
            if r'\ult\agnostic\test' not in r:
                continue
            for thing in f:
                # filter all mhw cmd header file
                #if thing.startswith('mhw_') and re.search('g\d', thing) and thing.endswith('.h'):
                if self.gen != 'all':
                    if thing.startswith('mhw_') and re.search(f'g{self.gen}', thing) and thing.endswith('.h'):
                        parser_list.append(header_parser.HeaderParser(thing, r))
                else:
                    if thing.startswith('mhw_') and thing.endswith('.h'):
                        parser_list.append(header_parser.HeaderParser(thing, r))
                
        for item in parser_list:
            item.read_file()
            item.write_xml()

    def txt2df(self):
        #read ringcmdtringcmd text file into pd dataframe, which cmd stringcmd can be easily extracted
        ## only start after cmd "MI_BATCH_BUFFER_START"
        os.chdir(self.ringpath)
        comment_char = ['<', '-']
        with open(self.ringfilename, 'r') as f:
            df = pd.DataFrame()         #initialize
            start = 'MI_BATCH_BUFFER_START'
            start_fg = False

            for index, line in enumerate(f):
                # find header:
                if 'Count' in line:
                    columns = line.strip('-').split()  
                #elif '<ContextRestore' in line:
                #    c_start = in

                # skip the commented lines
                
                elif line[0] in comment_char:
                    continue

                elif not start_fg and start in line:
                    start_fg = True

                if start_fg: 
                    df = pd.concat( [df, pd.DataFrame([tuple(line.strip().split())])], ignore_index=True )


        # 
        last_col = int(columns[-1]) #last dword num
        tar_last_col = len(df.columns) - len(columns) + last_col
        if tar_last_col > last_col:
            columns.extend( [str(i) for i in range(last_col+1,  tar_last_col+1)])
            df.columns = columns
        

        # df = df.iloc[0:0] #clear dataframe memory
        # df.loc[2] #select one column
        # df.loc[:,'Descriptiono'] #select one row

        #print(df)
        #df_dic = {'ContextRestore': df}
        self.df_dic = {'all':df}
        return self.df_dic

    def findbitval(self, binv_list, bit_item, dw_no, base_dw_no = ''):
        # for otherCMD inside struct cmd, has base_dw_no
        if base_dw_no:
            if '_' in base_dw_no:
                bd = int(base_dw_no.split('_')[1].strip())+1
            else:
                bd = int(base_dw_no)+1
        else:
            bd = 0
        ##----------------------------------------
        if '_' in dw_no:
            dw_no_l = int(dw_no.split('_')[0].strip()) + bd 
            dw_no_h = int(dw_no.split('_')[1].strip()) + bd
        else:
            dw_no_l = int(dw_no) + bd
            dw_no_h = int(dw_no) + bd

        if bit_item:
            #find defalt hex value by field index
            bit_l = int(bit_item[0].strip())
            bit_h = int(bit_item[1].strip())
        else:
            #not have bit attrib
            bit_l = 0
            bit_h = (dw_no_h - dw_no_l + 1)*32 - 1

        if bit_l == 0:
            bit_value_raw =  ''.join(binv_list[dw_no_l: dw_no_h+1])[-bit_h-1 : ]
        else:
            bit_value_raw =  ''.join(binv_list[dw_no_l: dw_no_h+1])[-bit_h-1 : -bit_l]

        if bit_value_raw:
            bit_value = hex(int(bit_value_raw, 2))
        else:
            bit_value = '0x0'

        return bit_value, str(bit_l), str(bit_h)

    def findval(self, value_list, dw_no, base_dw_no = ''):
        # for otherCMD inside struct cmd, has base_dw_no
        if base_dw_no:
            if '_' in base_dw_no:
                bd = int(base_dw_no.split('_')[1].strip()) + 1
            else:
                bd = int(base_dw_no) + 1
        else:
            bd = 0
        ##----------------------------------------
        if '_' in dw_no:
            dw_no_l = int(dw_no.split('_')[0].strip()) + bd
            dw_no_h = int(dw_no.split('_')[1].strip()) + bd
            dw_no_new = str(dw_no_l) + '_' + str(dw_no_h)
        else:
            dw_no_l = int(dw_no) + bd
            dw_no_h = int(dw_no) + bd
            dw_no_new = str(dw_no_h)
        val_str =  ''.join(value_list[dw_no_l: dw_no_h+1])
        if [i for i in val_str if i != '0']:
            val_str = '0x'+val_str
        else:
            val_str = '0x0'
        return dict(val_str = val_str, dw_no_new = dw_no_new)

    def searchkword(self, ringcmd, localcmd):
        #ringcmd: in ringcmdinfo "CMD_SFC_STATE_OBJECT"
        #local: in header file "SFC_STATE_CMD"
        #For match purpose
        if self.equal_list(ringcmd, localcmd):
            return True
        else:
            for l in self.same:
                for index, item in enumerate(l):
                    if item in ringcmd:
                        ringcmd_new = ringcmd.replace(item, l[len(l)-1-index])
                        return self.equal_list(ringcmd_new, localcmd)
            return False

    def equal_list(self, str1, str2):
        #split str with '_'
        #compare 2 lists after ignoringcmd some keywords
        l1 = str1.split('_')
        l2 = str2.split('_')
        ignored = set(self.ignored)
        for k1 in l1:
            if k1 not in ignored and k1 not in l2:
                return False
        for k2 in l2:
            if k2 not in ignored and k2 not in l1:
                return False
        return True

    

#----------------------------------------------------------------
ringpath = r'C:\projects\github\AutoULTGen\cmd_validation\vcstringinfo'
ringfilename = 'VcsRingInfo_0_0.txt'
gen = 12
source = r'C:\Users\jiny\gfx\gfx-driver\Source\media'
#----------------------------------------------------------------

#----------------------------------------------------------------
#init
obj = CmdFinder(source, gen, ringpath, ringfilename)
#obj.h2xml()
obj.writexml()
#----------------------------------------------------------------
#countlines(source)
#cpfiles(source)