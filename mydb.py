import mysql.connector

data_base = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123'

)


cursor_object = data_base.cursor()

cursor_object.execute('CREATE DATABASE stockExchange')

print('Exito al crear db.')


#uso unico
