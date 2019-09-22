import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='python', passwd='TestTestTest',
                               auth_plugin='mysql_native_password')
if mydb:
    print('Connection Success')
else:
    print('Unable to connect')

my_cursor = mydb.cursor()
my_cursor.execute('CREATE DATABASE IF NOT EXISTS users')
my_cursor.execute('USE users')
my_cursor.execute('DROP TABLE IF EXISTS users')

my_cursor.execute(
    'CREATE TABLE IF NOT EXISTS employee(id int AUTO_INCREMENT PRIMARY KEY, name varchar(25), salary int)')
# Another way
# my_cursor.execute(
#     'CREATE TABLE IF NOT EXISTS employee(id int AUTO_INCREMENT, name varchar(25), salary int, PRIMARY KEY(id))')
val = [
    ('Anoop CH', 12000),
    ('AB', 12800),
    ('AH', 12500),
    ('DC CH', 13000),
    ('E CH', 14000),
    ('AA CH', 242424),
    ('BB CH', 15000),
    ('XX CH', 12000),
    ('MD CH', 32000),
    ('ND CH', 19000),
    ('AD CH', 24000)
]

sql_query = "INSERT INTO employee (id, name, salary) VALUES (0, %s, %s)"
my_cursor.executemany(sql_query, val)

# For CURD operations commit is mandatory
mydb.commit()

# ASC DESC
# AND OR NOT - to combine the different conditions
my_cursor.execute('SELECT * FROM employee WHERE salary > 15000 ORDER BY name ASC LIMIT 25')
records = my_cursor.fetchall()
if records is not None:
    for employee in records:
        print(employee)

mydb.close()
