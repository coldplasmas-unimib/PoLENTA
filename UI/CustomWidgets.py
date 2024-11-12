from PySide6.QtWidgets import QBoxLayout, QWidget
from pyqtgraph import PlotWidget


class FixedAspectRatioWidget(QBoxLayout):

    def __init__(self, parent: QWidget | None = ...) -> None:
        super().__init__( QBoxLayout.Direction.TopToBottom, parent)

    def pollo(self):
        return "pollame"

    # def hasHeightForWidth(self) -> True:
    #     return True
