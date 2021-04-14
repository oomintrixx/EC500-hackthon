import sqlite3

# table three: table used for store online_users
# primary ID, username(string), ip address(string), port(int), public key(string)

def client_database3():
    conn = sqlite3.connect('client_table3.db') #Opens Connection to SQLite database file.
    conn.cursor().execute('''CREATE TABLE client_table3
                (PRIMARY_ID     INTEGER,
                USERNAME        TEXT,
                IP_ADDRESS      TEXT,
                PORT            INTEGER,
                PUBLIC_KEY      TEXT
                );''')
    conn.commit()
    conn.close()

#create client table 3 with primary id, username, text, time
def create_cltable3(primaryid, username, ipaddress, port, publickey):
    conn = sqlite3.connect('client_table3.db')
    cursor = conn.cursor()
    params = (primaryid, username, ipaddress, port, publickey)
    cursor.execute("INSERT INTO client_table3 VALUES (?,?,?,?,?)",params)
    conn.commit()
    #print('User Creation Successful')
    conn.close()

#retrieve all information stored inside client table 3
def retrieve_all():
    conn = sqlite3.connect('client_table3.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM client_table3")
    return (cur.fetchall())

#return all information associated with this primary id
def retrieve_specific(primaryid):
    conn = sqlite3.connect('client_table3.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM client_table3 WHERE PRIMARY_ID =:PRIMARY_ID",{'PRIMARY_ID':primaryid})
    return (cur.fetchall())

#delete all information related to this username from the database
def delete_userFromUsername(username):
    conn = sqlite3.connect('client_table3.db')
    cur = conn.cursor()
    cur.execute("""DELETE FROM client_table3 WHERE USERNAME =:USERNAME """,{'USERNAME':username})
    conn.commit()
    conn.close()

#delete all information related to this primary from the database
def delete_userFromID(primaryid):
    conn = sqlite3.connect('client_table3.db')
    cur = conn.cursor()
    cur.execute("""DELETE FROM client_table3 WHERE PRIMARY_ID =:PRIMARY_ID """,{'PRIMARY_ID':primaryid})
    conn.commit()
    conn.close()

#delete all information from database
def delete_all():
    conn = sqlite3.connect('client_table3.db')
    cur = conn.cursor()
    cur.execute("""DELETE FROM client_table3""")
    conn.commit()
    conn.close()

# if __name__ == "__main__":
#     #client_database3()
#     # x = datetime.datetime.now()
#     # create_cltable3(1, "test", "127.0", 4200, "10x")
#     # create_cltable3(2, "test2", "127.2", 4202, "12x")
#     # create_cltable3(3, "test3", "127.3", 4203, "13x")
#     #create_cltable1(2, "test2", "hello this is test2", x)
#     # # create_cltable1(3, "test3", "hello this is test3", x)
#     var = retrieve_all()
#     print(var)
#     # var2 = retrieve_specific(3)
#     # print(var2)
#     # print(var2[0][3])
#     # print(type(var2[0][3]))
#     # delete_all()
#     # delete_userFromID(1)
#     # delete_userFromUsername("test2")
