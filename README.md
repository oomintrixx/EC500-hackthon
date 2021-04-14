# EC500-hackthon

### First Milestone to accomplish
* Send messages between two clients
* Design your database
* Store data and retrieve it from a database
* Hard code discovery



### proposal
https://docs.google.com/document/d/1JWQu_GTM7QKCp5zlLjdlWdxtNVslb-jGqFCkIWc_xe4/edit?ts=606e1b52

### Datebase 
  Client:
  
    table one: table used for store chat_record
    primary ID, username, text(content of chat), time(the time of the chat)
  
    table two: table used for store friends
    primary ID, username(string), ip address(string), port(int), public key(string)
    
    table three: table used for store online_users
    primary ID, username(string), ip address(string), port(int), public key(string)
    
    table four: table used for personal informations
    primary ID, username(string), ip address(string), port(int), public key(string), private key(string)
    
  Server:
    
    table three: table used for store online_users
    primary ID, username(string), ip address(string), port(int), public key(string)
    
    table two: table userd for password
    primary ID, username(string), password(string)
  
  Interface:
  
      database.set(tablename, key, value)
      database.get(tablename, key, value)
      
 ## Notes on output and how to access output data from sqlite database python file
 
1. **retrieve_all()** function
* returns a tuple of all information stored inside a database
* for example, the server_table3.db contains the following:

| PRIMARY_ID  | USERNAME  | IP_ADDRESS | PORT | PUBLIC_KEY |
| ---------- | ---------- | ---------- | ---------- | ---------- |
| 1      | test1 | 127.0.0.0 | 4200 | 11x |
| 2      | test2 | 127.0.0.2| 4202 | 12x |
| 3 | test3 | 127.0.0.3 | 4203 | 13x |

> var1 = retrieve_all()
  print(var1)
    
will return
```
[(1, 'test1', '127.0.0.0', 4200, '10x'), (2, 'test2', '127.0.0.2', 4202, '12x'), (3, 'test3', '127.0.0.3', 4203, '13x')]
```

