import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='python', passwd='TestTestTest', auth_plugin='mysql_native_password')

print(mydb)
