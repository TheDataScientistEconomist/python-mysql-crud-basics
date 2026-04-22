# import required dependencies
import mysql.connector as connector
import yaml

# safely establish MySQL connection. Note that we're safely loading the connection details through yaml
db = yaml.safe_load(open('db.yaml'))
cnx = connector.connect(**
    {
    'user':     db['user'],
    'password': db['password'],
    'host':     db['host'],
    'auth_plugin':'mysql_native_password'
}
)

# create cursor
cursor = cnx.cursor()

# load the database schema. In this example, we're using the restaurants database
query = ('USE restaurants;')
cursor.execute(query)

# use the SELECT command READ records from a table in the database. In this example, we're using the restaurants table
query = ('SELECT* FROM restaurants;')
cursor.execute(query)

# print the query
for row in cursor.fetchall():
    print(row)

# clean up
cursor.close()
cnx.close()

