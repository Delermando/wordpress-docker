from tools import *

class Commands( object ):
    filesPath = 'files/'
    pathBdBase = filesPath+'baseDatabase/'
    pathWordpressBase = filesPath+'baseWordpress/'
    pathVhostBase = filesPath+'baseVhost/'

    def __init__( self ):
        self.tools = Tools()

    def startProject(self, projectName):        
        self.tools.getVhostContent( self.pathVhostBase)
        self.tools.descompressZip(  self.pathWordpressBase, projectName )
        self.tools.descompressTarGz( self.pathBdBase, projectName )
        self.tools.setVhost(projectName, self.pathVhostBase)
        self.tools.setWordpressConfig(projectName)
        