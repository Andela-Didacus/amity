import pickle
import sqlite3
from termcolor import colored

from person import create_person, Persons
from amity import Amity


def save_state(database_name):
    db_connect = sqlite3.connect(database_name)
    conn = db_connect.cursor()

    conn.execute("CREATE TABLE IF NOT EXISTS all_room_data "
                    "(dataID INTEGER PRIMARY KEY UNIQUE, "
                    "offices TEXT, living_spaces TEXT, rooms TEXT, office_details TEXT, living_space_details TEXT, all_rooms_details TEXT, fellows TEXT, staff TEXT, persons TEXT, unallocated_staff TEXT, unallocated_fellows TEXT, allocated_rooms TEXT, allocated_persons TEXT)")
    offices = pickle.dumps(Amity.offices)
    living_spaces = pickle.dumps(Amity.living_spaces)
    rooms = pickle.dumps(Amity.rooms)
    office_details = pickle.dumps(Amity.office_details)
    living_space_details = pickle.dumps(Amity.living_space_details)
    all_rooms_details = pickle.dumps(Amity.all_rooms_details)
    fellows = pickle.dumps(Amity.fellows)
    staff = pickle.dumps(Amity.staff)
    persons = pickle.dumps(Amity.persons)
    unallocated_staff = pickle.dumps(Amity.unallocated_staff)
    unallocated_fellows = pickle.dumps(Amity.unallocated_fellows)
    allocated_rooms = pickle.dumps(Amity.allocated_rooms)
    allocated_persons = pickle.dumps(Amity.allocated_persons)


    conn.execute("INSERT INTO all_room_data VALUES (null, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? );",
                    (offices, living_spaces, rooms, office_details, living_space_details, all_rooms_details, fellows, staff, persons, unallocated_staff, unallocated_fellows, allocated_rooms, allocated_persons))

    db_connect.commit()
    db_connect.close() 

    print colored("\nDATABASE SUCCESSFULLY SAVED\n", "blue")
    return "SUCCESSFULLY SAVED"

def load_state(database_name):
    db_connect = sqlite3.connect(database_name)
    conn = db_connect.cursor()   
    conn.execute("SELECT * FROM all_room_data WHERE dataID = (SELECT MAX(dataID) FROM all_room_data)")
    data = conn.fetchone()

    Amity.offices = pickle.loads(data[1])
    Amity.living_spaces = pickle.loads(data[2])
    Amity.rooms = pickle.loads(data[3])
    Amity.office_details = pickle.loads(data[4])
    Amity.living_space_details = pickle.loads(data[5])
    Amity.all_rooms_details = pickle.loads(data[6])
    Amity.fellows = pickle.loads(data[7])
    Amity.staff = pickle.loads(data[8])
    Amity.persons = pickle.loads(data[9])
    Amity.unallocated_staff = pickle.loads(data[10])
    Amity.unallocated_fellows = pickle.loads(data[11])
    Amity.allocated_rooms = pickle.loads(data[12])
    Amity.allocated_persons = pickle.loads(data[13])


    db_connect.commit()
    db_connect.close()    
    print colored("\nDATABASE SUCCESSFULLY LOADED\n", "blue")
    return "SUCCESSFULLY LOADED"        

def load_people():
    with open("people.txt") as f:
        content = f.read().splitlines()
    for person in content:
        length = len(person.split(" "))
        if length == 4:
            first_name, last_name, role, accomodation_status = person.split(' ')
            create_person(first_name, last_name, role, accomodation_status)
        if length == 3:
            first_name, last_name, role = person.split(' ')
            create_person(first_name, last_name, role, "N")

    return "PERSONS SUCCESSFULLY LOADED"