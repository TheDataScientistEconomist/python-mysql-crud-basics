# import required dependencies
import mysql.connector as connector
import yaml

# safely connect to database. Note that we're safely loading the connection details through yaml
db = yaml.safe_load(open('db.yaml'))
cnx = connector.connect(**
    {
    'user':     db['user'],
    'password': db['password'],
    'host':     db['host'],
    'database': db['db'],
    'auth_plugin':'mysql_native_password'
}
)

# create cursor
cursor = cnx.cursor()

# delete previous db
query = ("DROP DATABASE IF EXISTS `restaurants`;")
cursor.execute(query)

# create db
query = ("CREATE DATABASE IF NOT EXISTS `restaurants`")
cursor.execute(query)

# use db
query = ("USE restaurants")
cursor.execute(query)

# create table
query = ('''
CREATE TABLE restaurants(
    id VARCHAR(20) PRIMARY KEY,
    name VARCHAR(20)
)
''')
cursor.execute(query)

# clean up
cnx.commit()
cursor.close()
cnx.close()    