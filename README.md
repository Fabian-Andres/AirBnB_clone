# AirBnB clone project

This is a clone project for [Airbnb](https://www.airbnb.com/ "Airbnb") website 

### System requirements

-  [Python3](https://www.python.org/downloads/ "Python3").


## Installation

To carry out the installation of the project, the following steps must be carried out:

### Clone Repository.

To clone the application, run this command on your terminal:

    git clone https://github.com/Fabian-Andres/AirBnB_clone.git

### Project architecture
Within the download you'll find the following directories and files:
```
AirBnB_clone.
├── .gitignore
├── AUTHORS
├── README.md
├── console.py
├── models
│   ├── engine
│   │   ├── __init__.py
│   │   └── file_storage.py
│   ├── __init__.py
│   ├── amenity.py
│   ├── base_model.py
│   ├── city.py
│   ├── place.py
│   ├── review.py
│   ├── state.py
│   └── user.py
└──test
    ├── test_models
    │   │   ├── test_engine
    │   │   ├── __init__.py
    │   │   └── test_console.py
    │   ├── __init__.py
    │   ├── test_amenity.py
    │   ├── test_base_model.py
    │   ├── test_city.py
    │   ├── test_place.py
    │   ├── test_review.py
    │   ├── test_state.py
    │   └── test_user.py
    └── test_console.py
```

### Configure
Follow the instructions to start the project

Being in  `cd /AirBnB_clone`

- Now start the console with

```
$ ./console.py
```


#### Requests of the Console

You can use the console with the followings commands
```
(hbnb) command name_class(arguments)
```
**Or**
```
(hbnb) name_class.command(arguments)
```
### Commands for console
| Command  | Description |
| ------------- | ------------- |
| **help or ?** | Shows the list of commands available. If the input includes a command name, the output is more verbose and restricted to details of that command, when available.  | 
| **Ctrl + d** | It's to exit the program (End of File).  | 
| **quit** |It's to exit the program |
| **create** |  Creates a new instance of class (**BaseModel**, **User**, **State**, **City**, **Amenity**, **Place** and **Review**) | 
| **destroy** | Deletes an instance based on the class name and id. | 
| **all** | Prints all string representation of all instances based or not on the class name.| 
| **update** | Updates an instance based on the class name and id by adding or updating attribute. | 
| **show** | Show an instance based on the class name and id. | 
| **count** | Show the number of instances of a class. | 


Now we will use our **Console** to populate our file.json:


**class_name.create()** 
Return the **id** of the class created:
```
(hbnb) BaseModel.create()
8153f2d6-d7ca-4bd9-ad61-e892d5c560f9
(hbnb) Place.create()
118f7a06-ab4f-4112-bfc4-8cdab1aefe96
(hbnb) User.create()
55baa4fe-3f29-4c06-90e8-9fd2539aff27
(hbnb)
```

**all** 
Return all classes created:

```
(hbnb) all
[BaseModel] (8153f2d6-d7ca-4bd9-ad61-e892d5c560f9) {'created_at': datetime.datetime(2020, 7, 1, 23, 47, 49, 687974), 'updated_at': datetime.datetime(2020, 7, 1, 23, 47, 49, 688029), 'id': '8153f2d6-d7ca-4bd9-ad61-e892d5c560f9'}
[Place] (118f7a06-ab4f-4112-bfc4-8cdab1aefe96) {'created_at': datetime.datetime(2020, 7, 1, 23, 53, 18, 609947), 'updated_at': datetime.datetime(2020, 7, 1, 23, 53, 18, 610732), 'id': '118f7a06-ab4f-4112-bfc4-8cdab1aefe96'}
[User] (55baa4fe-3f29-4c06-90e8-9fd2539aff27) {'created_at': datetime.datetime(2020, 7, 2, 0, 34, 44, 326116), 'id': '55baa4fe-3f29-4c06-90e8-9fd2539aff27', 'updated_at': datetime.datetime(2020, 7, 2, 0, 34, 44, 326152)}
(hbnb) 
```
**class_name.all()** 
Return all classes created by the same type:

```
(hbnb) BaseModel.all()
[BaseModel] (8153f2d6-d7ca-4bd9-ad61-e892d5c560f9) {'created_at': datetime.datetime(2020, 7, 1, 23, 47, 49, 687974), 'updated_at': datetime.datetime(2020, 7, 1, 23, 47, 49, 688029), 'id': '8153f2d6-d7ca-4bd9-ad61-e892d5c560f9'}
(hbnb) 
```

**class_name.show(id)** 
Return specific class by id:

```
(hbnb) BaseModel.show("8153f2d6-d7ca-4bd9-ad61-e892d5c560f9")
[BaseModel] (8153f2d6-d7ca-4bd9-ad61-e892d5c560f9) {'updated_at': datetime.datetime(2020, 7, 1, 23, 47, 49, 688029), 'created_at': datetime.datetime(2020, 7, 1, 23, 47, 49, 687974), 'id': '8153f2d6-d7ca-4bd9-ad61-e892d5c560f9'}
(hbnb) 
```

**class_name.update(id, attribute_name, attribute_value)** 
Change the parameters for specific class to id:

```
(hbnb) User.show("55baa4fe-3f29-4c06-90e8-9fd2539aff27")
[User] (55baa4fe-3f29-4c06-90e8-9fd2539aff27) {'created_at': datetime.datetime(2020, 7, 1, 23, 47, 49, 687974), 'updated_at': datetime.datetime(2020, 7, 1, 23, 47, 49, 688029), 'id': '55baa4fe-3f29-4c06-90e8-9fd2539aff27'}
(hbnb) User.update("55baa4fe-3f29-4c06-90e8-9fd2539aff27", "first_name", "John")
(hbnb) User.show("55baa4fe-3f29-4c06-90e8-9fd2539aff27")
[User] (55baa4fe-3f29-4c06-90e8-9fd2539aff27) {'first_name,': 'John', 'id': '55baa4fe-3f29-4c06-90e8-9fd2539aff27', 'updated_at': datetime.datetime(2020, 7, 2, 0, 26, 11, 124897), 'created_at': datetime.datetime(2020, 7, 1, 23, 47, 49, 687974)}
(hbnb) 
```

**class_name.update(id, dictionary_representation)** 
Change the parameters from dictionary for a specific class to id:

```
(hbnb) User.show("55baa4fe-3f29-4c06-90e8-9fd2539aff27")
[User] (55baa4fe-3f29-4c06-90e8-9fd2539aff27) {'first_name,': 'John', 'id': '55baa4fe-3f29-4c06-90e8-9fd2539aff27', 'updated_at': datetime.datetime(2020, 7, 2, 0, 26, 11, 124897), 'created_at': datetime.datetime(2020, 7, 1, 23, 47, 49, 687974)}
(hbnb) User.update("55baa4fe-3f29-4c06-90e8-9fd2539aff27", {'first_name': "Bob", "age": 89})
(hbnb) User.show("55baa4fe-3f29-4c06-90e8-9fd2539aff27")
[User] (55baa4fe-3f29-4c06-90e8-9fd2539aff27) {'first_name,': 'Bob', 'age': 89, 'id': '55baa4fe-3f29-4c06-90e8-9fd2539aff27', 'first_name': 'Bob', 'updated_at': datetime.datetime(2020, 7, 2, 0, 31, 28, 164056), 'created_at': datetime.datetime(2020, 7, 1, 23, 47, 49, 687974)}
```

**class_name.destroy(id)** 
Delete specific class by id:

```
(hbnb) BaseModel.count()
1
(hbnb) BaseModel.destroy("8153f2d6-d7ca-4bd9-ad61-e892d5c560f9")
(hbnb) BaseModel.count()
0
(hbnb) BaseModel.show("8153f2d6-d7ca-4bd9-ad61-e892d5c560f9")
** no instance found **
(hbnb) 
```

### Authors
Manuel Puerta Villa [:octocat:](https://github.com/Manuelpv17 "Github") 
Fabian Andres Riascos [:octocat:](https://github.com/fabian-andres "Github")
