import sqlite3

connection = sqlite3.connect("./db/bad_words.db")
cursor = connection.cursor()

file = open("./to_add.md", 'r', encoding = "UTF8")

to_add = [line.rstrip() for line in file] 

for word in to_add:
    select_query = "select word from bad_words where word = \"" + word + "\""
    cursor.execute(select_query)

    exist = cursor.fetchone()
    print(exist, end = " ")

    if not exist:
        insert_query = "insert into bad_words (word) values(?)"  
        cursor.execute(insert_query, (word,) )
        connection.commit()

connection.commit()
connection.close()

file.close()
