# AirBnB_clone

Repository for ALX SE's `0x00. AirBnB clone - The console` project.

---
This project is the first part of a multi-part building process, whose final product will be a clone
\
of the popular accommodation-sharing application, AirBnB.
\
\
In this first part, different models in the application are controlled (created, read, updated, and
\
deleted) via the command-line a.k.a the "console".
\
This first revision also handles permanent storage via the use of .json files for serializing and
\
deserializing objects for reuse.

## Using the console

One only needs to run the file `console.py` in order to start interacting with the application.
\
This interaction involves creating, reading, updating and deleting all sorts of application-specific
\
objects like users, states, cities, places, reviews, and amenities.
\
All changes made to the objects are also reflected in the `file.json` file, which is the permanent
\
storage for this first iteration of the project.

## Demo (basic CRUD actions)

**Note**: The demo uses a `User` as the object being manipulated, but the commands shown also apply to
\
other objects as well.

### Starting the console

```sh
$ ./console.py
(hbnb) 
```

- Viewing all objects present in storage (there are none at the moment, so an empty list is show)

```sh
(hbnb) all
[]
(hbnb) 
```

- Furthermore, because no objects exist, no json file is present in the filesystem

```sh
$ cat file.json; echo ""
cat: file.json: No such file or directory
```

---

### `Creating` an object

After an object is created, a unique id that represents that object is printed on
\
the console, and the object's information is immediately stored in the json file.
\
The general syntax for creating any object is:
\
`create <class name>`

```sh
(hbnb) create User
5e3b660e-ef79-4f57-8438-311ff6809b6d
(hbnb) 
```

The contents of the now created json file can be verified

```sh
$ cat file.json; echo ""
{"User.5e3b660e-ef79-4f57-8438-311ff6809b6d": {"email": "", "password": "", "first_name": "", "last_name": "", "id": "5e3b660e-ef79-4f57-8438-311ff6809b6d", "created_at": "2024-03-12T10:03:04.945342", "updated_at": "2024-03-12T10:03:04.945372", "__class__": "User"}}
```

---

### `Reading` an object's information

One need not open the json file just to verify that created objects do, in fact, exist in storage.
\
\
In stead, a `show` command achieves the same result with the following syntax:
\
`show <class name> <object's id>`

```sh
(hbnb) show User 5e3b660e-ef79-4f57-8438-311ff6809b6d
[User] (5e3b660e-ef79-4f57-8438-311ff6809b6d) {'email': '', 'password': '', 'first_name': '', 'last_name': '', 'id': '5e3b660e-ef79-4f57-8438-311ff6809b6d', 'created_at': datetime.datetime(2024, 3, 12, 10, 3, 4, 945342), 'updated_at': datetime.datetime(2024, 3, 12, 10, 3, 4, 945372)}
```

**Note**: In permanent storage, all time-related attributes are stored in string format.
\
It is only when the objects are read from storage into memory, that these are converted back to their
\
`datetime` representations.
\
Furthermore, the `__class__` attribute only exists while the object is in permanent storage.

---

### `Updating` an object's information

And objects attributes can be updated with the `update` command, whose syntax is as follows
\
`update <class name> <object's id> <attribute to update> "<new value>"`

```sh
(hbnb) show User 5e3b660e-ef79-4f57-8438-311ff6809b6d
[User] (5e3b660e-ef79-4f57-8438-311ff6809b6d) {'email': '', 'password': '', 'first_name': '', 'last_name': '', 'id': '5e3b660e-ef79-4f57-8438-311ff6809b6d', 'created_at': datetime.datetime(2024, 3, 12, 10, 3, 4, 945342), 'updated_at': datetime.datetime(2024, 3, 12, 10, 3, 4, 945372)}
(hbnb) update User 5e3b660e-ef79-4f57-8438-311ff6809b6d first_name "Mizyu"
(hbnb) show User 5e3b660e-ef79-4f57-8438-311ff6809b6d
[User] (5e3b660e-ef79-4f57-8438-311ff6809b6d) {'email': '', 'password': '', 'first_name': 'Mizyu', 'last_name': '', 'id': '5e3b660e-ef79-4f57-8438-311ff6809b6d', 'created_at': datetime.datetime(2024, 3, 12, 10, 3, 4, 945342), 'updated_at': datetime.datetime(2024, 3, 12, 10, 3, 4, 945372)}
(hbnb) 
```

As expected, the contents of the json file are also updated accordingly

```sh
$ cat file.json; echo ""
{"User.5e3b660e-ef79-4f57-8438-311ff6809b6d": {"email": "", "password": "", "first_name": "Mizyu", "last_name": "", "id": "5e3b660e-ef79-4f57-8438-311ff6809b6d", "created_at": "2024-03-12T10:03:04.945342", "updated_at": "2024-03-12T10:03:04.945372", "__class__": "User"}}
```

---

### `Deleting` an object

An existing object can be deleted with the `destroy` from the application with the syntax:
`destroy <class name> <object's id>`

```sh
(hbnb) all
["[User] (5e3b660e-ef79-4f57-8438-311ff6809b6d) {'email': '', 'password': '', 'first_name': 'Mizyu', 'last_name': '', 'id': '5e3b660e-ef79-4f57-8438-311ff6809b6d', 'created_at': datetime.datetime(2024, 3, 12, 10, 3, 4, 945342), 'updated_at': datetime.datetime(2024, 3, 12, 10, 3, 4, 945372)}"]
(hbnb) destroy User 5e3b660e-ef79-4f57-8438-311ff6809b6d
(hbnb) all
[]
(hbnb) show User 5e3b660e-ef79-4f57-8438-311ff6809b6d
** no instance found **
(hbnb)
```

Yes, the json file is also empty!

```sh
$ cat file.json; echo ""
{}
```
