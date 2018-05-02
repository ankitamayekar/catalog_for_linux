# catalog_for_linux
Get your server.
1. Start a new Ubuntu Linux server instance on Amazon Lightsail. There are full details on setting up your Lightsail instance on the next page.
2. Follow the instructions provided to SSH into your server.

Secure your server.
3. Update all currently installed packages.
	sudo apt-get update
	sudo apt-get upgrade
	
4. Change the SSH port from 22 to 2200. Make sure to configure the Lightsail firewall to allow it.
	sudo nano /etc/ssh/sshd_config
		change the port from 22 to 2200
	sudo service ssh restart
	
4.1. Here after use Putty to connect with following configuration:
	IP: IP of your server
	PORT: 2200
	Connection>SSH>Auth : .ppk file i.e. private key file.
	
5. Configure the Uncomplicated Firewall (UFW) to only allow incoming connections for SSH (port 2200), HTTP (port 80), and NTP (port 123).
	sudo ufw default deny incoming
	sudo ufw default allow outgoing
	sudo ufw allow ssh
	sudo ufw allow 2200/tcp
	sudo ufw allow 80/tcp
	sudo ufw allow 123/udp
	sudo ufw enable

Give grader access.
In order for your project to be reviewed, the grader needs to be able to log in to your server.

6. Create a new user account named grader.
	sudo adduser grader
	
7. Give grader the permission to sudo.
	sudo nano /etc/sudoers.d/grader
	type in :
			grader ALL=(ALL:ALL) ALL

8. Create an SSH key pair for grader using the ssh-keygen tool.
	su - grader
	mkdir .ssh
	touch .ssh/authorized_keys 
	nano .ssh/authorized_keys 
	Paste the public key from local machine here.
	chmod 700 .ssh
	chmod 644 .ssh/authorized_keys
	
	reload ssh 
		service ssh restart
	
	ssh -i [private keyname] grader@34.216.153.142
	
Prepare to deploy your project.
9. Configure the local timezone to UTC.

	sudo dpkg-reconfigure tzdata
		choose UTC

10. Install and configure Apache to serve a Python mod_wsgi application.

	sudo apt-get install apache2
	sudo apt-get install python-setuptools libapache2-mod-wsgi
	sudo service apache2 restart	

11. Install and configure PostgreSQL:
	
	sudo apt-get install postgresql
	sudo nano /etc/postgresql/9.5/main/pg_hba.conf
		no remote connections are allowed
	sudo su - postgres
		login as user "postgres"
	
	psql
		start postgresSQL
		
		postgres=# CREATE DATABASE catalog;
			creating new db named catalog
		postgres=# CREATE USER catalog WITH PASSWORD 'password';

Do not allow remote connections
Create a new database user named catalog that has limited permissions to your catalog application database.

12. Install git.
	sudo apt-get install git

Deploy the Item Catalog project.
13. Clone and setup your Item Catalog project from the Github repository you created earlier in this Nanodegree program.
	go to dir /var/www
		cd /var/www
	make directory Catalog
		sudo mkdir Catalog
		cd Catalog
	clone the catalog from github to the virtual machine
		git clone https://github.com/ankitamayekar/catalog_for_linux.git
		
		installing pip
			sudo apt-get install python-pip
			sudo pip install --upgrade
			sudo apt-get install python-sqlalchemy
			sudo apt-get install python-flask
			sudo apt-get -qqy install postgresql python-psycopg2
			
	create database.
		python db.py
		python data.py
		python finalproject.py
			


14. Set it up in your server so that it functions correctly when visiting your server’s IP address in a browser. Make sure that your .git directory is not publicly accessible via a browser!
