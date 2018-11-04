import sys
from PySide import QtGui
from PySide import QtCore

class Basic_UI(QtGui.QMainWindow):

    def __init__(self):
        super(Basic_UI, self).__init__()
        
        # Init Layout
        self.layout = QtGui.QVBoxLayout()

        # Label
        self.label = QtGui.QLabel('Basic UI')
        self.layout.addWidget(self.label)

        # Exit Button
        self.exit_action = QtGui.QAction('Exit', self)
        self.exit_action.setShortcut('Ctrl+Q')
        self.exit_action.setStatusTip('Exit application')
        self.exit_action.triggered.connect(self.close_window)

        # Create Menu Bar
        self.menubar = self.menuBar()
        # Add File Menu
        self.file_menu = self.menubar.addMenu('File')
        # Add Exit Button
        self.file_menu.addAction(self.exit_action)
        
        # Set Central Widget (can only be one)
        self.setCentralWidget(self.label)

        # Set layout
        self.setWindowTitle('Basic_UI')
        self.setLayout(self.layout)

        self.statusBar().showMessage('Ready')
        
    def close_window(self):
        self.close()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main_window = Basic_UI()
    main_window.show()
    sys.exit(app.exec_())