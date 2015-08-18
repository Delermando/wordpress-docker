from wordpress import *
from mysql import *
from tools import *
from vhost import *
from docker import *
from config import *

class Commands( object ):
    
    def __init__( self ):
        self.wordpress = Wordpress()
        self.mysql = MySql()
        self.tools = Tools()
        self.vhost = Vhost()
        self.docker = Docker()
        self.configParser = ConfigParser() 

    def setConfigObject( self, projectName ):
        return Config( projectName )

    def initCli(self, args):
        self.tools.cli(self, args)

    def createProject(self, projectName):        
        #self.tools.getEnableIpOnPort(3306)
        configObject = self.setConfigObject( projectName )
        self.setConfigFile(projectName)
        self.wordpress.createFolder(configObject)
        self.mysql.descompress( configObject )
        self.wordpress.descompress( configObject )
        self.wordpress.setConfig( configObject )
        self.vhost.set( configObject )

    def up( self, projectName ):
        configObject = self.setConfigObject( projectName )
        self.docker.up( configObject )

    def killAll(self):
        self.docker.killAll()

    def rmAll(self):
        self.docker.rmAll()

    def showAll(self):
        self.docker.showAll()

    def deleteAllProject(self):
        self.checkDeleteAllProjects()

    def setConfigFile(self, projectName):       
        configObject = self.setConfigObject( projectName )
        configFile = open(configObject.confFile, 'a')
        self.configParser.add_section(configObject.confSection)
        self.configParser.set(configObject.confSection, 'name', configObject.pName)
        self.configParser.set(configObject.confSection, 'ip', configObject.dHost)
        self.configParser.write(configFile)
        configFile.close()
        
    def getDataFromFromSection(self,projectName, section, param):
        configObject = self.setConfigObject( projectName )
        self.configParser.read(configObject.confFile)
        return self.configParser.get(section, param)

    def getSectionFromConfigFile(self):
        self.configParser.read('config.ini')
        return self.configParser._sections.keys()

    def getProjectsName(self):
        self.configParser.read('config.ini')
        configSections = self.getSectionFromConfigFile()
        return map( lambda elem: self.configParser.get(elem,'name'), configSections ) 

        