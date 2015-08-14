class Docker(object):

    def up(self, configObject):
        #self.upWordpress(projectName)
        self.upMySql(projectName)
                
    def upWordpress( self, projectName):
        #--name='"+ self.wordpressName + "'
        command = "docker run -d   --privileged=true  --link "+ self.mysqlName +":mysql  -p "+self.ip+":"+self.port+":"+self.port+" -v "+self.projectFolder+"/vhost:"+self.vhostContainerFolder+":rw -v "+self.projectFolder+"/wordpress:"+self.containerApacheFolder+":rw "+self.wordpressImage+";" 
        print(command)

    def upMySql( self, configObject ):
        #--name='"+self.mysqlName+"'
        command = "docker run -d   -e "
        +configObject.dEnvUsername+
        " -e "
        +configObject.dEnvPassword+
        "  -e "
        +configObject.dEnvDatabase+
        "  -e "
        +configObject.dEnvHost+
        " -p "
        +configObject.dEnvPassword+
        ":"
        +configObject.dEnvPassword+
        ":"
        +configObject.dEnvPassword+
        " -v "
        +configObject.dEnvPassword+
        "/mysql-data/var/lib/mysql:"
        +configObject.dEnvPassword+
        ":rw  "
        +configObject.dEnvPassword+
        ";" 

        print(command)

        #Docker Env's
        self.dWordpressName = "-wordpress"
        self.dMysqlName = "-mysql"
        self.dHost = "127.0.0.2"
        self.dPort = "80"
        self.dWordpressImage = "rtancman/php:php53-apache22"
        self.dMysqlImage = "mysql:5.5"
        self.dProjectFolder = "teste"
        self.dVhostContainerFolder = "/etc/apache2/vhosts"
        self.dMysqlContainerFolder = "/var/lib/mysql"
        self.dApacheContainerFolder = "/var/www/html"
        self.dEnvPassword = 'MYSQL_ROOT_PASSWORD='+self.mPassword
        self.dEnvUsername = 'MYSQL_ROOT_USER='+self.mUsername
        self.dEnvDatabase = 'MYSQL_ROOT_DATABASE='+self.mDatabase
        self.dEnvHost = 'MYSQL_ROOT_HOST='+self.mHost
