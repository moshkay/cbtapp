#tables in the database
#maths
#userdetails
#admindetails
#subjecttab
import sqlite3 as lite
conn=lite.connect("cbtapp.db")
cursor=conn.cursor()
b=cursor.execute("""select * from admindetails""")
for i in b:
    print(i)

