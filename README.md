# Hbnb console

```python
                    _   _    ___    _       ____    _____   ____    _____    ___    _   _   
                   | | | |  / _ \  | |     | __ )  | ____| |  _ \  |_   _|  / _ \  | \ | |  
                   | |_| | | | | | | |     |  _ \  |  _|   | |_) |   | |   | | | | |  \| |  
                   |  _  | | |_| | | |___  | |_) | | |___  |  _ <    | |   | |_| | | |\  |  
                   |_| |_|  \___/  |_____| |____/  |_____| |_| \_\   |_|    \___/  |_| \_| 

                                ____     ____   _   _    ___     ___    _        
                               / ___|   / ___| | | | |  / _ \   / _ \  | |       
                               \___ \  | |     | |_| | | | | | | | | | | |       
                                ___) | | |___  |  _  | | |_| | | |_| | | |___    
                               |____/   \____| |_| |_|  \___/   \___/  |_____|   
                               
                                                                   .
                                                 $$$$..
                                               ed$$$$$$F                      
                                               d$$$$$$$$
                                              ^$$$$$$$$$
                                               $$$$$$$$$$
                                              $$$$$$3$$$$$
                                             4$$$$$F "***$$b
                                             $$$$$$$c     "
                                             4$$$$$$$$c
                                              $$$$$$$$$$.
                                              ^$$$$$$$$$$
                                             . ^$$$$$$$$$b
                                          ^$$$  d$$$$$$$$$
                                           $$$$$$$$$$$$$$P
                                         *$$$$$$$$$$$$$$$
                                           $$$$$$$$$$$$$
                                         =*$$$$$$$$$$P"
                                           $**$$$$$P
                                             d$$$$F
                                             $$$$$
                                            4$$$$$    .e.
                                            ^$$$$$   dP*$L
                                             $$$$$   %  4$
                                             ^$$$$.     4$
                                              ^$$$$.   .$P
                                                *$$$$$$$$
                                                  "*$$*"    

                       _   _ ____  _   _ ____     ____ ___  _   _ ____   ___  _     _____ 
                      | | | | __ )| \ | | __ )   / ___/ _ \| \ | / ___| / _ \| |   | ____|
                      | |_| |  _ \|  \| |  _ \  | |  | | | |  \| \___ \| | | | |   |  _|  
                      |  _  | |_) | |\  | |_) | | |__| |_| | |\  |___) | |_| | |___| |___ 
                      |_| |_|____/|_| \_|____/   \____\___/|_| \_|____/ \___/|_____|_____|
 ```



## Description  📄

 The AirBnB console project. is just a piece of the AirBnB clone of Holberton School, is about to make a command interpreter that perform operations, all this as part of foundations program of cohort 11, It's completely made in Python 3 programming language and implement unittest library to make the project stable and more reliable.


## ¿What is a hbnb interpreter?  💻

The hbnb interpreter is the part of a computer operating system that understands and executes **commands** that are entered interactively by a human being or from a program. 

This interpreter is capable of doing operations such as: 

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object
 
and also works in Non interactive mode 


## How to start 👨🏻‍💻

```python
Clone the repository to your machine
$ git clone https://github.com/NICOLASTOBON/AirBnB_clone

Move in to the directory
$ cd AirBnB_clone

Execute the console file
/AirBnB_clone$ ./console.py
```



## Make it works 🎮

Our console performs the commands you will find above, each of them performs a different task.

You can directly ask the console the commands available,  just as simply as inside the command interpreter type the next command.

```
(hbnb) help
```

The interpreter will show you the commands available.

```python
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
```



To be more specific and be aware what each command performs we've written detailed documentation for each command, you can ask for it using this syntax i.e (help create)

```python
(hbnb) help update
update an instance.
        Usage 🛠:
        1 - update <class name> <id> <attribute name> "<attribute value>
        2 - <class name>.update(<id>, <attribute name>, <attribute value>)
        3 - <class name>.update(<id>, <dictionary representation>)
```

now ask for the create method documentation.

```python
(hbnb) help create
 Create a new instance.
        Usage 🛠:
        1 - create <class name>

        
```

Perfect right? 

Now let's start some examples of console working.

## ⓵ - create , all, count commands

```python
AirBnB_clone$ ./console.py 
(hbnb) all
[]
(hbnb) create Place
492f60f3-ff1e-43c7-bb11-f8407b04dd59
(hbnb) create BaseModel
99f01e9a-99c0-42af-8c10-c35cadee1d8f
(hbnb) BaseModel.count()
1
(hbnb) all
["[Place] (492f60f3-ff1e-43c7-bb11-f8407b04dd59) {'id': '492f60f3-ff1e-43c7-bb11-f8407b04dd59', 'created_at': datetime.datetime(2020, 7, 1, 11, 36, 24, 576486), 'updated_at': datetime.datetime(2020, 7, 1, 11, 36, 24, 576530)}", "[BaseModel] (99f01e9a-99c0-42af-8c10-c35cadee1d8f) {'id': '99f01e9a-99c0-42af-8c10-c35cadee1d8f', 'created_at': datetime.datetime(2020, 7, 1, 11, 36, 30, 773211), 'updated_at': datetime.datetime(2020, 7, 1, 11, 36, 30, 773236)}"]
(hbnb)
```



## ⓶ - update method with an id and show command

```python
(hbnb) update BaseModel 99f01e9a-99c0-42af-8c10-c35cadee1d8f first_name "Betty"
(hbnb) show BaseModel 99f01e9a-99c0-42af-8c10-c35cadee1d8f
[BaseModel] (99f01e9a-99c0-42af-8c10-c35cadee1d8f) {'id': '99f01e9a-99c0-42af-8c10-c35cadee1d8f', 'created_at': datetime.datetime(2020, 7, 1, 11, 36, 30, 773211), 'updated_at': datetime.datetime(2020, 7, 1, 11, 36, 30, 773236), 'first_name': 'Betty'}
(hbnb) Place.update("492f60f3-ff1e-43c7-bb11-f8407b04dd59", "first_name", "John")
(hbnb) show Place 492f60f3-ff1e-43c7-bb11-f8407b04dd59
[Place] (492f60f3-ff1e-43c7-bb11-f8407b04dd59) {'id': '492f60f3-ff1e-43c7-bb11-f8407b04dd59', 'created_at': datetime.datetime(2020, 7, 1, 11, 36, 24, 576486), 'updated_at': datetime.datetime(2020, 7, 1, 11, 36, 24, 576530), 'first_name': 'John'}
```



## ⓷  -  update method with  dictionary representation

```python
(hbnb) BaseModel.update("99f01e9a-99c0-42af-8c10-c35cadee1d8f", {'first_name': "Petter", "age": 45})
(hbnb) show BaseModel 99f01e9a-99c0-42af-8c10-c35cadee1d8f
[BaseModel] (99f01e9a-99c0-42af-8c10-c35cadee1d8f) {'id': '99f01e9a-99c0-42af-8c10-c35cadee1d8f', 'created_at': datetime.datetime(2020, 7, 1, 11, 36, 30, 773211), 'updated_at': datetime.datetime(2020, 7, 1, 11, 36, 30, 773236), 'first_name': 'Petter', 'age': '45'}
```



## ⓸ - destroy and count command

```python
(hbnb) BaseModel.destroy("99f01e9a-99c0-42af-8c10-c35cadee1d8f")
(hbnb) all
["[Place] (492f60f3-ff1e-43c7-bb11-f8407b04dd59) {'id': '492f60f3-ff1e-43c7-bb11-f8407b04dd59', 'created_at': datetime.datetime(2020, 7, 1, 11, 36, 24, 576486), 'updated_at': datetime.datetime(2020, 7, 1, 11, 36, 24, 576530), 'first_name': 'John'}"]
(hbnb) BaseModel.count()
0
(hbnb) quit
AirBnB_clone$
```

## Non interactive mode

```bash
AirBnB_clone$ echo "create User" | ./console.py
(hbnb) 55b76419-6009-4b36-b88a-7c2930283f4a
AirBnB_clone$ echo "show User 55b76419-6009-4b36-b88a-7c2930283f4a" | ./console.py
(hbnb) [User] (55b76419-6009-4b36-b88a-7c2930283f4a) {'id': '55b76419-6009-4b36-b88a-7c2930283f4a', 'created_at': datetime.datetime(2020, 7, 1, 12, 37, 15, 575191), 'updated_at': datetime.datetime(2020, 7, 1, 12, 37, 15, 575237)}
```

## Authors ✏️

- [Juan Sebastian Bueno Marin ](https://github.com/Sebastianbm9507) Software Engineering student at [Holberton School](https://www.holbertonschool.com/co)
- [Nicolas Tobon Alvarez ](https://github.com/NICOLASTOBON) - Software Engineering student at [Holberton School](https://www.holbertonschool.com/co)

 ```
                                                )       \   /      (
                                               /|\      )\_/(     /|\
                      *                       / | \    (/\|/\)   / | \                      *
                      |`.____________________/__|__o____\`|'/___o__|__\___________________.'|
                      |                           '^`    \|/   '^`                          |
                      |                                   V                                 |
                      |                                                                     |
                      |_____   _   _      _      _   _   _  __   __   __   ___    _   _     |
                      |_   _| | | | |    / \    | \ | | | |/ /   \ \ / /  / _ \  | | | |    |
                      | | |   | |_| |   / _ \   |  \| | | ' /     \ V /  | | | | | | | |    |
                      | | |   |  _  |  / ___ \  | |\  | | . \      | |   | |_| | | |_| |    |
                      | |_|   |_| |_| /_/   \_\ |_| \_| |_|\_\     |_|    \___/   \___/     |
                      |                                                                     |
                      |                                 ♥️                                   |
                      |                                                                     |
                      | ._________________________________________________________________. |
                      |'               l    /\ /     \\            \ /\   l                `|
                      *                l  /   V       ))            V   \ l                 *
                                       l/            //                  \I
                               
```


**July/1/2020**  🗓
