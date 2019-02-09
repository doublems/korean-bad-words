import sqlite3

connection = sqlite3.connect("./db/bad_words.db")
cursor = connection.cursor()

file = open("./to_add.md", 'r', encoding = "UTF8")

to_add = [line.rstrip() for line in file] 

for word in to_add:
    query = "select " + word + " from bad_words"
    #print(query)
    cursor.execute(query)
    r = cursor.fetchall()
    #print(word, end ="")


file.close()
 #to_add.close()
