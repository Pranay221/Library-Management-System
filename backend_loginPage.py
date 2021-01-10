import sqlite3 as db
from tkinter import *
from tkinter import messagebox
import admin
import student

def connect():
    conn= db.connect('login.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE if not exists user(rollno INTEGER PRIMARY KEY, name text, password text)")
    conn.commit()
    conn.close()

def insert(name,password):
    conn= db.connect('login.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO user VALUES(NULL,?,?)',(name,password))
    conn.commit()
    conn.close()

def check(name,password):
    conn= db.connect('login.db')
    cur = conn.cursor()
    if(cur.execute('SELECT * FROM admin WHERE name =? AND password = ?',(name,password))):
        if cur.fetchone():
            admin.runx()
            '''window = Tk()
            window.title('Admin_User')
            window.geometry('700x400')
            admin.admin(window)
            window.mainloop()'''
        else:
            messagebox.showinfo('error:','INVALID CREDENTIALS for ADMIN LOGIN')

def checks(name,password):
    conn= db.connect('login.db')
    cur = conn.cursor()
    if(cur.execute('SELECT * FROM user WHERE name =? AND password = ?',(name,password))):
        if cur.fetchone():
            window = Tk()
            window.title('Student_User')
            window.geometry('700x450')
            student.student(window)
            window.mainloop()
        else:
            messagebox.showinfo('error:','INVALID CREDENTIALS for STUDENT LOGIN')

    conn.commit()
    conn.close()

connect()