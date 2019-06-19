import sys
import os
import re
import shutil
from PySide2.QtWidgets import (QLineEdit, QPushButton, QApplication,
                            QVBoxLayout, QDialog, QMainWindow, QFileDialog, QMessageBox, QErrorMessage)
from PySide2.QtQuick import QQuickView
from PySide2.QtCore import QUrl, Slot, QFile
from PySide2.QtUiTools import QUiLoader
from ui_inputwindow import Ui_InputWindow
#----------------------------------------------------------------

#----------------------------------------------------------------
class InputWindow(QMainWindow):
    def __init__(self):
        super(InputWindow, self).__init__()
        self.ui = Ui_InputWindow()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.addHeader)
        self.ui.buttonBox.rejected.connect(self.reject)
        self.ui.SelectPath.clicked.connect(self.selectpath)

    @Slot()
    def addHeader(self):
        # click OK, generate xml header
        self.Component = self.ui.Component_input.text()
        self.GUID = self.ui.GUID_input.text()
        self.Width = self.ui.Width_input.text()
        self.Height = self.ui.Height_input.text()
        self.OutputFormat = self.ui.OutputFormat_input.text()
        self.inputpath = self.ui.InputPathText.text()
        self.combine()
        msgBox = QMessageBox()
        msgBox.setText("The input file has been generated.")
        msgBox.exec_()
        #self.Header.set('Componet', Component)
        #self.Header.set('GUID', GUID)
        #self.Header.set('Width', Width)
        #self.Header.set('Height', Height)
        #self.Header.set('OutputFormat', OutputFormat)
    
    @Slot()
    def reject(self):
        # click cancel, exit
        sys.exit(app.exec_())

    def combine(self):
        #combine ddi_input text files and add header infomation
        os.chdir(self.inputpath)
        with open('DDIEnc_all.txt','w') as wfd:
            wfd.write('<Header Component=%s  GUID=%s Width=%s Height=%s OutputFormat=%s>\n' % (self.Component, self.GUID, self.Width, self.Height, self.OutputFormat))
            for f in os.listdir(self.inputpath):
                pattern = re.search('^(\d)-0.*DDIEnc_(.*)Params_._Frame.txt', f)
                if pattern:
                    FrameNo = str(int(pattern.group(1))+1)
                    ParaGroup = pattern.group(2)
                    wfd.write('<Frame No=%s  Param=%s >\n' % (FrameNo, ParaGroup))
                    with open(f,'r') as fd:
                        shutil.copyfileobj(fd, wfd)
                    wfd.write('</Frame>\n')
            wfd.write('</Header>')
        
    @Slot()
    def selectpath(self):
        #open file dialog and display directory in the text edit area
        dir = QFileDialog.getExistingDirectory(self, "Open Directory",
                                       "/home",
                                       QFileDialog.ShowDirsOnly
                                       | QFileDialog.DontResolveSymlinks)
        self.ui.InputPathText.setText(dir)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    input_window = InputWindow()
    input_window.show()
    sys.exit(app.exec_())
#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------
