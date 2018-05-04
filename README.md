# Linux Server Configuration
Get your server.
## 1. Start a new Ubuntu Linux server instance on Amazon Lightsail. There are full details on setting up your Lightsail instance on the next page.
	click create an instance
		select platform - linux/Unix
		select a blueprint - OS only -> Ubuntu
			Change the SSH key pair 
		Name your instance 
		click Create
		
## 2. Follow the instructions provided to SSH into your server.

Secure your server.
## 3. Update all currently installed packages.
	sudo apt-get update
	sudo apt-get upgrade
	
## 4. Change the SSH port from 22 to 2200. Make sure to configure the Lightsail firewall to allow it.
	sudo nano /etc/ssh/sshd_config
		change the port from 22 to 2200
	sudo service ssh restart
	
	4.1. Here after use Putty to connect with following configuration:
	IP: IP of your server
	PORT: 2200
	Connection>SSH>Auth : .ppk file i.e. private key file.
	
## 5. Configure the Uncomplicated Firewall (UFW) to only allow incoming connections for SSH (port 2200), HTTP (port 80), and NTP (port 123).
	sudo ufw default deny incoming
	sudo ufw default allow outgoing
	sudo ufw allow ssh
	sudo ufw allow 2200/tcp
	sudo ufw allow 80/tcp
	sudo ufw allow 123/udp
	sudo ufw enable
	sudo ufw status (check if active)

### Give grader access.
In order for your project to be reviewed, the grader needs to be able to log in to your server.

## 6. Create a new user account named grader.
	sudo adduser grader
	
## 7. Give grader the permission to sudo.
	sudo nano /etc/sudoers.d/grader
	type in :
			grader ALL=(ALL:ALL) ALL

## 8. Create an SSH key pair for grader using the ssh-keygen tool.
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
## 9. Configure the local timezone to UTC.

	sudo dpkg-reconfigure tzdata
		choose UTC

## 10. Install and configure Apache to serve a Python mod_wsgi application.
	
	Install Apache using your package manager with the following command
		sudo apt-get install apache2
	
	To install mod_wsgi
		sudo apt-get install python-setuptools libapache2-mod-wsgi
	
	Restart Apache with
		sudo service apache2 restart	

## 11. Install and configure PostgreSQL:
	
	Install PostgreSQL to server your data using the command
	sudo apt-get install postgresql
	
	To check for no remote connections:
		sudo nano /etc/postgresql/9.5/main/pg_hba.conf
	
	Login as user 'postgres'
		sudo su - postgres
	
	Start postgresSQL shell
		psql
		
			creating new db named catalog
				# CREATE DATABASE catalog;
			
			Create new user named 'catalog' and pasword 'password'
				# CREATE USER catalog WITH PASSWORD 'password';
			
			granting permisions to user 'catalog' on application database 'catalog'
				# GRANT ALL PRIVILEGES ON DATABASE catalog TO catalog;
		# \q
	exit
## 12. Install git.
	sudo apt-get install git

Deploy the Item Catalog project.
## 13. Clone and setup your Item Catalog project from the Github repository you created earlier in this Nanodegree program.
	go to dir /var/www
		cd /var/www
	make directory FlaskApp
		sudo mkdir FlaskApp
		cd FlaskApp
	
	clone the catalog_for_linux from github to the virtual machine
		git clone https://github.com/ankitamayekar/catalog_for_linux.git
	
	rename the project folder
		sudo mv ./catalog_for_linux ./FlaskApp
		cd FlaskApp
	
	rename finalproject.py to __init__.py
		sudo mv finalproject.py __init__.py
		
	Edit db.py, data.py and finalproject.py and change engine 
		from 
			engine = create_engine('sqlite:///dbentries.db')
		to
			engine = create_engine('postgresql://catalog:password@localhost/catalog')
	
		
		
		
	installing pip
		sudo apt-get install python-pip
	Use pip to install dependencies
		sudo pip install --upgrade
		sudo apt-get install python-sqlalchemy
		sudo apt-get install python-flask
	Install psycopg2
		sudo apt-get -qqy install postgresql python-psycopg2
			
	create database.
		sudo python db.py
			


## 14. Set it up in your server so that it functions correctly when visiting your server’s IP address in a browser. Make sure that your .git directory is not publicly accessible via a browser!
	create FlaskApp.conf
		sudo nano /etc/apache2/sites-available/FlaskApp.conf
	Add the following code to the file.
		<VirtualHost *:80>
			ServerName 52.25.194.149
			ServerAdmin kambliketan@gmail.com
			WSGIScriptAlias / /var/www/FlaskApp/flaskapp.wsgi
			<Directory /var/www/FlaskApp/FlaskApp/>
				Order allow,deny
				Allow from all
			</Directory>
			Alias /static /var/www/FlaskApp/FlaskApp/static
			<Directory /var/www/FlaskApp/FlaskApp/static/>
				Order allow,deny
				Allow from all
			</Directory>
			ErrorLog ${APACHE_LOG_DIR}/error.log
			LogLevel warn
			CustomLog ${APACHE_LOG_DIR}/access.log combined
		</VirtualHost>
	
	Enable the virtual host
		sudo a2ensite FlaskApp
		
	Create the .wsgi file
		cd /var/www/FlaskApp/
		sudo nano flaskapp.wsgi
		
	Add the following code to the file
		#!/usr/bin/python
		import sys
		import logging
		logging.basicConfig(stream=sys.stderr)
		sys.path.insert(0,"/var/www/FlaskApp/")

		from FlaskApp import app as application
		application.secret_key = 'supersecretkey'
		
	Restart Apache
		sudo service apache2 restart
		
## Visit
		http://52.25.194.149
		
## References:
	https://devops.profitbricks.com/tutorials/deploy-a-flask-application-on-ubuntu-1404/
	https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps
	
	http://songhuiming.github.io/pages/2016/10/30/set-up-flask-web-host-on-digitalocean-vps/
	

	
