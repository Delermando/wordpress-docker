class Config(object):
    
    def __init__( self, projectName ):
        #Project Env
        self.pMangeFolder = "manage/"
        self.pProjectsFolder = "projects/"
        self.pClassesFolder = "classes/"
        self.pName = projectName
        self.pPath = self.pProjectsFolder + self.pName+"/"
        self.pFilesFolder = 'files/'
        self.pPathBatabase = self.pMangeFolder + self.pFilesFolder+'baseDatabase/'
        self.pPathWordpress = self.pMangeFolder + self.pFilesFolder+'baseWordpress/'
        self.pPathVhost = self.pMangeFolder + self.pFilesFolder+'baseVhost/'

        #Wordpress Env's
        self.wName = "wordpress"
        self.wPath = "wordpress/"
        self.wSampleConfigFileName = "wp-config-sample"
        self.wConfigFileName = "wp-config"
        self.wExtension = ".php"
        self.wConfigFile = self.pPath + self.wPath + self.wConfigFileName + self.wExtension
        self.wSampleConfigFile = self.pPath + self.wPath + self.wSampleConfigFileName + self.wExtension
        

        #Vhost Env's
        self.hFolderName = "vhost/"
        self.hFolderPath = self.pPath + self.hFolderName
        self.hFileName = "host"
        self.hFileExtension = ".conf"
        self.hCategory = ".com.br"
        self.hFile = self.pPath + self.hFolderName+self.hFileName+self.hFileExtension
        self.hHost = self.pName+self.hCategory

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

        #MySql Env's
        self.mEnvPasswordName = 'MYSQL_ROOT_PASSWORD=root'
        self.mEnvUserName = 'MYSQL_ROOT_USER=root'
        self.mEnvDatabaseName = 'MYSQL_ROOT_DATABASE=wordpress'
        self.mEnvHostName = 'MYSQL_ROOT_HOST=127.0.0.1'