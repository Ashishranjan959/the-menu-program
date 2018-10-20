import sqlite3

def connect():
    conn=sqlite3.connect("student.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY,name text,year text,sub1 integer,sub2 integer,sub3 integer,sub4 integer,sub5 integer)")
    conn.commit()
    conn.close()

def insert(name,year,sub1,sub2,sub3,sub4,sub5):
    conn=sqlite3.connect("student.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO student VALUES(NULL,?,?,?,?,?,?,?)",(name,year,sub1,sub2,sub3,sub4,sub5))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("student.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM student")
    rows =cur.fetchall()
    conn.close()
    return rows


def search(name='',year=''):
    conn=sqlite3.connect("student.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM student WHERE name=? OR year=?",name,year)
    print('hey I am working')
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("student.db")
    cur=conn.cursor()
    cur.execute('DELETE FROM student WHERE id=?',(id))
    print('hey i am also working')
    conn.commit()
    conn.close()


def update(id,name,year,sub1,sub2,sub3,sub4,sub5):
    conn=sqlite3.connect("student.db")
    cur=conn.cursor()
    cur.execute("UPDATE student SET name=?,year=?,sub1=?,sub2=?,sub3=?,sub4=?,sub5=?",(name,year,sub1),(sub2,sub3),(sub4,sub5))
    print("HIII I am from update method")
    conn.commit()
    conn.close()

 
