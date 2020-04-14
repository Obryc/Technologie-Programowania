import sys
from PyQt5.QtWidgets import (QApplication, QDialog, QComboBox, QDoubleSpinBox, QVBoxLayout, QGridLayout, QLabel , QPushButton)



class przeliczanie(QDialog):
    def __init__(self):
     
        super().__init__() 

        

        self.button1 = QPushButton("dolar na złoty", self)
        gridLayout = QGridLayout()
        gridLayout.addWidget(self.button1, 0, 0)
        

        self.button2 = QPushButton("złoty na dolar", self)
        gridLayout = QGridLayout()
        gridLayout.addWidget(self.button2, 1, 0)

        vLayout = QVBoxLayout()
        vLayout.addLayout(gridLayout)
        self.setLayout(vLayout)
        
        self.box1 = QLabel()
        self.spinbox1Label = QLabel("waluta")
        self.spinbox2Label = QLabel("kurs")
        self.SpinBox1 = QDoubleSpinBox()
        self.SpinBox1.setRange(-200,200)
        self.SpinBox1.setValue(0)
        self.SpinBox2 = QDoubleSpinBox()
        self.SpinBox2.setRange(-200,200)
        self.SpinBox2.setValue(0)
        gridLayout.addWidget(self.box1, 0, 1)
        gridLayout.addWidget(self.spinbox1Label, 0, 1)
        gridLayout.addWidget(self.SpinBox1, 0, 2)
        gridLayout.addWidget(self.spinbox2Label, 2, 1)
        gridLayout.addWidget(self.SpinBox2, 2, 2)
        self.walutaLabel = QLabel("przeliczone")
        gridLayout.addWidget(self.walutaLabel, 3,1)
        
        self.button2.clicked.connect(self.plnUsd)
        self.button1.clicked.connect(self.usdPln)

        
    def plnUsd(self):
        p = self.SpinBox1.value()
        h = p/self.SpinBox2.value()
        self.walutaLabel.setText('w dolarach wynosi: {0:.2f}'.format(h))
        
    def usdPln(self):
        p = self.SpinBox1.value()
        h = p*self.SpinBox2.value()
        self.walutaLabel.setText('w złotych wynosi: {0:.2f}'.format(h))
    



if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = przeliczanie()
    demo.show()
    sys.exit(app.exec_())