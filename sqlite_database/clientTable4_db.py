import sqlite3

# table four: table used for personal informations
# primary ID, username(string), ip address(string), port(int), public key(string), private key(string)

def client_database4():
    conn = sqlite3.connect('client_table4.db') #Opens Connection to SQLite database file.
    conn.cursor().execute('''CREATE TABLE client_table4
                (PRIMARY_ID     INTEGER,
                USERNAME        TEXT,
                IP_ADDRESS      TEXT,
                PORT            INTEGER,
                PUBLIC_KEY      TEXT,
                PRIVATE_KEY     TEXT
                );''')
    conn.commit()
    conn.close()

#create client table 4 with primary id, username, text, time
def create_cltable4(primaryid, username, ipaddress, port, publickey, privatekey):
    conn = sqlite3.connect('client_table4.db')
    cursor = conn.cursor()
    params = (primaryid, username, ipaddress, port, publickey, privatekey)
    cursor.execute("INSERT INTO client_table4 VALUES (?,?,?,?,?,?)",params)
    conn.commit()
    #print('User Creation Successful')
    conn.close()

#retrieve all information stored inside client table 4
def retrieve_all():
    conn = sqlite3.connect('client_table4.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM client_table4")
    return (cur.fetchall())

#return all information associated with this primary id
def retrieve_specific(primaryid):
    conn = sqlite3.connect('client_table4.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM client_table4 WHERE PRIMARY_ID =:PRIMARY_ID",{'PRIMARY_ID':primaryid})
    return (cur.fetchall())

#delete all information related to this username from the database
def delete_userFromUsername(username):
    conn = sqlite3.connect('client_table4.db')
    cur = conn.cursor()
    cur.execute("""DELETE FROM client_table4 WHERE USERNAME =:USERNAME """,{'USERNAME':username})
    conn.commit()
    conn.close()

#delete all information related to this primary from the database
def delete_userFromID(primaryid):
    conn = sqlite3.connect('client_table4.db')
    cur = conn.cursor()
    cur.execute("""DELETE FROM client_table4 WHERE PRIMARY_ID =:PRIMARY_ID """,{'PRIMARY_ID':primaryid})
    conn.commit()
    conn.close()

#delete all information from database
def delete_all():
    conn = sqlite3.connect('client_table4.db')
    cur = conn.cursor()
    cur.execute("""DELETE FROM client_table4""")
    conn.commit()
    conn.close()
