from PySide6.QtWidgets import QListView
from UI import ListModel

class SourcesListViewer( QListView ):

    def __init__(self, model: ListModel.ListModel, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setModel( model )