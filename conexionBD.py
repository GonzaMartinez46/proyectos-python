import mysql.connector

conexion = mysql.connector.connect(
    user='root',
    password='37913791',
    host='localhost',
    database='club',
    port='3306'
)

print(conexion)