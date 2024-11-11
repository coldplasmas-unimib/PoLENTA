from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from qt_material import apply_stylesheet


app = QApplication()

ui_file = QFile("UI/mainWindow.ui")
ui_file.open(QFile.ReadOnly)

loader = QUiLoader()
window = loader.load(ui_file)

apply_stylesheet(app, theme='dark_teal.xml')

window.show()

app.exec()
