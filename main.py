from PyQt5 import uic, QtWidgets

ModeForm, _ = uic.loadUiType("uis/mode.ui")


class ModeUI(QtWidgets.QMainWindow, ModeForm):
    def __init__(self):
        super(ModeUI, self).__init__()
        self.setupUi(self)

        self.radioButton.toggled.connect(self.onClicked)
        self.radioButton_2.toggled.connect(self.onClicked)

    def onClicked(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            print("Country is %s" % (radioButton.text()))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = ModeUI()
    w.show()  # show window
    sys.exit(app.exec_())