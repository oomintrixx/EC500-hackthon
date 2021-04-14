import sqlite3

#server table three: table used for store online_users
#primary ID, username(string), ip address(string), port(int), public key(string)

def server_database3():
    conn = sqlite3.connect('server_table3.db') #Opens Connection to SQLite database file.
    conn.cursor().execute('''CREATE TABLE server_table3
                (PRIMARY_ID     INTEGER,
                USERNAME        TEXT,
                IP_ADDRESS      TEXT,
                PORT            INTEGER,
                PUBLIC_KEY      TEXT
                );''')
    conn.commit()
    conn.close()

#create server table 3 with primary id, username, ip address, port, and public key
def create_svtable3(primaryid, username, ipaddress, port, publickey):
    conn = sqlite3.connect('server_table3.db')
    cursor = conn.cursor()
    params = (primaryid, username, ipaddress, port, publickey)
    cursor.execute("INSERT INTO server_table3 VALUES (?,?,?,?,?)",params)
    conn.commit()
    #print('User Creation Successful')
    conn.close()

#retrieve all information stored inside server table 3
def retrieve_all():
    conn = sqlite3.connect('server_table3.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM server_table3")
    return (cur.fetchall())

#return all information associated with this primary id
def retrieve_specific(primaryid):
    conn = sqlite3.connect('server_table3.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM server_table3 WHERE PRIMARY_ID =:PRIMARY_ID",{'PRIMARY_ID':primaryid})
    return (cur.fetchall())

#delete all information related to this username from the database
def delete_userFromUsername(username):
    conn = sqlite3.connect('server_table3.db')
    cur = conn.cursor()
    cur.execute("""DELETE FROM server_table3 WHERE USERNAME =:USERNAME """,{'USERNAME':username})
    conn.commit()
    conn.close()

#delete all information related to this primary from the database
def delete_userFromID(primaryid):
    conn = sqlite3.connect('server_table3.db')
    cur = conn.cursor()
    cur.execute("""DELETE FROM server_table3 WHERE PRIMARY_ID =:PRIMARY_ID """,{'PRIMARY_ID':primaryid})
    conn.commit()
    conn.close()

#delete all information from database
def delete_all():
    conn = sqlite3.connect('server_table3.db')
    cur = conn.cursor()
    cur.execute("""DELETE FROM server_table3""")
    conn.commit()
    conn.close()
