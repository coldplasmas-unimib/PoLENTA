from abc import ABC, abstractmethod

class SerialInterface( ABC ):

    @staticmethod
    @abstractmethod
    def checkWithoutWriting( port: str ) -> bool:
        pass
    
    @staticmethod
    @abstractmethod
    def checkWithWriting( port: str ) -> bool:
        pass

    @abstractmethod
    def __init__( self, port: str ):
        self.port = port