from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QSplitter, QPlainTextEdit
import pyqtgraph as pg
import lorem

class MainWindow( QMainWindow ):

    def __init__(self):
        super().__init__()

        self.mainSplitter = QSplitter( )
        self.mainSplitter.setOrientation( QSplitter.Orientation.Horizontal )
        self.setCentralWidget( self.mainSplitter )

        self.secondSplitter = QSplitter( )
        self.mainSplitter.setORientation( QSplitter.Orientation.Vertical )
        self.mainSplitter.addWidget( self.secondSplitter )

        self.logTextView = QPlainTextEdit( )
        self.logTextView.setReadOnly( True )
        self.logTextView.setPlainText( lorem.paragraphs(5) )
        self.mainSplitter.addWidget( self.logTextView )

        self.sideTextView = QPlainTextEdit( )
        self.sideTextView.setReadOnly( True )
        self.sideTextView.setPlainText( lorem.paragraphs(1) )
        self.secondSplitter.addWidget( self.sideTextView )

        self.plot = pg.PlotWidget()
        self.secondSplitter.addWidget( self.plot )


# from PySide6.QtWidgets import QVBoxLayout
# import pyqtgraph as pg

# uiclass, baseclass = pg.Qt.loadUiType("UI/mainWindow.ui")

# class MainWindow(uiclass, baseclass):

#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)

#         plotNEholder: QVBoxLayout = self.plotNEholder
#         plotNEholder.hasHeightForWidth = lambda:True
#         plotNEholder.heightForWidth = lambda x: x * 2 / 3
#         plotNEholder.hasWidthForHeight = lambda:True
#         plotNEholder.widthForHeight = lambda x: x * 3 / 2

#     def plotNE(self, xs, ys ):
#         self.plotNEwidget.plot( xs, ys )
