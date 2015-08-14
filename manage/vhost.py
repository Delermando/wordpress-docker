from tools import *

class Vhost(object):
    hostFolderName = "vhost/"
    hostFileName = "host"
    hostFileExtension = "conf"
    hostType = ".com.br"


    def __init__(self):
        self.tools = Tools()

    def set(self, projectName, path ):
        self.tools.createFolder(projectName +"/"+ self.hostFolderName)
        fileObject = self.tools.createFile( projectName + "/" + self.hostFolderName + self.hostFileName, self.hostFileExtension )
        content = self.replaceHostName(projectName, self.getContent(path))
        self.tools.writeInFile(fileObject, content)
    
    def printHostMessage(self,host):
        self.tools.clearScreen()
        print("Acesse --> "+host)

    def getContent( self, path ):
        path = self.tools.listFiles( path )
        return self.tools.getFileContents(path[0])

    def replaceHostName(self, hostName, content):
        return content.replace("example", hostName + self.hostType)