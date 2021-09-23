import boto3
import mysql.connector
# rdsClient = boto3.client("rds")

# print("Creating RDS MYSQL Database")
# response = rdsClient.create_db_instance(
#     DBName="abhinandanKumar",
#     DBInstanceIdentifier="abhinandanKumar",
#     AllocatedStorage=5,
#     DBInstanceClass="db.t2.micro",
#     Engine="MySQL",
#     MasterUsername="abhinandanKumar",
#     MasterUserPassword="abhinandanKumar",
#     PubliclyAccessible=True,
# )

# import time

# while True:
#     response = rdsClient.describe_db_instances(
#         DBInstanceIdentifier="abhinandanKumar",
#         MaxRecords=20,
#     )

#     status = response["DBInstances"][0]["DBInstanceStatus"]

#     if status == "available" or status == "AVAILABLE":
#         break
#     else:
#         time.sleep(10)

# print("Successfully Created ")
# print(response["DBInstances"][0]["Endpoint"]["Address"])


def connection():
    try:
        connection = mysql.connector.connect(host='abhinandankumar.cuwzqfpzmzt3.us-east-1.rds.amazonaws.com',
                                             port=3306,
                                             user='abhinandanKumar',
                                             passwd='abhinandanKumar',
                                             database='abhinandanKumar')
        print(connection)
        db = connection.cursor()
       # db.execute("show databases;")
        db.execute("use abhinandanKumar")
        # db.execute(
        #     'create table complainable(name varchar(15) primary key,complaint varchar(15))')
        db.execute("show tables")
        result = db.fetchall()
        print(result)
    except Exception as e:
        print(e)


#create_db_instance()
connection()
