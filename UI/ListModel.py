from PySide6.QtCore import QAbstractListModel, Qt

class ListModel(QAbstractListModel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.list = [ 'uno', 'due', 'tre' ]

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.list[index.row()]

    def rowCount(self, index):
        return len(self.list)