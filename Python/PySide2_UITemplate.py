import sys
import webbrowser
from PySide2 import QtGui
from PySide2 import QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setWindowTitle('UI Template')
        self.setFixedSize(300, 180)

        # Menu
        menu = self.menuBar()
        fileMenu = menu.addMenu("File")
        helpMenu = menu.addMenu("About")
        # Exit QAction
        exitAction = QtWidgets.QAction("Exit", self)
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)
        # Documentation QAction
        aboutAction = QtWidgets.QAction("Documentation", self)
        aboutAction.setStatusTip('Open documentation URL')
        aboutAction.triggered.connect(self.documentation)
        helpMenu.addAction(aboutAction)
        # About QAction
        aboutAction = QtWidgets.QAction("About", self)
        aboutAction.setStatusTip('About this app')
        aboutAction.triggered.connect(self.about)
        helpMenu.addAction(aboutAction)

        # Center Layout
        layout =  QtWidgets.QVBoxLayout()
        # Label
        label = QtWidgets.QLabel("Enter your name:", self)
        layout.addWidget(label)

        # Text field
        self.textField = QtWidgets.QLineEdit(self)
        self.textField.setStatusTip('Enter text')
        layout.addWidget(self.textField)
        # Checkbox
        self.checkbox = QtWidgets.QCheckBox("Add name", self)
        self.checkbox.setStatusTip('Check it')
        layout.addWidget(self.checkbox)
        # Button
        button = QtWidgets.QPushButton( 'Click me' )
        button.setStatusTip('Click it')
        button.pressed.connect(lambda: self.buttonClick('!') )
        layout.addWidget(button)

        # Central Widget
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # Status Bar
        status = self.statusBar()
        status.showMessage('Ready...')

    def documentation(self):
        url = 'http://google.com/'
        webbrowser.open(url)

    def about(self):
        QtWidgets.QMessageBox.about(self, 'About Application',
            'The <b>Application</b> example demonstrates how to '
               'write modern GUI applications using Qt, with a menu bar, '
               'toolbars, and a status bar.')

    def buttonClick(self, arg):
        msg = 'Button'
        if self.checkbox.checkState():
            if self.textField.text != '':
                msg = self.textField.text()
        QtWidgets.QMessageBox.information(self,'QMessageBox', msg + ' clicked' + arg)

if __name__ == '__main__':
    # Create the Qt Application
    app = QtWidgets.QApplication(sys.argv)
    # Create and show the form
    form = MainWindow()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())