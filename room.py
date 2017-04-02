import sys
from abc import ABCMeta, abstractmethod


class Room(object):
    __metaclass__ = ABCMeta

    def __init__(self, room_name, timestamp):
        self.room_name = room_name
        self.timestamp = timestamp

    @abstractmethod
    def get_name(self):
        print self.room_name


class Office(Room):

    def __init__(self, room_name, timestamp):
        self.max_number = 6
        self.num_of_occupants = 0
        self.room_type = "OFFICE"
        super(Office, self).__init__(room_name, timestamp)

    def get_name(self):
        print "Name: %s" % self.room_name


class Living_space(Room):

    def __init__(self, room_name, timestamp):
        self.max_number = 4
        self.num_of_occupants = 0
        self.room_type = "LIVING SPACE"
        super(Living_space, self).__init__(room_name, timestamp)

    def get_name(self):
        print "Name: %s" % self.room_name
