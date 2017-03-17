import sys
import sqlite3
import datetime
import time
from termcolor import cprint,colored

def create_tables():
    conn = sqlite3.connect('amity.db')
    c = conn.cursor()

    print "successfully connected"

    conn.execute('''CREATE TABLE  rooms    
        (ID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
       ROOM_NAME     TEXT    UNIQUE NOT NULL,
       ROOM_TYPE     TEXT    NOT NULL,
       MAX_NUMBER    INT     NOT NULL,
       NUMBER_OF_OCCUPANTS INT  NOT NULL,
       TIMESTAMP     TEXT    NOT NULL )''')

    print ("Table successfully created")

    conn.execute('''CREATE TABLE amity      
       (ID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
      FULL_NAME     TEXT    UNIQUE  NOT NULL,
      ROLE          TEXT    NOT NULL,
      OFFICE        TEXT    NOT NULL,
      LIVING_SPACE    TEXT    NOT NULL,
      TIMESTAMP       TEXT    NOT NULL
      )''')
    print "Table successfully created"

    conn.commit()  # commits the current transaction to enable visibility of changes to other database connections
    c.close()

def create_room(room_name, room_type, max_number,num_of_occupants, timestamp):
    conn = sqlite3.connect('amity.db')
    c = conn.cursor()
    try:
        c.execute(" INSERT INTO rooms (ROOM_NAME, ROOM_TYPE, MAX_NUMBER, NUMBER_OF_OCCUPANTS, TIMESTAMP ) VALUES(?,?,?,?,?)",
              (room_name, room_type, max_number, num_of_occupants, timestamp))

        conn.commit()

        c.close()

        # return "ROOM %s SUCCESSFULLY CREATED!!" %room_name

    except:
        print colored("ROOM ALREADY EXISTS in THE DATABASE!!! USE ANOTHER NAME", "red")
        print colored("---------------------------------------------------------", "red")
        return "Error! room name already exists!!"
    
def update_room(num_of_occupants,room_name):
    conn = sqlite3.connect("amity.db")
    c = conn.cursor()
    c.execute("UPDATE rooms SET NUMBER_OF_OCCUPANTS = '%s' WHERE ROOM_NAME = '%s' " %
              (num_of_occupants, room_name))
    conn.commit()
    c.close()
    return "SUCCESS"
    
def add_person(full_name, role, office, living_space, timestamp):
    try:
        conn = sqlite3.connect('amity.db')
        c = conn.cursor()

        c.execute(" INSERT INTO amity (FULL_NAME, ROLE, OFFICE, LIVING_SPACE, TIMESTAMP ) VALUES(?,?,?,?,?)",
                (full_name, role, office, living_space, timestamp))

        conn.commit()

        c.close()
    except:
        print colored("PERSON ALREADY EXISTS IN THE DATABASE!!! USE ANOTHER NAME", "red")
        print colored("---------------------------------------------------------", "red")
        return "Error! room name already exists!!"

     