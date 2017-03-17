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

def create_room(room_name):
    if type(room_name) != str:
        print "INVALID NAME INPUT"
        return "INVALID input!!"
    else:
        room_name = room_name.upper()
        if room_name in Amity.offices or room_name in Amity.living_spaces:
            print colored("ROOM NAME ALREADY EXISTS!! USE ANOTHER NAME", "red")
            print
            # return "ROOM EXISTS!"
        else:
            day = time.time()
            timestamp = str(datetime.datetime.fromtimestamp(day).strftime("%y-%m-%d"))
            room_types = ["LIVING SPACE", "OFFICE"]
            room_type = random.choice(room_types)
            print room_type
            print room_name

            if room_type == "OFFICE":
                database.create_room(room_name, room_type, 6, 0, timestamp)
                room_name = Room(room_name, room_type, timestamp)
                Room.offices.append(room_name)
                Amity.offices.append(room_name.room_name)
            elif room_type == "LIVING SPACE":
                database.create_room(room_name, room_type, 4, 0, timestamp)
                room_name = Room(room_name, room_type, timestamp)
                Room.living_spaces.append(room_name)
                Amity.living_spaces.append(room_name.room_name)
            else:
                print colored("INVALID INPUT! ENTER 1 OR 2", "red")
                print
                return "INVALID ROOM TYPE INPUT!!"

    print colored("*--* AMITY *--*", "cyan")
    print colored("     -----      ", "cyan")
    print "ROOM_NAME: %s"%room_name.room_name
    print "ROOM TYPE: %s"%room_name.room_type
    print "DATE CREATED: %s"%room_name.timestamp
    print colored("*--*--*--*--*--*--*--*", "cyan")
    return "ROOM SUCCESSFULLY CREATED IN AMITY" 

def print_rooms():
    
    print colored("<== AMITY ROOMS ==>", "blue")
    print colored("    -----------    ", "blue")
    if (len(Room.rooms[0]) == 0) and (len(Room.rooms[1]) == 0):
        print colored("NO ROOMS AVAILABLE IN AMITY", "red")
        return "EMPTY"
    else:
        for room_type in Room.rooms:
            for room in room_type:
                print "ROOM NAME: %s"%room.room_name
                print "ROOM TYPE: %s"%room.room_type
                print "NUMBER OF OCCUPANTS: %s"%room.num_of_occupants
                print colored("------------------------------", "blue")
                        
        return "SUCCESS!!" 
