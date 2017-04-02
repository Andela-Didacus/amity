
# **AMITY ROOM ALLOCATION SYSTEM**
[![Build Status](https://travis-ci.org/Andela-Didacus/amity.svg?branch=develop)](https://travis-ci.org/Andela-Didacus/amity) [![Code Health](https://landscape.io/github/Andela-Didacus/amity/master/landscape.svg?style=flat)](https://landscape.io/github/Andela-Didacus/amity/master)

The amity room allocation program is a room allocation system for one of Andela’s facilities called Amity. The main aim of the program being to easen the creating and allocation of rooms.
The system allows the user to create rooms, allocate rooms, reallocate rooms, print allocations among other features.

# **Getting Started**
The program has been fully developed using **Python** and some of its libraries, while the database implementation uses **SQLITE3**
* Python 2.7
* SQLITE3
* Visual Studio

# **Prerequisites**
Below are some of the basic requirements to run the program:
* Python should be installed in your computer, if not do so here _[Python Download](https://tutorial.djangogirls.org/en/python_installation/)_
* Git should be installed in your computer, if not do so here, _[Git Download](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwjxsYyak8zRAhWsI8AKHR9YDL4QFggfMAA&url=https%3A%2F%2Fgit-scm.com%2Fdownloads&usg=AFQjCNHZLDrEFiZHXrz1JGq57NFHFrcfkA&sig2=4ht1GzU2s-G7fLM3fuDxYA)_
* A stable internet connection is recommended
* SQLITE3 should be installed, if not, do so on _[SQLITE3](github.com/sqlitebrowser/sqlitebrowser/releases)_

# **Installation**
Follow the following steps to succesfully _**install**_ the program:
1. Run your _Git Bash_ program and enter **`$ cd `** to place your directory in into desktop folder.
2. Type **`$ git clone https://github.com/Andela-Didacus/amity.git`** to clone the repository to your desktop folder.
3. open command prompt and enter **`$ pip install -r requirements.txt`** to install the required packages to run the program.
4. Enter **`$ cd desktop\amity`** . 
5. Finally enter **`$ python app.py -i`** to run the program.

## **Amity System**

<img width="1280" alt="screen shot 2017-03-19 at 11 26 23 pm" src="https://cloud.githubusercontent.com/assets/25657649/24084491/18253d20-0cfc-11e7-8297-9fe93379306b.png">

**Room Creation and Person Allocation**
<img width="1280" alt="screen shot 2017-03-19 at 11 39 39 pm" src="https://cloud.githubusercontent.com/assets/25657649/24084558/629d143a-0cfd-11e7-831d-7004edf4e200.png">

**Printing Allocations**
<img width="1200" alt="screen shot 2017-03-19 at 11 44 05 pm" src="https://cloud.githubusercontent.com/assets/25657649/24084604/fbbaebec-0cfd-11e7-9c1b-907d3d51f973.png">

## *Amity Commands*

1. `create_room <room_type> <room_name>...` - Creates rooms either office or living space. Multipla rooms of the same type can also be created using this command

2. `add_person <person_name> <role> [--accomodate=accomodation]`- adds the person to Amity and assigns an office and living space if specified

3. `reallocate_person <person_first_name> <person_last_name> <new_room_name>` - Reallocates person to a new room`.

4. `load_people <file_name>` - loads people to rooms from a text file.`

5. `print_unallocated [--o=filename]` - Prints a list of unallocated people to the screen. Specifying the --o option here outputs the information to the txt file provided and has an option to allocate all unallocated persons rooms if any available

6. `print_allocations [--o=filename]`  - Prints a list of allocations onto the screen. Specifying the optional --o option here outputs the registered allocations to a txt file.

7. `print_available_rooms` - prints a list of all the available rooms and available space

8. `print_rooms`- prints all the amity rooms and the number of occupants
9. `print_room <room_name>` - Prints  the names and role of persons in the room.

10. `save_state [--db=sqlite_database]` - Persists all the data stored in the app to a SQLite database. Specifying the --db parameter explicitly stores the data in the `sqlite_database` specified.

11. `load_state [--db=sqlite_database]` - Loads data from a database into the application.

12. `exit` - quits the application

## Running the tests

Tests on this project are done using python nose package. To run the tests enter the following command in your terminal in the amity directory.
`nosetests --with-coverage` or `test.py`
## Authors

* **Didacus Odhiambo** -- [Didacus Odhiambo](https://github.com/Andela-Didacus/amity)




