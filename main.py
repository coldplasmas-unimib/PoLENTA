from PySide6.QtWidgets import QApplication
from UI.MainWindow import MainWindow
from qt_material import apply_stylesheet
from UI import ListModel

# app = QApplication()

# listModel = ListModel.ListModel()

# window = MainWindow( listModel )

# apply_stylesheet(app, theme='dark_teal.xml')

# window.plot.plot( [1,2,3,4,5], [3,2,5,2,1])

# window.show()

# app.exec()

from Interfaces import SerialInterfacesList

for cl in SerialInterfacesList.thelist:
    print(cl.checkWithoutWriting('COM3'))
for cl in SerialInterfacesList.thelist:
    print(cl.checkWithWriting('COM3'))
for cl in SerialInterfacesList.thelist:
    print(cl('COM3'))
