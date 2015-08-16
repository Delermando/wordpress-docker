import os
import glob
import re

class Tools( object ):

    def executeFunctionFromClass(self, classe, functionName ):
        getattr(classe, functionName)()

    def cli(self, commands, args ):
            self.checkCreateProjectParam( commands, args )
            self.checkUpParam( commands, args )
            self.checkKillAll( commands, args )
            self.checkRmAll( commands, args )
            self.checkShowll( commands, args )
            self.checkDeleteAllProjects(args)

    def delete(self, path):
        self.executeSystemCommand("rm -r " + path)

    def deleteAllProjects(self):
        self.delete("projects/")

    def checkDeleteAllProjects(self, args):
        self.executeFunctionPosition(args,'-deleteAllProjects', 1, self, 'deleteAllProjects')

    def checkParamPosition(self,args, param, position):
        if( len(args) == position + 2 and args[position] == param  and args[position + 1] != ''):
            return True
        else:
            return False

    def checkKillAll(self, commands, args):
        self.executeFunctionPosition(args,'-killAll', 1, commands, 'killAll')
    
    def checkRmAll(self, commands, args):
        self.executeFunctionPosition(args,'-rmAll', 1, commands, 'rmAll')    

    def checkShowll(self, commands, args):
        self.executeFunctionPosition(args,'-showAll', 1, commands, 'showAll')

    def checkUpParam( self, commands, args  ):
        if( self.checkParamPosition(args, '-up', 1) ):
            commands.up( args[2] )

    def checkCreateProjectParam( self, commands, args ):
        if( self.checkParamPosition(args, '-createProject', 1) ):
            commands.createProject( args[2] )

    def executeFunctionPosition( self,  args, param, position , classe, functionName):
        if( len(args) >= position + 1 and args[ position ] == param):
            self.executeFunctionFromClass(classe, functionName)
        return False

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
        return self.executeSystemCommand('clear')

    def currentFolder(self):
        return os.getcwd()+"/"
