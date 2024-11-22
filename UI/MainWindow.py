from PySide6.QtWidgets import QMainWindow, QSplitter, QPlainTextEdit
from PySide6.QtCore import Qt
import pyqtgraph as pg
from Model import Writer
from UI import SourcesListViewer, ListModel

class MainWindow( QMainWindow ):

    def __init__(self, model: ListModel.ListModel ):
        super().__init__()

        self.mainSplitter = QSplitter( )
        self.mainSplitter.setOrientation( Qt.Orientation.Horizontal )
        self.setCentralWidget( self.mainSplitter )

        self.secondSplitter = QSplitter( )
        self.mainSplitter.setOrientation( Qt.Orientation.Vertical )
        self.mainSplitter.addWidget( self.secondSplitter )

        self.logTextView = QPlainTextEdit( )
        self.logTextView.setReadOnly( True )
        self.logTextView.setPlainText( Writer.pargraphs(3) )
        self.mainSplitter.addWidget( self.logTextView )

        self.sourcesList = SourcesListViewer.SourcesListViewer( model )
        self.secondSplitter.addWidget( self.sourcesList )

        self.plot = pg.PlotWidget()
        self.secondSplitter.addWidget( self.plot )