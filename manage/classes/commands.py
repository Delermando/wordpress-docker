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

    def creatProject(self, projectName):        
        configObject = self.setConfigObject( projectName )
        #self.docker.up(projectName)
        #self.wordpress.createFolder(configObject)
        #self.mysql.descompress( configObject )
        #self.wordpress.descompress( configObject )
        #self.wordpress.setConfig( configObject )
        #self.vhost.set( configObject )

        
    def setConfigObject( self, projectName ):
        return Config( projectName )