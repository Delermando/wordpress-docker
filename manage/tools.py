import os
import glob
import re

class Tools( object ):

    def patternReplace(self, pattern, string, content):
        return re.sub( pattern, string, content )

    def createFolder( self, folderName ):
        self.executeSystemCommand('mkdir -p ' + folderName)

    def executeSystemCommand(self, command):
        return os.system( command )

    def descompressZip(self, filePath, projectPath ):
        path = self.listFiles( filePath )
        self.executeSystemCommand('unzip ' + path[0] + ' -d '+ projectPath) 

    def descompressTarGz(self, filePath, projectPath ):
        path = self.listFiles( filePath )
        self.executeSystemCommand('tar -xvf ' + path[0] + ' -C '+ projectPath)        
    

    def createFile(self, fileName):
        return open(fileName, "wb")

    def writeInFile(self, fileObject, content):
        return fileObject.write( content)

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

    def currentFolder(self):
        return self.executeSystemCommand('pwd')
