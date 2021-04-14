 ## Notes on output and how to access output data from sqlite database python file
 
1. **retrieve_all()** function
* returns a tuple of all information stored inside a database
* for example, the server_table3.db contains the following:

| PRIMARY_ID  | USERNAME  | IP_ADDRESS | PORT | PUBLIC_KEY |
| ---------- | ---------- | ---------- | ---------- | ---------- |
| 1      | test1 | 127.0.0.0 | 4200 | 10x |
| 2      | test2 | 127.0.0.2| 4202 | 12x |
| 3 | test3 | 127.0.0.3 | 4203 | 13x |

```python
var1 = retrieve_all()
  print(var1)
```
will return
```
[(1, 'test1', '127.0.0.0', 4200, '10x'), (2, 'test2', '127.0.0.2', 4202, '12x'), (3, 'test3', '127.0.0.3', 4203, '13x')]
```

2. **retrieve_specific(primaryid)** function
* return a tuple of information associated to specifice primary id
* using the server_table3.db shown above, 
```python
var2 = retrieve_specific(1)
    print(var2)
```
will return 
```
[(1, 'test1', '127.0.0.0', 4200, '10x')]
```
If users want to access the username from the above tuple, user can do
```python
var[0][1]
```
the above code will return
```
test1
```
with the <class 'str'> as its type
