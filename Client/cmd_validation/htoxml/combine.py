import os
import shutil
import re

def combine(inputpath):
    os.chdir(inputpath)
    with open('DDIEnc_all.txt','w') as wfd:
        for f in os.listdir(inputpath):
            pattern = re.search('^(\d)-0.*DDIEnc_(.*)Params_._Frame.txt', f)
            if pattern:
                FrameNo = str(int(pattern.group(1))+1)
                ParaGroup = pattern.group(2)
                wfd.write('<Frame No=%s  Param=%s >\n' % (FrameNo, ParaGroup))
                with open(f,'r') as fd:
                    shutil.copyfileobj(fd, wfd)

#----------------------------------------------------------------
inputpath = r'C:\projects\github\AutoULTGen\cmd_validation\vcstringinfo\HEVC-VDENC-Grits001 - 1947\DDI_Input'
#----------------------------------------------------------------
combine(inputpath)



