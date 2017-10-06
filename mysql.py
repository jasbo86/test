import pymysql

class Database:

    def __init__(self):
        self.conn=pymysql.connect(host='localhost',
                             user='root',
                             password='m0ng0lf13r4',
                             db='marco',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        self.cur=self.conn.cursor()


    def create_table(self,name,col):
        column=""
        x=0
        while x < len(col)-1:
            if x==0:
                column=col[x] +" "+ col[x+1]
            else:
                column=column +","+ col[x]+" "+col[x+1]
            x=x+2

        self.cur.execute("CREATE TABLE IF NOT EXISTS "+ name +" (id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY, "+ column +")")
        row=self.conn.commit()
        return True



    def show_tables(self,table):
        self.cur.execute("SHOW TABLES LIKE '"+ table +"'")
        rows=self.cur.fetchall()
        return rows

    def describe_table(self,table):
        self.cur.execute("DESCRIBE "+ table)
        rows=self.cur.fetchall()
        return rows

    def insert(self,title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES(%s,%s,%s,%s)",(title,author,year,isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        return rows

    def search(self,title="",author="",year="",isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title=%s OR author=%s OR year=%s OR isbn=%s)",(title,author,year,isbn))
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE from book WHERE id=%s",(id))
        self.conn.commit()


    def update(self,id,title="", author="", year="", isbn=""):
        self.cur.execute("UPDATE book SET title=%s, author=%s, year=%s, isbn=%s WHERE id=%s",(title, author, year, isbn,id))
        self.conn.commit()


    def __del__(self):
        self.conn.close()
