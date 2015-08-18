import os
import glob
import re
import socket
import sys
from ConfigParser import SafeConfigParser, ConfigParser

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
            self.checkListProjectsAll(commands, args)

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

    def getEnableIpOnPort(self, port):
        for i in range(1,255):
            ip = '127.0.0.' + str(i)
            result = self.getIpStatusOnPort(ip, int(port))
            if(result):
                return ip

        return '127.0.0.1'


    def getIpStatusOnPort(self, ip, port):
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        status = soc.connect_ex((ip, port))
        if status == 0:
            return False
        else:
            return True

    def checkKillAll(self, commands, args):
        self.executeFunctionPosition(args,'-killAll', 1, commands, 'killAll')
    
    def checkListProjectsAll(self, commands, args):
        self.executeFunctionPosition(args,'-listProjects', 1, commands, 'listProjects')
    
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

    def openFile(self, fileName):
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

    def setConfigFile(self, projectName):       
        configObject = self.setConfigObject( projectName )
        configFile = open(configObject.confFile, 'a')
        self.configParser.add_section(configObject.confSection)
        self.configParser.set(configObject.confSection, 'name', configObject.pName)
        self.configParser.set(configObject.confSection, 'path', configObject.dWordpressDataPath)
        self.configParser.write(configFile)
        configFile.close()
        
    def getDataFromSection(self,configFile, section, param):
        configParser = ConfigParser() 
        configParser.read( configFile )
        return configParser.get(section, param)

    def getSectionsFromConfigFile(self, configFile):
        configParser = ConfigParser() 
        configParser.read( configFile )
        return configParser._sections.keys()