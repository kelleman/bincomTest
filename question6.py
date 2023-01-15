import psycopg2
import bincomTest
 
# connection establishment
conn = psycopg2.connect(
   database="uniformDB",
    user='Godfrey',
    password='root',
    host='localhost',
    port= '5432'
)
   
 
conn.autocommit = True
cursor = conn.cursor()
 
sql = '''CREATE TABLE uniformColors(
          colors char(20),
          freq int);'''
 
 
cursor.execute(sql)

# accessing variables from a file bincomTest.py
columns= bincomTest.data.keys()
for i in bincomTest.data.values():
    sql2='''insert into uniformColors(colors ,
          frequency) VALUES{};'''.format(i)
 
    cursor.execute(sql2)
 
sql3='''select * from uniformColors;'''
cursor.execute(sql3)
for i in cursor.fetchall():
    print(i)
 
conn.commit()
conn.close()