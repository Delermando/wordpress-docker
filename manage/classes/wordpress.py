from tools import *

class Wordpress( object ):
    
    def __init__( self ):
        self.tools = Tools()

    def setConfig(self,configObject):
        content = self.tools.getFileContents( configObject.wSampleConfigFile )
        fileObject = self.tools.openFile( configObject.wConfigFile )
        content = self.setWpConfigVars(content)
        return self.tools.writeInFile(fileObject, content)

    def setWpConfigVars( self, content):
        content = self.tools.patternReplace(".*DB_NAME.*",self.wpVariablePatter('DB_NAME','MYSQL_ROOT_DATABASE'),content)
        content = self.tools.patternReplace(".*DB_USER.*",self.wpVariablePatter('DB_USER','MYSQL_ROOT_USER'),content)
        content = self.tools.patternReplace(".*DB_PASSWORD.*",self.wpVariablePatter('DB_PASSWORD','MYSQL_ROOT_PASSWORD'),content)
        return self.tools.patternReplace(".*DB_HOST.*",self.wpVariablePatter('DB_HOST','MYSQL_PORT_3306_TCP_ADDR'),content)

    def wpVariablePatter( self,wpVariableName,variableName ):
        return "define('"+wpVariableName+"', getenv('"+variableName+"'));"

    def descompress( self, configObject):
        print(configObject.pPathWordpress)
        self.tools.descompressZip( configObject.pPathWordpress, configObject.pPath)

    def createFolder(self, configObject):
        self.tools.createFolder( configObject.pPath )