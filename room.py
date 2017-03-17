class Room:
    offices = []
    living_spaces = []
    rooms = [offices,living_spaces]
    allocated_rooms = []
    allocated_persons= []
    def __init__(self, room_name, room_type, timestamp):
        self.room_name = room_name
        self.room_type = room_type
        self.timestamp = timestamp
        self.num_of_occupants = 0

        if self.room_type == "OFFICE":
            self.max_number = 6
            # database.create_room(self.room_name, "OFFICE",self.max_number, self.timestamp)

        elif self.room_type == "LIVING SPACE":
            self.max_number = 4
            # database.create_room(room_name, "LIVING SPACE", self.max_number, self.timestamp)


        else:
            print "Invalid Input"