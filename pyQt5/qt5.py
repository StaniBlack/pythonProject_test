import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout


app = QApplication([])
window = QWidget()
Layout = QVBoxLayout
Layout.addWidget(QPushButton('Top'))
Layout.addWidget(QPushButton('Bottom'))
window.setLayout(Layout)
window.show()




app.exec_()


