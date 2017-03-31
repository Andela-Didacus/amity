import sys
from abc import ABCMeta, abstractmethod


class Room(object):
    __metaclass__ = ABCMeta

    def __init__(self, room_name, room_type, timestamp):
        self.room_name = room_name
        self.room_type = room_type
        self.timestamp = timestamp

    @abstractmethod
    def get_name(self):
        print self.full_name


class Office(Room):

    def __init__(self, room_name, room_type, timestamp):
        self.max_number = 6
        self.num_of_occupants = 0
        super(Office, self).__init__(room_name, room_type, timestamp)

    def get_name(self):
        print "Name: %s" % self.full_name


class Living_space(Room):

    def __init__(self, room_name, room_type, timestamp):
        self.max_number = 4
        self.num_of_occupants = 0
        self.room_name = room_name
        super(Living_space, self).__init__(room_name, room_type, timestamp)

    def get_name(self):
        print "Name: %s" % self.full_name
