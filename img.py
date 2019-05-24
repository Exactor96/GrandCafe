import sqlite3
import requests

con = sqlite3.connect('recipe.db')

cur = con.cursor()

cur.execute('select * from images')


print(cur.fetchone())
 
