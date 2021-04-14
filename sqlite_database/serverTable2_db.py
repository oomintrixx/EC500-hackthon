import sqlite3

# server table two: table userd for password
# primary ID, username(string), password(string)
def server_database2():
    conn = sqlite3.connect('server_table2.db') #Opens Connection to SQLite database file.
    conn.cursor().execute('''CREATE TABLE server_table2
                (PRIMARY_ID     INTEGER,
                USERNAME        TEXT,
                PASSWORD        TEXT
                );''')
    conn.commit()
    conn.close()

#create user with primary id, username, and password
def create_svtable2(primaryid, username, password):
    conn = sqlite3.connect('server_table2.db')
    cursor = conn.cursor()
    params = (primaryid, username,password)
    cursor.execute("INSERT INTO server_table2 VALUES (?,?,?)",params)
    conn.commit()
    #print('User Creation Successful')
    conn.close()
    #return True

#return bool 'True' if username matches password as stored inside the database
def confirm_login(username,password):
    conn = sqlite3.connect('server_table2.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM server_table2 WHERE USERNAME =:USERNAME",{'USERNAME':username})

    if cur.fetchone()[2] == password:
        #print('LogIn Successful')
        return True

#retrieve all information stored inside server table 2
def retrieve_all():
    conn = sqlite3.connect('server_table2.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM server_table2")
    return (cur.fetchall())

#return all information associated with this primary id
def retrieve_specific(primaryid):
    conn = sqlite3.connect('server_table2.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM server_table2 WHERE PRIMARY_ID =:PRIMARY_ID",{'PRIMARY_ID':primaryid})
    return (cur.fetchall())

#return username if user input primaryid
def retrieve_username(primaryid):
    conn = sqlite3.connect('server_table2.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM server_table2 WHERE PRIMARY_ID =:PRIMARY_ID",{'PRIMARY_ID':primaryid})
    return (cur.fetchone()[1])

#return primary id if input username
def retrieve_primaryid(username):
    conn = sqlite3.connect('server_table2.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM server_table2 WHERE USERNAME =:USERNAME",{'USERNAME':username})
    return (cur.fetchone()[0])

#delete all information related to this username from the database
def delete_userFromUsername(username):
    conn = sqlite3.connect('server_table2.db')
    cur = conn.cursor()
    cur.execute("""DELETE FROM server_table2 WHERE USERNAME =:USERNAME """,{'USERNAME':username})
    conn.commit()
    conn.close()
    #return  True

#delete all information related to this username from the database
def delete_userFromID(primaryid):
    conn = sqlite3.connect('server_table2.db')
    cur = conn.cursor()
    cur.execute("""DELETE FROM server_table2 WHERE PRIMARY_ID =:PRIMARY_ID """,{'PRIMARY_ID':primaryid})
    conn.commit()
    conn.close()

#delete all information from database
def delete_all():
    conn = sqlite3.connect('server_table2.db')
    cur = conn.cursor()
    cur.execute("""DELETE FROM server_table2""")
    conn.commit()
    conn.close()
