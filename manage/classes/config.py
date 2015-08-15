from tools import *

class Config(object):
    
    def __init__( self, projectName ):
        self.tools = Tools()
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
        self.hFolderName = "vhosts/"
        self.hFolderPath = self.pPath + self.hFolderName
        self.hFileName = "host"
        self.hFileExtension = ".conf"
        self.hCategory = ".com.br"
        self.hFile = self.pPath + self.hFolderName+self.hFileName+self.hFileExtension
        self.hHost = self.pName+self.hCategory

        #MySql Env's
        self.mPassword = 'root'
        self.mUsername = 'root'
        self.mDatabase = 'wordpress'
        self.mHost = '127.0.0.1'        
        self.mDataFolder = 'mysql-data/var'        
        

        #Docker Env's
        self.dWordpressDataPath =  self.tools.currentFolder() + self.pPath + self.wPath
        self.dMysqlDataPath =  self.tools.currentFolder() + self.pPath+self.mDataFolder
        self.dVhostDataPath =  self.tools.currentFolder() + self.pPath+self.hFolderName
        self.dWordpressName = "-wordpress"
        self.dMysqlName = "-mysql"
        self.dHost = "127.0.0.3"
        self.dApachePort = "80"
        self.dMysqlPort = "3306"
        self.dWordpressImage = "rtancman/php:php53-apache22"
        self.dWordpressContainerName = self.pName+"-"+self.dWordpressName
        self.dWMysqlContainerName = self.pName+"-"+self.dMysqlName
        self.dMysqlImage = "mysql:5.5"
        self.dProjectFolder = "teste"
        self.dVhostContainerFolder = "/etc/apache2/vhosts"
        self.dMysqlContainerFolder = "/var/lib/mysql"
        self.dApacheContainerFolder = "/var/www/html"
        self.dEnvPassword = 'MYSQL_ROOT_PASSWORD='+self.mPassword
        self.dEnvUsername = 'MYSQL_ROOT_USER='+self.mUsername
        self.dEnvDatabase = 'MYSQL_ROOT_DATABASE='+self.mDatabase
        self.dEnvHost = 'MYSQL_ROOT_HOST='+self.mHost
