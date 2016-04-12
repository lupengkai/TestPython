import mysql.connector

conn = mysql.connector.connect(user='root', password='0715', database='test')
cursor = conn.cursor()

cursor.execute('create table user (id varchar(20) PRIMARY KEY , name VARCHAR(20))')

cursor.execute('insert into user (id, name) values (%s,%s)', ['1', 'tage'])

cursor.rowcount

conn.commit()
cursor.close()

cursor = conn.cursor()

cursor.execute('select * from user WHERE id = %s', ('1',))

values = cursor.fetchall()

print(values)

cursor.close()

conn.close()
