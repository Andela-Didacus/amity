import pickle
import sqlite3
from amity import Amity

def save_state(database_name):
    db_connect = sqlite3.connect(database_name)
    conn = db_connect.cursor()

    conn.execute("CREATE TABLE IF NOT EXISTS all_room_data "
                    "(dataID INTEGER PRIMARY KEY UNIQUE, "
                    "offices TEXT, living_spaces TEXT, rooms TEXT, office_details TEXT, living_space_details TEXT, all_rooms_details TEXT)")
    offices = pickle.dumps(Amity.offices)
    living_spaces = pickle.dumps(Amity.living_spaces)
    rooms = pickle.dumps(Amity.rooms)
    office_details = pickle.dumps(Amity.office_details)
    living_space_details = pickle.dumps(Amity.living_space_details)
    all_rooms_details = pickle.dumps(Amity.all_rooms_details)

    conn.execute("INSERT INTO all_room_data VALUES (null, ?, ?, ?, ?, ?, ?);",
                    (offices, living_spaces, rooms, office_details, living_space_details, all_rooms_details))

    db_connect.commit()
    db_connect.close() 

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

    db_connect.commit()
    db_connect.close()            
