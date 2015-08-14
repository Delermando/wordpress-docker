class Docker(object):

    # wordpressName = "-wordpress"
    # mysqlName = "-mysql"
    # ip = "127.0.0.2"
    # port = "80"
    # wordpressImage = "rtancman/php:php53-apache22"
    # mysqlImage = "mysql:5.5"
    # projectFolder = "teste"
    # vhostContainerFolder = "/etc/apache2/vhosts"
    # mysqlContainerFolder = "/var/lib/mysql"
    # containerApacheFolder = "/var/www/html"

    # mysqlPass = 'MYSQL_ROOT_PASSWORD=root'
    # mysqlUser = 'MYSQL_ROOT_USER=root'
    # mysqlDb = 'MYSQL_ROOT_DATABASE=wordpress'
    # mysqlHost = 'MYSQL_ROOT_HOST=127.0.0.1'

    def up(self, projectName):
        self.upWordpress(projectName)
        self.upMySql(projectName)
        
        
    
    def upWordpress( self, projectName):
        #--name='"+ self.wordpressName + "'
        command = "docker run -d   --privileged=true  --link "+ self.mysqlName +":mysql  -p "+self.ip+":"+self.port+":"+self.port+" -v "+self.projectFolder+"/vhost:"+self.vhostContainerFolder+":rw -v "+self.projectFolder+"/wordpress:"+self.containerApacheFolder+":rw "+self.wordpressImage+";" 
        print(command)

    def upMySql( self, projectName ):
        #--name='"+self.mysqlName+"'
        command = "docker run -d   -e "+self.mysqlPass+" -e "+self.mysqlUser+"  -e "+self.mysqlDb+"  -e "+self.mysqlHost+" -p "+self.ip+":"+self.port+":"+self.port+" -v "+self.projectFolder+"/mysql-data/var/lib/mysql:"+self.mysqlContainerFolder+":rw  "+self.mysqlImage+";" 
        print(command)


    