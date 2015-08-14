from wordpress import *
from tools import *
from vhost import *

class Commands( object ):
    filesPath = 'files/'
    pathBdBase = filesPath+'baseDatabase/'
    pathWordpressBase = filesPath+'baseWordpress/'
    pathVhostBase = filesPath+'baseVhost/'

    def __init__( self ):
        self.wordpress = Wordpress()
        self.tools = Tools()
        self.vhost = Vhost()

    def creatProject(self, projectName):        
        self.tools.createFolder(projectName)
        self.tools.descompressZip( self.pathWordpressBase, projectName )
        self.tools.descompressTarGz( self.pathBdBase, projectName )
        self.wordpress.setConfig( projectName )
        self.vhost.set(projectName, self.pathVhostBase )

        
        