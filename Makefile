up:
	docker run -d  --name="mysql55-wordpress"  -e MYSQL_ROOT_PASSWORD=root -p 3306:3306    -v `pwd`/mysql-data/var/lib/mysql:/var/lib/mysql:rw  mysql:5.5;
	docker run -d   --privileged=true --name="wordpress" --link mysql55-wordpress:mysql  -p 80:80  -v `pwd`/vhosts:/etc/apache2/vhosts:rw    -v `pwd`:/var/www/html:rw rtancman/php:php53-apache22;

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
	docker exec -it wordpress env | grep MYSQL_PORT_3306_TCP_ADDR;

status:
	docker ps -a;

connectMySql:
	docker exec -it mysql55-wordpress bash;

connectWordpress:
	docker exec -it wordpress bash;

setHost:
	echo "0.0.0.0 local.workcopy.com.br" >> /etc/hosts

setMySqlEnv:
	sed -i -e "s,.*DB_HOST.*,define('DB_HOST' \, getenv('MYSQL_PORT_3306_TCP_ADDR'));  ," wp-config.php