import sqlite3
#import datetime

# table one: table used for store chat_record
# primary ID, username, text(content of chat), time(the time of the chat)

def client_database1():
    conn = sqlite3.connect('client_table1.db') #Opens Connection to SQLite database file.
    conn.cursor().execute('''CREATE TABLE client_table1
                (PRIMARY_ID     INTEGER,
                USERNAME        TEXT,
                TEXT            TEXT,
                TIME            BLOB
                );''')
    conn.commit()
    conn.close()

#create client table 1 with primary id, username, text, time
def create_cltable1(primaryid, username, text, time):
    conn = sqlite3.connect('client_table1.db')
    cursor = conn.cursor()
    params = (primaryid, username, text, time)
    cursor.execute("INSERT INTO client_table1 VALUES (?,?,?,?)",params)
    conn.commit()
    #print('User Creation Successful')
    conn.close()

#retrieve all information stored inside client table 1
def retrieve_all():
    conn = sqlite3.connect('client_table1.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM client_table1")
    return (cur.fetchall())

#return all information associated with this primary id
def retrieve_specific(primaryid):
    conn = sqlite3.connect('client_table1.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM client_table1 WHERE PRIMARY_ID =:PRIMARY_ID",{'PRIMARY_ID':primaryid})
    return (cur.fetchall())

#delete all information related to this username from the database
def delete_userFromUsername(username):
    conn = sqlite3.connect('client_table1.db')
    cur = conn.cursor()
    cur.execute("""DELETE FROM client_table1 WHERE USERNAME =:USERNAME """,{'USERNAME':username})
    conn.commit()
    conn.close()

#delete all information related to this primary from the database
def delete_userFromID(primaryid):
    conn = sqlite3.connect('client_table1.db')
    cur = conn.cursor()
    cur.execute("""DELETE FROM client_table1 WHERE PRIMARY_ID =:PRIMARY_ID """,{'PRIMARY_ID':primaryid})
    conn.commit()
    conn.close()

#delete all information from database
def delete_all():
    conn = sqlite3.connect('client_table1.db')
    cur = conn.cursor()
    cur.execute("""DELETE FROM client_table1""")
    conn.commit()
    conn.close()
