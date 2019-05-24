import os
import shutil
from ult_generator import header_parser
import pandas as pd
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import (
    Element, SubElement, tostring, XML, Comment
)
from ElementTree_pretty import prettify

def countlines(start, lines=0, header=True, begin_start=None):
    if header:
        print('{:>10} |{:>10} | {:<20}'.format('ADDED', 'TOTAL', 'FILE'))
        print('{:->11}|{:->11}|{:->20}'.format('', '', ''))

    for r,d,f in os.walk(start):
        for thing in f:
            # filter all mhw cmd header file
            if thing.startswith('mhw_') and 'cmd' in thing and 'g12' in thing and thing.endswith('.h'):
                thing = os.path.join(r, thing)
                with open(thing, 'rb') as f:    #'rb' fix reading errors
                    newlines = f.readlines()
                    newlines = len(newlines)
                    lines += newlines

                    if begin_start is not None:
                        reldir_of_thing = '.' + thing.replace(begin_start, '')
                    else:
                        reldir_of_thing = '.' + thing.replace(start, '')

                    print('{:>10} |{:>10} | {:<20}'.format(
                            newlines, lines, reldir_of_thing))

            if os.path.isdir(thing):
                lines = countlines(thing, lines, header=False, begin_start=start)
    return lines

def cpfiles(source, target,  lines=0, header=True, begin_start=None):
    if header:
        print('{:>10} |{:>10} | {:<20}'.format('COPIED', 'TOTAL', 'FILE'))
        print('{:->11}|{:->11}|{:->20}'.format('', '', ''))

        for r,d,f in os.walk(source):
            for thing in f:
                # filter all mhw cmd header file
                if thing.startswith('mhw_') and 'cmd' in thing and '_g' in thing and thing.endswith('.h'):
                    fullthing = os.path.join(r, thing)
                    dstdir =  os.path.join(target, r.replace(source, '.'))
                    if not os.path.exists(dstdir):
                        os.makedirs(dstdir) # create directories, raise an error if it already exists
                    shutil.copy(fullthing, dstdir)

                    with open(fullthing, 'rb') as f:    #'rb' fix reading errors
                        newlines = f.readlines()
                        newlines = len(newlines)
                        lines += newlines

                        print('{:>10} |{:>10} | {:<20}'.format(
                                newlines, lines, fullthing.replace(source, '.')))

                if os.path.isdir(thing):
                    lines = countlines(thing, lines, header=False, begin_start=source)
        return lines

def h2xml(target):
    parser_list = []
    for r,d,f in os.walk(target):
        for thing in f:
            # filter all mhw cmd header file
            if thing.startswith('mhw_') and 'cmd' in thing and '_g' in thing and thing.endswith('.h'):
                parser_list.append(header_parser.HeaderParser(thing, r))
                
    for item in parser_list:
        item.read_file()
        item.write_xml()

def mapxml(TestName, target, vcs, value_list, platform = 'all'):
    # para target: search library path
    # para vcs: in vcsinfo cmd string, e.g.  "CMD_SFC_STATE_OBJECT"
    # para platform: platform_list = [8, 9, 10, 11, 12] represents gen8 to gen12; 
    #                If not set, defalt value 0 means search in all platforms and return the first match result
    # para value_list: hex string stream split in list,  eg. ['75010020', '00000041', '00ff00ff', '00000005', '00080350', '00ff00ff', '00000000', '00ff00ff', '00ff00ff', '00000000', '00000000', '00000000', '00000000', '000003ff', '00020000', '00020000', '00000000', '00f10000', '00000001', '00000000', '00e6b000', '00000001', '0000000e', '001b5000', '00000001', '0000000e', '00000000', '00000000', '00000000', '50000ffb', '00000000', '00000000', '00000000', '00000000']

    # return xml tree which map vcsinfo value in cmd struct definition
    platform_group = SubElement(TestName, 'Platform')
    vcs_group = SubElement(platform_group, 'vcs', {'name' : vcs})
    #convert hex stream to binary stream
    binv_list = [ bin(int(i, 16))[2:].zfill(32) for i in value_list ]   #each dword length = 32 bits(include leading 0)

    for r,d,f in os.walk(target):
        os.chdir(r)
        for thing in f:
            # find required cmd in xml file
            if thing.startswith('mhw_') and 'cmd' in thing and '_g' in thing and thing.endswith('.h.xml'):
                if platform == 'all' or platform != 'all' and str(platform) in thing:
                        tree = ET.parse(thing)
                        root = tree.getroot()
                        for Class in root.findall('class'):
                            for structcmd in root.iter('struct'):
                                # search cmd in all the local files
                                if 'name' in structcmd.attrib and searchkword(vcs, structcmd.attrib['name']):
                                    Class_group = SubElement(vcs_group, 'class', {'name' : Class.attrib['name']})
                                    structcmd_group = SubElement(Class_group, 'cmd', {'name' : structcmd.attrib['name']})

                                    dw_len = 0
                                    for union in structcmd.findall('union'):
                                        if 'name' in union.attrib and 'DW' in union.attrib['name']:
                                            dw_no = union.attrib['name'].strip('DW')
                                            dword_group = SubElement(structcmd_group, 'dword', {'NO' : dw_no})
                                            for s in union.iter('struct'):
                                                for elem in s.iter():
                                                    if 'name' in elem.attrib:
                                                        if 'bitfield' in elem.attrib :
                                                            bit_item = elem.attrib['bitfield'].split(',')  #bitfield="0,  5"
                                                        else:
                                                            bit_item = []

                                                        bit_value, bit_l, bit_h = findbitval(bit_item, binv_list, dw_no)
                                                        bitfield_group = SubElement(dword_group, elem.attrib['name'], {'defalt_value': bit_value, 
                                                                                                                        'min_value': bit_value,
                                                                                                                        'max_value': bit_value,
                                                                                                                        'bitfield_l': bit_l,
                                                                                                                        'bitfield_h': bit_h})   #set hex value , which represents defalt value of a bitfield
                                                        if 'Address' in elem.attrib['name']:
                                                            bitfield_group.set('Address', 'Y')
                                                            bitfield_group.set('CHECK', 'N')
                                                        elif 'Reserved' in elem.attrib['name']:
                                                            bitfield_group.set('Address', 'N')
                                                            bitfield_group.set('CHECK', 'N')
                                                        else:
                                                            bitfield_group.set('Address', 'N')
                                                            bitfield_group.set('CHECK', 'Y')
                                                        #complement undefined dword length, for unmapped buffer stream
                                                        if elem.attrib['name'] == "DwordLength":
                                                            dw_len = int(bit_value,16) 

                                    #print(prettify(Result))
                                    #break
                                    if dw_len:
                                        if int(dw_no[-1]) < dw_len:
                                            for i in range(int(dw_no[-1])+1, dw_len+2):
                                                dword_group = SubElement(structcmd_group, 'dword', {'NO' : str(i),
                                                                                                    'unmappedstr' : value_list[i]})
                                    return TestName

    #cmd not found in local file
    Class_group = SubElement(vcs_group, 'class', {'name' : 'Not Found'})
    return TestName
                   
def findbitval(bit_item, binv_list, dw_no):
    
    if '_' in dw_no:
        dw_no_l = int(dw_no.split('_')[0].strip())
        dw_no_h = int(dw_no.split('_')[1].strip())
    else:
        dw_no_l = int(dw_no)
        dw_no_h = int(dw_no)

    if bit_item:
        #find defalt hex value by field index
        bit_l = int(bit_item[0].strip())
        bit_h = int(bit_item[1].strip())
    else:
        #not have bit attrib
        bit_l = 0
        bit_h = (dw_no_h - dw_no_l + 1)*32

    if bit_l == 0:
        bit_value_raw =  ''.join(binv_list[dw_no_l: dw_no_h+1])[-bit_h-1 : ]
    else:
        bit_value_raw =  ''.join(binv_list[dw_no_l: dw_no_h+1])[-bit_h-1 : -bit_l]

    if bit_value_raw:
        bit_value = hex(int(bit_value_raw, 2))
    else:
        bit_value = '0x0'.zfill(8)

    return bit_value, str(bit_l), str(bit_h)


def searchkword(vcs, localcmd):
    #vcs: in vcsinfo "CMD_SFC_STATE_OBJECT"
    #local: in header file "SFC_STATE_CMD"
    #For match purpose
    vcs_list = vcs.split('_')
    local_list = localcmd.split('_')
    ignored = ['CMD', 'OBJECT', 'STATE']
    return equal_list(vcs_list, local_list, ignored)

def equal_list(l1, l2, ignored):
    #compare 2 lists after ignoring some keywords
    if 'CHECK' in l1:
        l1.remove('CHECK')
        l1.append('ON')
        l1.append('OFF')
    if 'CHECK' in l2:
        l2.remove('CHECK')
        l2.append('ON')
        l2.append('OFF')

    ignored = set(ignored)
    for k1 in l1:
        if k1 not in ignored and k1 not in l2:
            return False
    for k2 in l2:
        if k2 not in ignored and k2 not in l1:
            return False
    return True


def txt2df(vcspath):
    #read vcstring text file into pd dataframe, which cmd string can be easily extracted
    os.chdir(vcspath)
    comment_char = ['<', '-']
    with open('VecsRingInfo_0_0.txt', 'r') as f:
        df = pd.DataFrame()         #initialize 
        for index, line in enumerate(f):
            # find header:
            if 'Count' in line:
                columns = line.strip('-').split()  
            #elif '<ContextRestore' in line:
            #    c_start = in

            # skip the commented lines
            elif line[0] in comment_char:
                continue

            else:
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
    df_dic = {'all':df}
    return df_dic


def extractdf(df_dic, dfname = 'all'):
    #df_list means df extracted from vcstring file


    #dfname options:
    #           'all': search in all the dfs
    #           'ContextRestore': search in ContextRestore portion
    #           'Workload': search in Workload portion
    
    #fullvcs : [{'MI_LOAD_REGISTER_IMM': ['1108101d', '00000244']},...]

    
    df = df_dic[dfname]
    full_vcs = []

    for i in df.index:
        #vcs = []
        full_vcs.append({df.loc[i,"Description"]:[x for x in df.loc[i,"Header":].values.tolist() if str(x) != 'nan']}) 
        #vcs.append([x for x in df.loc[i,"Header":].values.tolist() if str(x) != 'nan'])
        #full_vcs.append(vcs)
    return full_vcs

def searchvcs(full_vcs, vcs):
        #vcs options:
        #            cmdname : search by cmdname, e.g. "CMD_SFC_STATE_OBJECT"
        pass
#----------------------------------------------------------------
#dic: {gennumber:(source, target),}
dic = {12: (r'C:\Users\jiny\gfx\gfx-driver\Source\media\media_embargo\agnostic\gen12', r'C:\Users\jiny\gfx\gfx-driver\Source\media\media_embargo\media_driver_next\ult\agnostic\test\gen12'),
       11: (r'C:\Users\jiny\gfx\gfx-driver\Source\media\media_driver\agnostic', r'C:\Users\jiny\gfx\gfx-driver\Source\media\media_driver\ult\agnostic\test')}  
vcspath = r'c:\projects\github\autoultgen\cmd_validation\vcstringinfo'
#string = "75010020  00000041  00ff00ff  00000005  00080350  00ff00ff  00000000  00ff00ff  00ff00ff  00000000  00000000  00000000  00000000  000003ff  00020000  00020000  00000000  00f10000  00000001  00000000  00e6b000  00000001  0000000e  001b5000  00000001  0000000e  00000000  00000000  00000000  50000ffb  00000000  00000000  00000000  00000000"
#cmdname = "CMD_SFC_STATE_OBJECT"
df_dic = txt2df(vcspath)
full_vcs = extractdf(df_dic)
gen = 11
source, target = dic[gen]
#----------------------------------------------------------------
#countlines(source)
#cpfiles(source, target)
#h2xml(target)
TestName = Element('TestName')  #create TestName as root node
for pair in full_vcs:
    #fullvcs : [{'MI_LOAD_REGISTER_IMM': ['1108101d', '00000244']},...]
    for cmdname, value_list in pair.items():
        #if mapxml(target, cmdname, value_list, 11):
        #    result += mapxml(TestName, target, cmdname, value_list, 11)
        TestName = mapxml(TestName, target, cmdname, value_list, gen)
        #print(result)
print(prettify(TestName))

with open( os.path.join(vcspath ,  "mapvecstring.xml") , "w") as f:
    f.write(prettify(TestName))



