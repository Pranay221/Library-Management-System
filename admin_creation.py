'''NOT FOR USE, KINDLY IGNORE THIS FILE.
THIS IS ONLY FOR REGISTERING AS ADMINS
. NOT TO BE USED ALONG WITH APPLICATION'''

'''import sqlite3 as db

conn= db.connect('login.db')
cur= conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type IN ('table','view') AND name NOT LIKE 'sqlite_%'ORDER BY 1;")
t=cur.fetchall()
for i in t:
    print(t)'''

'''cur.execute("CREATE TABLE if not exists admin(admid INTEGER PRIMARY KEY, name text, password text)")

conn.commit()
conn.close()'''
'''cur.execute("INSERT into admin values(02,'Yash','apsian')")
conn.commit()
conn.close()'''

'''cur.execute("Select * from admin")
x=cur.fetchall()
for i in x:
    print(i)'''