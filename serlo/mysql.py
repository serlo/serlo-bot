import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    port="3306",
    database="serlo",
    charset="latin1"
)

def query(sql):
    c = db.cursor()
    c.execute(sql)

    return c.fetchall()
