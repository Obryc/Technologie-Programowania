import sys
from PyQt5.QtWidgets import (QApplication, QDialog, QComboBox, QDoubleSpinBox, QVBoxLayout, QGridLayout, QLabel)
class Przeliczanie(QDialog):
    def __init__(self):
        super().__init__()
        fahrenheitaLabel = QLabel("fahtenheit: ")
        self.fahrenheitSpinBox = QDoubleSpinBox()
        self.fahrenheitSpinBox.setRange(-200,200)
        self.fahrenheitSpinBox.setValue(0)

        self.fahrenheitSpinBox.valueChanged.connect(self.przelicz)

        self.censjuszaLabel = QLabel("censjusz")
        self.censjusz = QLabel()


        gridLayout = QGridLayout()
        gridLayout.addWidget(fahrenheitaLabel, 0, 0)
        gridLayout.addWidget(self.fahrenheitSpinBox, 0, 1)
        gridLayout.addWidget(self.censjuszaLabel, 3, 0)
        gridLayout.addWidget(self.censjusz, 3, 1)
        vLayout = QVBoxLayout()
        vLayout.addLayout(gridLayout)
        self.setLayout(vLayout)


        self.przelicz()
    def przelicz(self):
        p = self.fahrenheitSpinBox.value()
        f = (p-32)/(9/5)
        self.censjuszaLabel.setText('W skali Censjusza to: {0:.2f}'.format(f))


        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Przeliczanie()
    demo.show()
    sys.exit(app.exec_())
