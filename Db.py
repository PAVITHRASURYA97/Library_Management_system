
import sqlite3

class Employees:
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS employees(
        id Integer Primary Key,
        name text,
        age text,
        doj text,
        email text,
        gender text,
        contact text,
        address text
        )
"""
              
        self.cur.execute(sql)
        self.con.commit()
        #insert function
"""
    def insert(self, id, name, age, doj, email, gender, contact, address):
            self.cur.execute("insert into employees values(NULL,?,?,?,?,?,?,?)",
            (name, age, doj, email, gender, contact, address))
            self.con.commit()

            #fetch all data from DB

    def fetch(self):
        self.cur.execute("SELECT  * from employees")
        rows=self.cur.fetchall()
        #print(rows)
        return rows
    #DELETE  A RECORD  IN DB
    def remove(self,db):
        self.cur.execute("insert data from files",())
        self.con.commit()
"""
o=Employees("employee.db")
#o.insert("9","Kavi","29","12-10-2015","kavitha@gmail.com","Female","9789798235","sevvanthi nagar,Madurai")

