#creating the database for the cbt app
#dbs  subjecttab,admindetails....
try:
    
    import sqlite3 as lite
    conn=lite.connect("cbtapp.db")
    cursor=conn.cursor()

    cursor.execute("""create table userdetails(ID integer primary key autoincrement,username char(20) unique,password char(20))""")
    conn.close()
    print("table created successfully")
except:
    print("an error occured while creating the table")



