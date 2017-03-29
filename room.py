import sys
import datetime
from abc import ABCMeta, abstractmethod
from termcolor import colored
import time
from amity import Amity


class Room(object):
    __metaclass__ = ABCMeta

    @classmethod
    def print_room(self):
        pass
    
    
class Office(Room):

    def __init__(self, room_name, room_type, timestamp):
        self.room_name = room_name
        self.room_type = room_type
        self.timestamp = timestamp
        self.max_number = 6
        self.num_of_occupants = 0
        self.room_name = room_name


class Living_space(Room):

    def __init__(self, room_name, room_type, timestamp):
        self.room_name = room_name
        self.room_type = room_type
        self.timestamp = timestamp
        self.max_number = 4
        self.num_of_occupants = 0
        self.room_name = room_name


def create_room(room_name, room_type):
    if type(room_name) != str or type(room_type) != str or room_name.isalpha() == False:
        print colored("\nINVALID NAME INPUT, NAME CANNOT BE A NUMBER\n", "red")
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
                Amity.office_details.append(room_name)
                Amity.offices.append(room_name.room_name)
            elif room_type == "LIVING SPACE":
                room_name = Living_space(room_name, room_type, timestamp)
                Amity.living_space_details.append(room_name)
                Amity.living_spaces.append(room_name.room_name)
            else:
                print colored("\nINVALID INPUT!! ROOM CAN ONLY BE OFFICE OR \ LIVING SPACE\n", "red")
                return "INVALID ROOM TYPE INPUT!!"
            printer_room(room_name.room_name, room_name.room_type, room_name.timestamp)
            return "ROOM SUCCESSFULLY CREATED IN AMITY"

def printer_room(room_name, room_type, timestamp): #Helper function
    print colored("\n*--* AMITY *--*", "cyan")
    print colored("     ----------      ", "cyan")
    print colored("ROOM_NAME: %s"%room_name , "cyan")
    print colored("ROOM TYPE: %s"%room_type , "cyan")
    print colored("DATE CREATED: %s"%timestamp , "cyan")
    print colored("*--*--*--*--*--*--*--*--*--*\n", "cyan")

create_room("dojo", "office")
