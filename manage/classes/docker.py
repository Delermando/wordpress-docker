class Docker(object):

    def up(self, configObject):
        self.upWordpress(configObject)
        self.upMySql(configObject)
                
    def upWordpress( self, configObject):
        var = (
            configObject.dWordpressContainerName,
            configObject.dWMysqlContainerName,
            configObject.dHost,
            configObject.dApachePort,
            configObject.dApachePort,
            configObject.dVhostDataPath,
            configObject.dVhostContainerFolder, 
            configObject.dWordpressDataPath,
            configObject.dApacheContainerFolder,
            configObject.dWordpressImage
        )
        print("docker run -d --privileged=true --name='%s' --link %s:mysql -p %s:%s:%s -v %s:%s:rw -v %s:%s:rw %s; " % var)

    def upMySql( self, configObject ):
        var = (
            configObject.dWMysqlContainerName,
            configObject.dEnvUsername, 
            configObject.dEnvPassword, 
            configObject.dEnvDatabase, 
            configObject.dEnvHost, 
            configObject.dHost, 
            configObject.dMysqlPort, 
            configObject.dMysqlPort, 
            configObject.dMysqlDataPath, 
            configObject.dMysqlContainerFolder, 
            configObject.dMysqlImage 
        )
        print("docker run -d --name='%s' -e %s -e %s -e %s -e %s -p %s:%s:%s  -v %s:%s:rw %s;" % var)

