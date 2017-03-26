class Rooms(object):
    offices = []
    living_spaces = []
    rooms = [offices, living_spaces]


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
        
        