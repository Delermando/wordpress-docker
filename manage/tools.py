import os
import glob
import re

class Tools( object ):
    hostFolderName = "vhost/"
    hostFileName = "host"
    hostFileExtension = "conf"
    hostType = ".com.br"
    wpSampleConfigFile = "wp-config-sample"
    wpConfigFile = "wp-config"
    wpExtension = "php"
    wp = "wordpress"


    def setWordpressConfig(self,projectName):
        content = self.getFileContents(projectName + "/"+self.wp+"/"+self.wpSampleConfigFile + "." +self.wpExtension)
        fileObject = self.createFile( projectName + "/"+self.wp+"/"+self.wpConfigFile, self.wpExtension)
        content = self.setWpConfigVars(content)
        return self.writeInFile(fileObject, content)

    def patternReplace(self, pattern, string, content):
        return re.sub( pattern, string, content )

    def setWpConfigVars( self, content):
        content = self.patternReplace(".*DB_NAME.*",self.wpVariablePatter('DB_NAME','MYSQL_PORT_3306_TCP_ADDR'),content)
        content = self.patternReplace(".*DB_USER.*",self.wpVariablePatter('DB_USER','MYSQL_PORT_3306_TCP_ADDR'),content)
        content = self.patternReplace(".*DB_PASSWORD.*",self.wpVariablePatter('DB_PASSWORD','MYSQL_PORT_3306_TCP_ADDR'),content)
        return self.patternReplace(".*DB_HOST.*",self.wpVariablePatter('DB_HOST','MYSQL_PORT_3306_TCP_ADDR'),content)

    def wpVariablePatter( self,wpVariableName,variableName ):
        return "define('"+wpVariableName+"', getenv('"+variableName+"));"

    def createFolder( self, name ):
        self.executeSystemCommand('mkdir -p ' + name)

    def executeSystemCommand(self, command):
        return os.system( command )

    def descompressZip(self, filePath, projectPath ):
        path = self.listFiles( filePath )
        self.executeSystemCommand('unzip ' + path[0] + ' -d '+ projectPath) 

    def descompressTarGz(self, filePath, projectPath ):
        path = self.listFiles( filePath )
        self.executeSystemCommand('tar -xvf ' + path[0] + ' -C '+ projectPath)        
    
    def setVhost(self, projectName, path ):
        self.createFolder(projectName +"/"+ self.hostFolderName)
        fileObject = self.createFile( projectName + "/" + self.hostFolderName + self.hostFileName, self.hostFileExtension )
        content = self.replaceHostName(projectName, self.getVhostContent(path))
        self.writeInFile(fileObject, content)

    def createFile(self, fileName, extension):
        return open(fileName+"."+extension, "wb")

    def writeInFile(self, fileObject, content):
        return fileObject.write( content)

    def getVhostContent( self, path ):
        path = self.listFiles( path )
        return self.getFileContents(path[0])

    def replaceHostName(self, hostName, content):
        return content.replace("example", hostName + self.hostType)

    def getFileContents(self, path ):
        if os.path.exists( path ):
            fp = open( path , "r")
            content = fp.read()
            fp.close()
            return content
        else:
            return ''

    def listFiles( self, path):
        return glob.glob(path + '*')

    def clearScreen(self):
        self.executeSystemCommand('clear')

    def printHostMessage(self,host):
        self.clearScreen()
        print("Acesse --> "+host)

        