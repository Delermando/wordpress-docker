class Docker(object):
    
    def dockerUp(self):
        self.executeSystemCommand('docker run -d  --name="mysql55-wordpress2"  -e MYSQL_ROOT_PASSWORD=root -p 127.0.0.2:3306:3306    -v `pwd`/mysql-data/var/lib/mysql:/var/lib/mysql:rw  mysql:5.5;')