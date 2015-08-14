from tools import *

class MySql():
    def __init__( self ):
        self.tools = Tools()

    def descompress( self, configObject ):
        print(configObject.pPathBatabase)
        self.tools.descompressTarGz( configObject.pPathBatabase, configObject.pPath)