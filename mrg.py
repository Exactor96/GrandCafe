import sqlite3

con1 = sqlite3.connect('db.sqlite3')
con2 = sqlite3.connect('recipes.db')

cur1=con1.cursor()
cur2=con2.cursor()

cur2.execute("""Select * from recipes""")

for each in cur2.fetchall():
    print(each['title'])
    break
