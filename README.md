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
  
      database.set(key, value)
      database.get(key, value)
    
