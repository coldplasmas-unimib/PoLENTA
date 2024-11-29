from Interfaces import SerialInterface

class Demo( SerialInterface.SerialInterface ):
    
    @staticmethod
    def checkWithoutWriting( port: str ) -> bool:
        return False
    
    @staticmethod
    def checkWithWriting( port: str ) -> bool:
        return True

    def __init__( self, port: str ):
        super().__init__( port )