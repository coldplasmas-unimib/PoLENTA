from PySide6.QtWidgets import QApplication
from UI.MainWindow import MainWindow
from qt_material import apply_stylesheet

app = QApplication()

window = MainWindow()

apply_stylesheet(app, theme='dark_teal.xml')

window.plot.plot( [1,2,3,4,5], [3,2,5,2,1])

window.show()

app.exec()
