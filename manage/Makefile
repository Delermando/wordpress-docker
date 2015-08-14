up:
	docker run -d  --name="mysql55-wordpress2"  -e MYSQL_ROOT_PASSWORD=root -p 127.0.0.2:3306:3306    -v `pwd`/mysql-data/var/lib/mysql:/var/lib/mysql:rw  mysql:5.5;
	docker run -d   --privileged=true --name="wordpress2" --link mysql55-wordpress2:mysql  -p 127.0.0.2:80:80 -v `pwd`/vhosts:/etc/apache2/vhosts:rw    -v `pwd`/wordpress:/var/www/html:rw rtancman/php:php53-apache22;

down:
	docker rm wordpress mysql55-wordpress;

downAll:
	docker rm `docker ps -a -q`

kill:
	docker kill wordpress mysql55-wordpress;

killAll:
	docker kill `docker ps -a -q`;

restart:
	docker restart mysql55-wordpress wordpress ;

mysqlIp:
	docker exec -it wordpress env | grep MYSQL_PORT_3306_TCP_ADDR |sed 's,MYSQL_PORT_3306_TCP_ADDR=,,'

status:
	docker ps -a;

connectMySql:
	docker exec -it mysql55-wordpress bash;

connectWordpress:
	docker exec -it wordpress bash;

setHost:
	echo "0.0.0.0 local.workcopy.com.br" >> /etc/hosts

setConfig:
	mv wordpress/wp-config-sample.php wordpress/wp-config.php
	sed -i -e "s,.*DB_HOST.*,define('DB_HOST' \, getenv('MYSQL_PORT_3306_TCP_ADDR'));  ," wordpress/wp-config.php
	sed -i -e "s,.*DB_NAME.*, define('DB_NAME' \, 'wordpress'); ," wordpress/wp-config.php
	sed -i -e "s,.*DB_USER.*, define('DB_USER' \, 'root'); ," wordpress/wp-config.php
	sed -i -e "s,.*DB_PASSWORD.*, define('DB_PASSWORD' \, 'root'); ," wordpress/wp-config.php

descompressMySql:
	tar -xvf mysql-data.tar.gz
descompressWordpress:
	unzip `ls | grep .*wordpres.*zip`  -d `pwd`

manage:
	python manage.py