from tools import *

class Wordpress( object ):
    wpSampleConfigFile = "wp-config-sample"
    wpConfigFile = "wp-config"
    wpExtension = "php"
    wp = "wordpress"

    def __init__( self ):
        self.tools = Tools()

    def setConfig(self,projectName):
        content = self.tools.getFileContents(projectName + "/"+self.wp+"/"+self.wpSampleConfigFile + "." +self.wpExtension)
        fileObject = self.tools.createFile( projectName + "/"+self.wp+"/"+self.wpConfigFile, self.wpExtension)
        content = self.setWpConfigVars(content)
        return self.tools.writeInFile(fileObject, content)

    def setWpConfigVars( self, content):
        content = self.tools.patternReplace(".*DB_NAME.*",self.wpVariablePatter('DB_NAME','MYSQL_PORT_3306_TCP_ADDR'),content)
        content = self.tools.patternReplace(".*DB_USER.*",self.wpVariablePatter('DB_USER','MYSQL_PORT_3306_TCP_ADDR'),content)
        content = self.tools.patternReplace(".*DB_PASSWORD.*",self.wpVariablePatter('DB_PASSWORD','MYSQL_PORT_3306_TCP_ADDR'),content)
        return self.tools.patternReplace(".*DB_HOST.*",self.wpVariablePatter('DB_HOST','MYSQL_PORT_3306_TCP_ADDR'),content)

    def wpVariablePatter( self,wpVariableName,variableName ):
        return "define('"+wpVariableName+"', getenv('"+variableName+"));"

