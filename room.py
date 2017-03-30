import sys
import datetime
from abc import ABCMeta, abstractmethod
from termcolor import colored
import time



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



