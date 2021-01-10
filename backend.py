import sqlite3 as db

def connect():
    conn = db.connect('books.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE if NOT exists BOOK(id INTEGER PRIMARY KEY, title text, author text, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

'''def connectx():
    conn = db.connect('bookstest.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE if NOT exists BOOKT(id INTEGER PRIMARY KEY, title text, author text, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()'''

def issue():
    conn= db.connect('books.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE if NOT exists issue(id INTEGER NOT NULL, title text, author text, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def request():
    conn = db.connect('request.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE if NOT exists REQUEST(id INTEGER PRIMARY KEY, title text, author text, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn = db.connect('books.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO BOOK VALUES(NULL,?,?,?,?)',(title,author,year,isbn))
    conn.commit()
    conn.close()

'''def insert(title, author, year, isbn):
    conn = db.connect('bookstest.db')
    cur=conn.cursor()
    cur.execute('INSERT into BOOKT values(NULL,?,?,?,?)',(title,author,year,isbn))
    conn.commit()
    conn.close()'''

def request_insert(title,author,year,isbn):
    conn=db.connect('request.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO REQUEST VALUES(NULL,?,?,?,?)',(title,author,year,isbn))
    conn.commit()
    conn.close()

def request_view(title="",author="",year="",isbn=""):
    conn= db.connect('request.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM REQUEST")
    rows=cur.fetchall()
    conn.close()
    return rows

def request_delete(id):
    conn= db.connect('request.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM REQUEST WHERE id=?",(id,) )
    conn.commit()
    conn.close()

def issue_insert(id):
    conn = db.connect('books.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO issue SELECT * FROM BOOK WHERE id=?',(id,))
    conn.commit()
    conn.close()

def issue_delete(id):
    conn = db.connect('books.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM issue where id=?",(id,))
    conn.commit()
    conn.close()

def issue_view(title="",author="",year="",isbn=""):
    conn=db.connect('books.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM issue")
    rows = cur.fetchall()
    conn.close()
    return rows

def view():
    conn=db.connect('books.db')
    cur=conn.cursor()
    cur.execute('Select * FROM BOOK')
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",isbn=""):
    conn=db.connect('books.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM BOOK WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

'''def view():
    conn=db.connect('bookstest.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM BOOKT")
    rows=cur.fetchall()
    #conn.close()
    for row in rows:
        print(row)'''

'''connectx()
titlex=input()
authorx=input()
yearx=int(input())
isbnx=int(input())
insert(titlex,authorx,yearx, isbnx)
view()'''

def delete(id):
    conn=db.connect('books.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM BOOK WHERE id=?",(id,) )
    conn.commit()
    conn.close()

def update(id, title, author, year, isbn ):
    conn= db.connect('books.db')
    cur = conn.cursor()
    cur.execute("UPDATE BOOK SET title=? ,author=?, year=?, isbn=? WHERE id=?",(title, author, year, isbn, id))
    conn.commit()
    conn.close()

connect()
issue()
request()
