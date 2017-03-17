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

def print_available_rooms():
    print colored("<== AVAILABLE AMITY ROOMS ==>", "green")
    print colored("    ---------------------   ", "green")
    if (len(Room.rooms[0]) == 0) and (len(Room.rooms[1]) == 0):
        print colored(" NO ROOMS AVAILABLE IN AMITY", "red")
        print colored("------------------------------", "green")
        return "EMPTY"
    else:
        for room_type in Room.rooms:
            for room in room_type:
                if room.num_of_occupants < room.max_number:
                    print "ROOM NAME: %s"%room.room_name
                    print "ROOM TYPE: %s"%room.room_type
                    print "NUMBER OF OCCUPANTS: %s"%room.num_of_occupants
                    print colored("------------------------------", "green")
                        
        return "SUCCESS!!"

def allocate_room(full_name, role, accomodation_status, timestamp):
    if role == "STAFF" and accomodation_status == "Y":
        living_space = "----"
        for room in Room.offices:
            if room.num_of_occupants < room.max_number:
                office = room.room_name
                first_name, last_name = full_name.split(" ")
                database.add_person(full_name, role, office, living_space, timestamp)
                first_name = Amity(full_name, role, office, living_space)
                Room.allocated_persons.append(first_name)
                Room.allocated_rooms.append(office)
                room.num_of_occupants += 1
                database.update_room(room.num_of_occupants, room.room_name)
                print "STAFF ARE NOT ALLOWED LIVING SPACES!!"
                break
        else:
            print
            Amity.unallocated_staff.append(full_name + " " + "STAFF" + " " + "Y" + " " + "N") 
            print colored("NO ROOMS AVAILABLE!! ADDED TO WAITING LIST", "red")
            print colored("------------------------------------------", "red")
            return "NO ROOMS AVAILABLE!!"
            
        print colored("*--*--*STAFF SUCCESSFULLY ADDED*--*--*", "yellow")
        print colored("       ------------------------        ", "yellow")
        print "NAME: %s"%full_name
        print "ROLE: %s"%role
        print "OFFICE: %s"%office
        print colored("---------------------------------------", "yellow")
        print 
        return "ROOM SUCCESSFULLY ASSIGNED!!"

    elif role == "STAFF" and accomodation_status == "N":
        living_space = "----"
        for room in Room.offices:
            if room.num_of_occupants < room.max_number:
                office = room.room_name
                first_name, last_name = full_name.split(" ")
                database.add_person(full_name, role, office, living_space, timestamp)
                first_name = Amity(full_name, role, office, living_space)
                Room.allocated_persons.append(first_name)
                Room.allocated_rooms.append(office)
                room.num_of_occupants += 1
                database.update_room(room.num_of_occupants, room.room_name)
                break
        else:
            print 
            Amity.unallocated_staff.append(full_name + " " + "STAFF" + " " + "Y" + " " + "N")
            print colored("NO ROOMS AVAILABLE!! ADDED TO WAITING LIST", "red")
            print colored("-------------------", "red")
            return "NO ROOMS AVAILABLE!!"

        print colored("*--*--*STAFF SUCCESSFULLY ADDED*--*--*", "yellow")
        print colored("       ------------------------        ", "yellow")
        print "NAME: %s"%full_name
        print "ROLE: %s"%role
        print "OFFICE: %s"%office
        print colored("---------------------------------------", "yellow")
        print
        return "ROOM SUCCESSFULLY ASSIGNED!!"
    
    elif role == "FELLOW" and accomodation_status == "N":
        living_space = "----"
        for room in Room.offices:
            if room.num_of_occupants < room.max_number:
                office = room.room_name
                first_name, last_name = full_name.split(" ")
                database.add_person(full_name, role, office, living_space, timestamp)
                first_name = Amity(full_name, role, office, living_space)
                Room.allocated_persons.append(first_name)
                Room.allocated_rooms.append(office)
                room.num_of_occupants += 1
                database.update_room(room.num_of_occupants, room.room_name)
                break
        else:
            print 
            Amity.unallocated_fellows.append(full_name + " " + "FELLOW" + " " + "Y" + " " + "N")
            print colored("NO ROOMS AVAILABLE!! ADDED TO WAITING LIST", "red")
            print colored("------------------", "red")
            return "NO ROOMS AVAILABLE!!"

        print colored("*--*--*FELLOW SUCCESSFULLY ADDED*--*--*", "yellow")
        print colored("       -------------------------       ", "yellow")
        print "NAME: %s"%full_name
        print "ROLE: %s"%role
        print "OFFICE: %s"%office
        print colored("----------------------------------------", "yellow")
        print 
        return "ROOM SUCCESSFULLY ASSIGNED!!"

    elif role == "FELLOW" and accomodation_status == "Y":
        for room in Room.living_spaces:
            if room.num_of_occupants < room.max_number:
                living_space = room.room_name
                room.num_of_occupants += 1
                database.update_room(room.num_of_occupants, room.room_name)
                break
        else:
            print
            print colored("NO LIVING SPACES AVAILABLE!! ONLY OFFICE ASSIGNED AND ADDED TO WAITING LIST", "blue")
            living_space = "----"
            Amity.unallocated_fellows.append(full_name + " " + "FELLOW" + " " + "N" + " " + "Y")

        for room in Room.offices:
            if room.num_of_occupants < room.max_number:
                office = room.room_name
                first_name, last_name = full_name.split(" ")
                database.add_person(full_name, role, office, living_space, timestamp)
                first_name = Amity(full_name, role, office, living_space)
                Room.allocated_persons.append(first_name)
                Room.allocated_rooms.append(office)
                Room.allocated_rooms.append(living_space)
                room.num_of_occupants += 1
                database.update_room(room.num_of_occupants, room.room_name)
                break
        else:
            if living_space != "----":
                office = "----"
                Amity.unallocated_fellows.append(full_name + " " + "FELLOW" + " " + "Y" + " " + "N") #NEED WORK
                print colored("ONLY LIVING SPACE AVAILABLE!! ADDED TO OFFICE WAITING LIST", "red")
                print colored("----------------------------------------------------------", "red")
                first_name, last_name = full_name.split(" ")
                database.add_person(full_name, role, office, living_space, timestamp)
                first_name = Amity(full_name, role, office, living_space)
                Room.allocated_persons.append(first_name)
                Room.allocated_rooms.append(office)
                Room.allocated_rooms.append(living_space)
            else:
                print
                Amity.unallocated_fellows.append(full_name + " " + "FELLOW" + " " + "Y" + " " + "Y") #NEED WORK
                print colored("NO ROOMS AVAILABLE!!", "red")
                print colored("------------------", "red")
                return "NO ROOMS AVAILABLE!!"
                
                
        print colored("*--*--*FELLOW SUCCESSFULLY ADDED*--*--*", "yellow")
        print colored("       -------------------------       ", "yellow")
        print "NAME: %s"%full_name
        print "ROLE: %s"%role
        print "OFFICE: %s"%office
        print "LIVING SPACE: %s"%living_space
        print colored("----------------------------------------", "yellow")
        print 
        return "ROOM SUCCESSFULLY ASSIGNED!!"

    else:
        print colored("INVALID INPUT!! PLEASE TRY AGAIN", "red")
        print
        return "INVALID INPUT"

def delete_room(room_name):
    if type(room_name) is not str:
        print colored("INVALID ROOM NAME", "red")
        return "INVALID ROOM NAME"
    else:
        room_name = room_name.upper()
        if room_name not in Amity.offices and room_name not in Amity.living_spaces:
            print colored("ROOM DOES NOT EXIST!!", "red")
            return "INVALID ROOM NAME"
        else:
            if room_name in Amity.offices:
                Amity.offices.remove(room_name)
                database.delete_room(room_name)
                for room in Room.offices:
                    if room.room_name == room_name:
                        Room.offices.remove(room)
                        del room
                print "---------------------------------"
                print colored("ROOM %s SUCCESSFULLY DELETED"%room_name, "red")
                print
                return "SUCCESS"

            elif room_name in Amity.living_spaces:
                Amity.living_spaces.remove(room_name)
                database.delete_room(room_name)
                for room in Room.living_spaces:
                    if room.room_name == room_name:
                        Room.living_spaces.remove(room) 
                        del room
                print "--------------------------------"
                print colored("ROOM %s SUCCESSFULLY DELETED"%room_name ,"red")
                print
                return "SUCCESS"

def print_allocations():
    if len(Room.allocated_persons) == 0:
        print colored("<== AMITY ALLOCATIONS ==> ", "cyan")
        print colored("    -----------------     ", "cyan")
        print colored(" NO ALLOCATIONS AVAILABLE", "red")
        print colored("--------------------------", "cyan")
        print
        return "EMPTY!!"
    else:
        print colored("<== AMITY ALLOCATIONS ==> ", "cyan")
        print colored("    -----------------     ", "cyan")
        for person in Room.allocated_persons:
            if person.role == "STAFF":
                print colored("-----------------------------------------", "cyan")
                print colored("|STAFF NAME: %s"%person.full_name, "cyan")
                print colored("|ALLOCATED OFFICE: %s"%person.office, "cyan")
                print colored("-----------------------------------------", "cyan")

        for person in Room.allocated_persons:
            if person.role == "FELLOW":
                if person.living_space == "----":
                    print colored("-----------------------------------------", "cyan")
                    print colored("|FELLOW NAME: %s"%person.full_name, "cyan")
                    print colored("|ALLOCATED OFFICE: %s"%person.office, "cyan")
                    print colored("-----------------------------------------", "cyan")
                else:
                    print colored("-----------------------------------------", "cyan")
                    print colored("|FELLOW NAME: %s"%person.full_name, "cyan")
                    print colored("|ALLOCATED OFFICE: %s"%person.office, "cyan")
                    print colored("|ALLOCATED LIVING SPACE: %s"%person.living_space, "cyan")
                    print colored("-----------------------------------------", "cyan")

        return "SUCCESS!!"

def print_unallocated():
    if len(Amity.unallocated_fellows) == 0 and len(Amity.unallocated_staff) == 0:
        print colored("OOPS!! ALL PERSONS ARE ALLOCATED!!", "magenta")
        return "ALL ALLOCATED"
    else:
        print colored("<== UNALLOCATED PERSONS IN AMITY ==>", "cyan")
        print colored("    ----------------------------    ", "cyan")
        for person in Amity.unallocated_fellows:
            first_name, last_name, role, office_status, accomodation_status = person.split(" ")
            print colored("-----------------------------------", "cyan")
            print "|NAME: %s %s "%(first_name,last_name)
            print "|ROLE: FELLOW"
            print "|"
        for person in Amity.unallocated_staff:
            first_name, last_name, role, office_status, accomodation_status = person.split(" ")
            print colored("-----------------------------------", "cyan")
            print "|NAME: %s %s "%(first_name,last_name)
            print "|ROLE: STAFF" 
            print "|"
        return "SUCCESS!!" 

def print_room(room_name):
    if type(room_name) != str or len(room_name) == 0:
        print colored("INVALID INPUT!! ROOM NAME CANNOT BE EMPTY OR A NON-STRING!!", "red")
        return "INVALID TYPE INPUT!!"
    else:
        room_name = room_name.upper()
        if room_name not in Amity.rooms[0] and room_name not in Amity.rooms[1]:
            print colored("INVALID INPUT!! ROOM DOES NOT EXIST", "red")
            print
            return "INVALID ROOM INPUT!! "
        else:
            if room_name not in Room.allocated_rooms:
                print colored("INVALID INPUT!! ROOM DOES HAS NOT BEEN ALLOCATED", "red")
                print
                return "INVALID ROOM INPUT!!"
            else:
                print colored("*--*--* %s ALLOCATIONS *--*--*", "blue")
                print colored("     ------------------------    ")
                for person in Room.allocated_persons:
                    if person.office == room_name:
                        print "------------------------"
                        print "NAME: %s"%person.full_name
                        print "------------------------" 
                    elif person.living_space == room_name:
                        print "------------------------"
                        print "NAME: %s"%person.full_name
                        print "------------------------" 
                return "SUCCESS!"

def check_rooms():
    for room in Room.offices:
        if room.num_of_occupants < room.max_number:
            Amity.available_offices.append(room.room_name)

    for room in Room.living_spaces:
        if room.num_of_occupants < room.max_number:
            Amity.available_living_spaces.append(room.room_name)
