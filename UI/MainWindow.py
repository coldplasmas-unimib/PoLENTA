from PySide6.QtWidgets import QVBoxLayout
import pyqtgraph as pg

uiclass, baseclass = pg.Qt.loadUiType("UI/mainWindow.ui")

class MainWindow(uiclass, baseclass):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        plotNEholder: QVBoxLayout = self.plotNEholder
        plotNEholder.hasHeightForWidth = lambda:True
        plotNEholder.heightForWidth = lambda x: x * 2 / 3
        plotNEholder.hasWidthForHeight = lambda:True
        plotNEholder.widthForHeight = lambda x: x * 3 / 2

    def plotNE(self, xs, ys ):
        self.plotNEwidget.plot( xs, ys )
