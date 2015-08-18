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

    def listProjects(self):
        configSections = self.tools.getSectionsFromConfigFile('config.ini')
        print( map( lambda elem: self.tools.getDataFromSection('config.ini', elem, 'name'), configSections ) )

        