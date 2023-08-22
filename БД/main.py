import sqlite3

con = sqlite3.connect('test.db')

curObj = con.cursor()


curObj.execute("SELECT name FROM manga")

rows = curObj.fetchall()

print(rows)