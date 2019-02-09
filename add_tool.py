import sqlite3

connection = sqlite3.connect("./db/bad_words.db")
cursor = connection.cursor()

file = open("./to_add.md", 'r', encoding = "UTF8")

to_add = [line.rstrip() for line in file] 

for word in to_add:
    query = "select \"" + word + "\" from bad_words"
    cursor.execute(query)

r = cursor.fetchall()
print(r)

file.close()
 #to_add.close()
