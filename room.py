import sys
import datetime
import time
from termcolor import colored

from amity import Amity


class Rooms(object):
    pass


class Office(Rooms):
    def __init__(self, room_name, room_type, timestamp):
        self.room_name = room_name
        self.room_type = room_type
        self.timestamp = timestamp
        self.num_of_occupants = 0
        self.max_number = 6

class Living_space(Rooms):
    def __init__(self, room_name, room_type, timestamp):
        self.room_name = room_name
        self.room_type = room_type
        self.timestamp = timestamp
        self.num_of_occupants = 0
        self.max_number = 4
        
def create_room(room_name, room_type):
    if type(room_name) != str or type(room_type) != str or (room_name.isalpha() == False):
        print colored("\nNOTICE!! INVALID NAME INPUT, NAME CANNOT BE NUMBER\n", "red")
        return "INVALID input!!"

    else:
        room_name = room_name.upper()
        room_type = room_type.upper()
        if room_type == "LIVING_SPACE":
            room_type = "LIVING SPACE"
        else:
            pass
        if room_name in Amity.offices or room_name in Amity.living_spaces:
            print colored("\nROOM NAME ALREADY EXISTS!! USE ANOTHER NAME\n", "red")
            return "ROOM EXISTS!"
        else:
            day = time.time()
            timestamp = str(datetime.datetime.fromtimestamp(day).strftime("%y-%m-%d"))
            if room_type == "OFFICE":
                room_name = Office(room_name, room_type, timestamp)
                Amity.offices.append(room_name.room_name)
                Amity.office_details.append(room_name)
                printer_room(room_name.room_name, room_name.room_type, room_name.timestamp)
                return "OFFICE SUCCESSFULY CREATED SUCCESSFULLY CREATED!!"
            elif room_type == "LIVING SPACE":
                room_name = Living_space(room_name, room_type, timestamp)
                Amity.living_spaces.append(room_name.room_name)
                Amity.living_space_details.append(room_name)
                printer_room(room_name.room_name, room_name.room_type, room_name.timestamp)
                return "LIVING SPACE SUCCESSFULY CREATED SUCCESSFULLY CREATED!!"
            else:
                print colored("\nINVALID INPUT!! ROOM CAN ONLY BE OFFICE OR LIVING SPACE\n", "red")
                return "INVALID ROOM TYPE INPUT!!"
            
def printer_room(room_name, room_type, timestamp):
    print colored("\n*--* AMITY *--*", "cyan")
    print colored("     -----      ", "cyan")
    print "ROOM_NAME: %s"%room_name
    print "ROOM TYPE: %s"%room_type
    print "DATE CREATED: %s"%timestamp
    print colored("*--*--*--*--*--*--*--*\n", "cyan")

create_room("dida", "office")
print Amity.all_rooms_details
print Amity.offices