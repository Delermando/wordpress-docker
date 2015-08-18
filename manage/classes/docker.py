from tools import *

class Docker(object):

    def __init__(self):
        self.tools = Tools()

    def up(self, configObject):
        self.tools.executeSystemCommand(self.upMySql( configObject ))
        self.tools.executeSystemCommand(self.upWordpress( configObject ))
    
    def killAll(self):
        self.tools.executeSystemCommand("docker kill $(docker ps -a -q)")

    def rmAll(self):
        self.tools.executeSystemCommand("docker rm $(docker ps -a -q)")    

    def showAll(self):
        self.tools.executeSystemCommand("docker ps -a")

    def upWordpress( self, configObject):

        var = (
            configObject.dWordpressContainerName,
            configObject.dWMysqlContainerName,
            configObject.dEnvUsername, 
            configObject.dEnvPassword, 
            configObject.dEnvDatabase, 
            configObject.dEnvHost, 
            self.tools.getEnableIpOnPort(80),
            #configObject.dHost,
            configObject.dApachePort,
            configObject.dApachePort,
            configObject.dVhostDataPath,
            configObject.dVhostContainerFolder, 
            configObject.dWordpressDataPath,
            configObject.dApacheContainerFolder,
            configObject.dWordpressImage
        )
        return "docker run -d --privileged=true --name='%s' --link %s:mysql -e %s -e %s -e %s -e %s  -p %s:%s:%s -v %s:%s:rw -v %s:%s:rw %s; " % var

    def upMySql( self, configObject ):
        var = (
            configObject.dWMysqlContainerName,
            #configObject.dHost, 
            self.tools.getEnableIpOnPort(3306),
            configObject.dMysqlPort, 
            configObject.dMysqlPort, 
            configObject.dMysqlDataPath, 
            configObject.dMysqlContainerFolder, 
            configObject.dMysqlImage 
        )
        return "docker run -d --name='%s'  -e MYSQL_ROOT_PASSWORD=root -p %s:%s:%s  -v %s:%s:rw %s;" % var

