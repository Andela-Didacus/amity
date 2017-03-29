from termcolor import colored


class Amity(object):
    offices = []
    living_spaces = []
    rooms = [offices,living_spaces]
    fellows = []
    staff = []
    persons = [staff,fellows]
    unallocated_staff = []
    unallocated_fellows = []
    allocated_rooms = []
    allocated_persons = []
    available_living_spaces = []
    available_offices = []
    office_details = []
    living_space_details = []
    all_rooms_details = [office_details, living_space_details]

    @staticmethod
    def print_all_rooms():
        print colored("\n<== AMITY ROOMS ==>", "blue")
        print colored("    -----------    ", "blue")
        if (len(Amity.office_details) == 0) and (len(Amity.living_space_details) == 0):
            print colored("NO ROOMS AVAILABLE IN AMITY", "red")
            return "EMPTY"
        else:
            for room_type in Amity.all_rooms_details:
                for room in room_type:
                    print "ROOM NAME: %s"%room.room_name
                    print "ROOM TYPE: %s"%room.room_type
                    print "NUMBER OF OCCUPANTS: %s"%room.num_of_occupants
                    print "DATE CREATED: %s"%room.timestamp
                    print colored("------------------------------", "blue")
      
            return "SUCCESS!!" 

    @staticmethod
    def print_available_space():
        print colored("\n<== AVAILABLE AMITY ROOMS ==>", "green")
        print colored("    ---------------------   ", "green")
        clear()
        check_rooms()
        if (len(Amity.available_living_spaces) == 0) and (len(Amity.available_offices) == 0):
            print colored(" NO ROOMS AVAILABLE IN AMITY", "red")
            print colored("------------------------------", "green")
            return "EMPTY"
        else:
            for room in Amity.living_space_details:
                if room.num_of_occupants < room.max_number:
                    print "ROOM NAME: %s"%room.room_name
                    print "ROOM TYPE: %s"%room.room_type
                    print "AVAILABLE SPACE: %s"%(room.max_number - room.num_of_occupants)
                    print colored("------------------------------", "green")
            for room in Amity.office_details:
                if room.num_of_occupants < room.max_number:
                    print "ROOM NAME: %s"%room.room_name
                    print "ROOM TYPE: %s"%room.room_type
                    print "AVAILABLE SPACE: %s"%(room.max_number - room.num_of_occupants)
                    print colored("------------------------------", "green")
            
            clear() 
            return "SUCCESS!!"

    @staticmethod
    def print_room(room_name):
        if (type(room_name) != str) or (len(room_name) == 0) or (room_name.isalpha() == False):
            print colored("\nINVALID INPUT!! ROOM NAME CANNOT BE EMPTY OR A NON-STRING!!\n", "red")
            return "INVALID TYPE INPUT!!"

        else:
            room_name = room_name.upper()
            if room_name not in Amity.offices and room_name not in Amity.living_spaces:
                print colored("\nINVALID INPUT!! ROOM DOES NOT EXIST\n", "red")
                return "INVALID ROOM INPUT!! "
            else:
                if room_name not in Amity.allocated_rooms:
                    print colored("\nINVALID INPUT!! ROOM DOES HAS NOT BEEN ALLOCATED\n", "red")
                    return "INVALID ROOM INPUT!!"
                else:
                    print_room_persons(room_name)
                    return "SUCCESS!!"


def check_rooms(): #helper function for checking available rooms
    for room in Amity.office_details:
        if room.num_of_occupants < room.max_number:
            Amity.available_offices.append(room.room_name)

    for room in Amity.living_space_details:
        if room.num_of_occupants < room.max_number:
            Amity.available_living_spaces.append(room.room_name)

def clear():  #helper function for clearing available rooms list
    del Amity.available_living_spaces[:]
    del Amity.available_offices[:]

def print_room_persons(room_name):#helper function to print allocated people in a room
    print colored("*--*--* %s ALLOCATIONS *--*--*"%room_name, "blue")
    print colored("     ------------------------    ", "blue")
    for person in Amity.allocated_persons:
        if person.office == room_name:
            print "-----------------------------------"
            print "NAME: %s"%person.full_name
            print "ROLE: %s"%person.role
            print "-----------------------------------\n" 
        elif person.living_space == room_name:
            print "-----------------------------------"
            print "NAME: %s"%person.full_name
            print "ROLE: %s"%person.role
            print "-----------------------------------\n" 