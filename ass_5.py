# Aayush Maurya
# 1901002

import mysql.connector
import boto3

user_script = '''#!/bin/bash
sudo yum update -y
sudo amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2
sudo yum install -y httpd
sudo systemctl start httpd
sudo systemctl enable httpd
cd /var/www/html
rm index.html
wget https://aayushmauryaassignment2.s3.amazonaws.com/index.html'''


def create_db_instance():
    rds = boto3.client('rds')

    response = rds.create_db_instance(
        DBName='db2',
        DBInstanceIdentifier='aayush',
        MasterUsername='aayush',
        MasterUserPassword='123456789',
        DBInstanceClass='db.t2.micro',
        Engine='mysql',
        AllocatedStorage=10)

    print(response)


def connection():
    try:
        connection = mysql.connector.connect(host='aayush.cmyi9iqznzuz.us-east-1.rds.amazonaws.com',
                                             port=3306,
                                             user='aayush',
                                             passwd='123456789',
                                             database='db2')
        print(connection)
        db = connection.cursor()
       # db.execute("show databases;")
        db.execute("use db2")
        db.execute('create table complainable(name varchar(15) primary key,complaint varchar(15))')
        db.execute("show tables")
        result = db.fetchall()
        print(result)
    except Exception as e:
        print(e)


#create_db_instance()
connection()
