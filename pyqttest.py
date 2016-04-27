# encoding: UTF-8


import sys
from PyQt4 import QtGui, QtCore


########################################################################
class SliderLabel(QtGui.QWidget):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent = None):
        """Constructor"""
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('SliderLabel')
        self.slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        self.slider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.slider.setGeometry(30, 40, 100, 30)
        self.connect(self.slider, QtCore.SIGNAL('valueChanged(int)'),
                     self.changeValue)
        self.label = QtGui.QLabel(self)
        self.label.setPixmap(QtGui.QPixmap('icons/mute.png'))
        self.label.setGeometry(160, 40, 80, 30)
        
    #----------------------------------------------------------------------
    def changeValue(self):
        """"""
        pos = self.slider.value()
        if pos == 0:
            self.label.setPixmap(QtGui.QPixmap('icons/mute.png'))
        elif 0 < pos <= 30:
            self.label.setPixmap(QtGui.QPixmap('icons/min.png'))
        elif 30 < pos < 80:
            self.label.setPixmap(QtGui.QPixmap('icons/med.png'))
        else:
            self.label.setPixmap(QtGui.QPixmap('icons/max.png'))

########################################################################
class ProgressBar(QtGui.QWidget):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        QtGui.QWidget.__init__(self)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('ProgressBar')
        
        self.pbar = QtGui.QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)
        
        self.button = QtGui.QPushButton('Start', self)
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button.move(40, 80)
        
        self.connect(self.button, QtCore.SIGNAL('clicked()'),
                     self.onStart)
        self.timer = QtCore.QBasicTimer()
        self.step = 0
        
    #----------------------------------------------------------------------
    def timerEvent(self, event):
        """"""
        if self.step >= 100:
            self.timer.stop()
            return
        self.step = self.step + 1
        self.pbar.setValue(self.step)
        
    #----------------------------------------------------------------------
    def onStart(self):
        """"""
        if self.timer.isActive():
            self.timer.stop()
            self.button.setText('Start')
        else:
            self.timer.start(100, self)
            self.button.setText('Stop')
        
    
########################################################################
class Calendar(QtGui.QWidget):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent = None):
        """Constructor"""
        QtGui.QWidget.__init__(self)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.cal = QtGui.QCalendarWidget(self)
        self.cal.setGridVisible(True)
        self.connect(self.cal, QtCore.SIGNAL('selectionChanged()'),
                     self.showDate)
        self.label = QtGui.QLabel(self)
        date = self.cal.selectedDate()
        self.label.setText(str(date.toPyDate()))
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.cal)
        vbox.addWidget(self.label)
        self.setLayout(vbox)
    
    #----------------------------------------------------------------------
    def showDate(self):
        """"""
        date = self.cal.selectedDate()
        self.label.setText(str(date.toPyDate()))


########################################################################
class StandardDialog(QtGui.QDialog):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent = None):
        """Constructor"""
        super(StandardDialog, self).__init__(parent)
        
        self.setWindowTitle('Standard Dialog')
        
        filePushButton = QtGui.QPushButton(u'文本对话框')
        colorPushButton = QtGui.QPushButton(u'颜色对话框')
        fontPushButton = QtGui.QPushButton(u'字体对话框')
        
        self.fileLineEdit = QtGui.QLineEdit()
        self.colorFrame = QtGui.QFrame()
        self.colorFrame.setFrameShape(QtGui.QFrame.Box)
        self.colorFrame.setAutoFillBackground(True)
        self.fontLineEdit = QtGui.QLineEdit('Hello World!')
        
        layout = QtGui.QGridLayout()
        layout.addWidget(filePushButton, 0, 0)
        layout.addWidget(self.fileLineEdit, 0, 1)
        layout.addWidget(colorPushButton, 1, 0)
        layout.addWidget(self.colorFrame, 1, 1)
        layout.addWidget(fontPushButton, 2, 0)
        layout.addWidget(self.fontLineEdit, 2, 1)
        
        self.setLayout(layout)
        
        self.connect(filePushButton, QtCore.SIGNAL('clicked()'), self.openFile)
        self.connect(colorPushButton, QtCore.SIGNAL('clicked()'), self.openColor)
        self.connect(fontPushButton, QtCore.SIGNAL('clicked()'), self.openFont)
        
    #----------------------------------------------------------------------
    def openFile(self):
        """"""
        s = QtGui.QFileDialog.getOpenFileName(self, "Open file dialog", '/', 'Python files(*.py)')
        self.fileLineEdit.setText(str(s))
    
    #----------------------------------------------------------------------
    def openColor(self):
        """"""
        c = QtGui.QColorDialog.getColor(QtCore.Qt.blue)
        if c.isValid():
            self.colorFrame.setPalette(QtGui.QPalette(c))
            
    #----------------------------------------------------------------------
    def openFont(self):
        """"""
        f, ok = QtGui.QFontDialog.getFont()
        if ok:
            self.fontLineEdit.setFont(f)


########################################################################
class Geometry(QtGui.QDialog):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent = None):
        """Constructor"""
        super(Geometry, self).__init__(parent)
        
        Label1 = QtGui.QLabel('x0:')
        Label2 = QtGui.QLabel('y0:')
        Label3 = QtGui.QLabel('frameGeometry():')
        Label4 = QtGui.QLabel('pos():')
        Label5 = QtGui.QLabel('geometry():')
        Label6 = QtGui.QLabel('width():')
        Label7 = QtGui.QLabel('height():')
        Label8 = QtGui.QLabel('rect():')
        Label9 = QtGui.QLabel('size():')
        
        self.xLabel = QtGui.QLabel()
        self.yLabel = QtGui.QLabel()
        self.frameGeoLabel = QtGui.QLabel()
        self.posLabel = QtGui.QLabel()
        self.geoLabel = QtGui.QLabel()
        self.widthLabel = QtGui.QLabel()
        self.heightLabel = QtGui.QLabel()
        self.rectLabel = QtGui.QLabel()
        self.sizeLabel = QtGui.QLabel()
        
        layout = QtGui.QGridLayout()
        layout.addWidget(Label1, 0, 0)
        layout.addWidget(self.xLabel, 0, 1)
        layout.addWidget(Label2, 1, 0)
        layout.addWidget(self.yLabel, 1, 1)
        layout.addWidget(Label3, 2, 0)
        layout.addWidget(self.frameGeoLabel, 2, 1)
        layout.addWidget(Label4, 3, 0)
        layout.addWidget(self.posLabel, 3, 1)
        layout.addWidget(Label5, 4, 0)
        layout.addWidget(self.geoLabel, 4, 1)
        layout.addWidget(Label6, 5, 0)
        layout.addWidget(self.widthLabel, 5, 1)
        layout.addWidget(Label7, 6, 0)
        layout.addWidget(self.heightLabel, 6, 1)
        layout.addWidget(Label8, 7, 0)
        layout.addWidget(self.rectLabel, 7, 1)
        layout.addWidget(Label9, 8, 0)
        layout.addWidget(self.sizeLabel, 8, 1)
        
        self.setLayout(layout)
        self.updateLabel()
        
    #----------------------------------------------------------------------
    def moveEvent(self, event):
        """"""
        self.updateLabel()
        
    #----------------------------------------------------------------------
    def resizeEvent(self, event):
        """"""
        self.updateLabel()
        
    #----------------------------------------------------------------------
    def updateLabel(self):
        """"""
        temp = QtCore.QString()
        
        self.xLabel.setText(temp.setNum(self.x()))
        self.yLabel.setText(temp.setNum(self.y()))
        self.frameGeoLabel.setText(temp.setNum(self.frameGeometry().x())+'.'+
                                   temp.setNum(self.frameGeometry().y())+'.'+
                                   temp.setNum(self.frameGeometry().width())+'.'+
                                   temp.setNum(self.frameGeometry().height()))
        self.posLabel.setText(temp.setNum(self.pos().x())+'.'+
                              temp.setNum(self.pos().y()))
        self.geoLabel.setText(temp.setNum(self.geometry().x())+'.'+
                              temp.setNum(self.geometry().y())+'.'+
                              temp.setNum(self.geometry().width())+'.'+
                              temp.setNum(self.geometry().height()))
        self.widthLabel.setText(temp.setNum(self.width()))
        self.heightLabel.setText(temp.setNum(self.height()))
        self.rectLabel.setText(temp.setNum(self.rect().x())+'.'+
                               temp.setNum(self.rect().y())+'.'+
                               temp.setNum(self.rect().width())+'.'+
                               temp.setNum(self.rect().height()))
        self.sizeLabel.setText(temp.setNum(self.size().width())+'.'+
                               temp.setNum(self.size().height()))


########################################################################
class MyQQ(QtGui.QToolBox):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent = None):
        """Constructor"""
        super(MyQQ, self).__init__(parent)
        
        toolButton1_1 = QtGui.QToolButton()
        toolButton1_1.setText(u'休眠')
        toolButton1_1.setIcon(QtGui.QIcon('image/9.gif'))
        toolButton1_1.setIconSize(QtCore.QSize(60, 60))
        toolButton1_1.setAutoRaise(True)
        toolButton1_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        
        toolButton2_1 = QtGui.QToolButton()
        toolButton2_1.setText(u'天的另一边')
        toolButton2_1.setIcon(QtGui.QIcon("image/5.gif"))
        toolButton2_1.setIconSize(QtCore.QSize(60, 60))
        toolButton2_1.setAutoRaise(True)
        toolButton2_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        
        groupbox1 = QtGui.QGroupBox()
        vlayout1 = QtGui.QVBoxLayout(groupbox1)
        vlayout1.setMargin(10)
        vlayout1.setAlignment(QtCore.Qt.AlignCenter)
        vlayout1.addWidget(toolButton1_1)
        
        groupbox2 = QtGui.QGroupBox()
        vlayout2 = QtGui.QVBoxLayout(groupbox2)
        vlayout2.setMargin(10)
        vlayout2.setAlignment(QtCore.Qt.AlignCenter)
        vlayout2.addWidget(toolButton2_1)
        
        self.addItem(groupbox1, u'我的好友')
        self.addItem(groupbox2, u'同事')
        

########################################################################
class MyTable(QtGui.QTableWidget):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent = None):
        """Constructor"""
        super(MyTable, self).__init__(parent)
        
        self.setColumnCount(5)
        self.setRowCount(2)
        self.setItem(0, 0, QtGui.QTableWidgetItem(u'性别'))
        self.setItem(0, 1, QtGui.QTableWidgetItem(u'姓名'))
        self.setItem(0, 2, QtGui.QTableWidgetItem(u'出生日期'))
        self.setItem(0, 3, QtGui.QTableWidgetItem(u'职业'))
        self.setItem(0, 4, QtGui.QTableWidgetItem(u'收入'))
        
        lbp1 = QtGui.QLabel()
        lbp1.setPixmap(QtGui.QPixmap('image/4.gif'))
        self.setCellWidget(1, 0, lbp1)
        twi1 = QtGui.QTableWidgetItem('tom')
        self.setItem(1, 1, twi1)
        dte1 = QtGui.QDateTimeEdit()
        dte1.setDateTime(QtCore.QDateTime.currentDateTime())
        dte1.setDisplayFormat('yyyy/mm/dd')
        dte1.setCalendarPopup(True)
        self.setCellWidget(1, 2, dte1)
        cbw = QtGui.QComboBox()
        cbw.addItem('worker')
        cbw.addItem('famer')
        cbw.addItem('doctor')
        cbw.addItem('lawyer')
        cbw.addItem('soldier')
        self.setCellWidget(1, 3, cbw)
        sb1 = QtGui.QSpinBox()
        sb1.setRange(1000, 10000)
        self.setCellWidget(1, 4, sb1)
    
    


app = QtGui.QApplication(sys.argv)
w = MyTable()
w.show()
sys.exit(app.exec_())
        
        
    
    