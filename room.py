import sys
import datetime
import time
from termcolor import colored

from amity import Amity, Persons


class Rooms(object):
    def allocate_staff_room(self, full_name, role, accomodation_status, timestamp):
        self.full_name = full_name
        self.role = role
        self.accomodation_status = accomodation_status
        self.timestamp = timestamp
        if role == "STAFF":
            self.living_space = "----"
            check_rooms()
            if len(Amity.available_offices) == 0:
                Amity.unallocated_staff.append(self.full_name + " " + "STAFF" + " " + "Y" + " " + "N") 
                print colored("\nNO ROOMS AVAILABLE!! ADDED TO WAITING LIST", "red")
                print colored("------------------------------------------\n", "red")
                clear()
                return "NO ROOMS AVAILABLE!!"
            else:
                self.office = assign_office()
                self.first_name, self.last_name = self.full_name.split(" ")
                self.first_name = Persons(self.full_name, self.role, self.office, self.living_space)
                Amity.allocated_persons.append(self.first_name)
                Amity.allocated_rooms.append(self.office)
                Amity.staff.append(self.full_name)
                if self.accomodation_status == "Y":
                    print colored("\nNB: STAFF ARE NOT ALLOWED LIVING SPACES!!\n", "red")
                printer_staff(self.full_name, self.role, self.office)
                clear()
                return "ROOM SUCCESSFULLY ASSIGNED!!"

    def allocate_fellow_room_with_no_accomodation(self, full_name, role, accomodation_status, timestamp):
        self.full_name = full_name
        self.role = role
        self.accomodation_status = accomodation_status
        self.timestamp = timestamp
        if role == "FELLOW":
            self.living_space = "----"
            check_rooms()
            if len(Amity.available_offices) == 0:
                Amity.unallocated_fellows.append(self.full_name + " " + "FELLOW" + " " + "Y" + " " + "N") 
                print colored("\nNO ROOMS AVAILABLE!! ADDED TO WAITING LIST", "red")
                print colored("------------------------------------------\n", "red")
                clear()
                return "NO ROOMS AVAILABLE!!"

            else:
                self.office = assign_office()
                self.first_name, self.last_name = self.full_name.split(" ")
                self.first_name = Persons(self.full_name, self.role, self.office, self.living_space)
                Amity.allocated_persons.append(self.first_name)
                Amity.allocated_rooms.append(self.office)
                Amity.fellows.append(self.full_name)
                printer_fellow_N(self.full_name, self.role, self.office)
                clear()
                return "ROOM SUCCESSFULLY ASSIGNED!!"

    def allocate_fellow_with_accomodation(self, full_name, role, accomodation_status, timestamp):
        self.full_name = full_name
        self.role = role
        self.accomodation_status = accomodation_status
        self.timestamp = timestamp
        check_rooms()
        if len(Amity.available_offices) == 0 and len(Amity.available_living_spaces) == 0:
            Amity.unallocated_fellows.append(self.full_name + " " + "FELLOW" + " " + "Y" + " " + "Y") 
            print colored("\nNO ROOMS AVAILABLE!! ADDED TO WAITING LIST", "red")
            print colored("------------------------------------------\n", "red")
            clear()
            return "NO ROOMS AVAILABLE!!"
        elif len(Amity.available_living_spaces) == 0 and len(Amity.available_offices) != 0:
            print colored("\nNO LIVING SPACES AVAILABLE!! ONLY OFFICE ASSIGNED AND ADDED TO WAITING LIST", "blue")
            self.living_space = "----"
            Amity.unallocated_fellows.append(self.full_name + " " + "FELLOW" + " " + "N" + " " + "Y")
            
            self.office = assign_office()
            self.first_name, self.last_name = self.full_name.split(" ")
            self.first_name = Persons(self.full_name, self.role, self.office, self.living_space)
            Amity.allocated_persons.append(self.first_name)
            Amity.allocated_rooms.append(self.office)
            Amity.fellows.append(self.full_name)
            printer_fellow_N(self.full_name, self.role, self.office)
            clear()
            return "ROOM SUCCESSFULLY ASSIGNED!!"
        elif len(Amity.available_living_spaces) != 0 and len(Amity.available_offices) == 0:
            print colored("\nNO OFFICES AVAILABLE!! ONLY LIVING SPACE ASSIGNED AND ADDED TO WAITING LIST", "blue")
            self.office = "----"
            Amity.unallocated_fellows.append(self.full_name + " " + "FELLOW" + " " + "Y" + " " + "N")

            self.living_space = assign_living_space()
            self.first_name, self.last_name = self.full_name.split(" ")
            self.first_name = Persons(self.full_name, self.role, self.office, self.living_space)
            Amity.allocated_persons.append(self.first_name)
            Amity.allocated_rooms.append(self.office)
            Amity.fellows.append(self.full_name)
            printer_fellow_accomodation_only(self.full_name, self.role, self.living_space)
            clear()
            return "ROOM SUCCESSFULLY ASSIGNED!!"

        elif len(Amity.available_living_spaces) != 0 and len(Amity.available_offices) != 0:
            self.office = assign_office()
            self.living_space = assign_living_space()
            self.first_name, self.last_name = self.full_name.split(" ")
            self.first_name = Persons(self.full_name, self.role, self.office, self.living_space)
            Amity.allocated_persons.append(self.first_name)
            Amity.allocated_rooms.append(self.office)
            Amity.fellows.append(self.full_name)
            printer_fellow_with_accomodation_and_office(self.full_name, self.role, self.office, self.living_space)
            clear()
            return "ROOM SUCCESSFULLY ASSIGNED!!"

    def print_rooms(self):
        print colored("\n<== AMITY ROOMS ==>", "blue")
        print colored("    -----------    ", "blue")
        if (len(Amity.offices) == 0) and (len(Amity.living_spaces) == 0):
            print colored("\nNOTICE!! NO ROOMS AVAILABLE IN AMITY AT THE MOMENT\n", "red")
            return "EMPTY"
        else:
            for room_type in Amity.all_rooms_details:
                for room in room_type:
                    print "ROOM NAME: %s"%room.room_name
                    print "ROOM TYPE: %s"%room.room_type
                    print "DATE CREATED: %s"%room.timestamp
                    print colored("------------------------------", "blue")
            return "SUCCESSFULLY PRINTED!!"

        

    def print_available_rooms(self):
        print colored("\n<== AVAILABLE AMITY ROOMS ==>", "green")
        print colored("    ---------------------   ", "green")
        check_rooms()
        if (len(Amity.available_living_spaces) == 0) and (len(Amity.available_offices) == 0):
            print colored(" NO ROOMS AVAILABLE IN AMITY", "red")
            print colored("------------------------------", "green")
            return "EMPTY"
        else:
            for room_type in Amity.all_rooms_details:
                for room in room_type:
                    if room.num_of_occupants < room.max_number:
                        print "ROOM NAME: %s"%room.room_name
                        print "ROOM TYPE: %s"%room.room_type
                        print "AVAILABLE SPACE: %s"%(room.max_number - room.num_of_occupants)
                        print colored("------------------------------", "green")
            clear()
            return "SUCCESSFULLY PRINTED!!"


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



def check_rooms():
    for room in Amity.office_details:
        if room.num_of_occupants < room.max_number:
            Amity.available_offices.append(room.room_name)

    for room in Amity.living_space_details:
        if room.num_of_occupants < room.max_number:
            Amity.available_living_spaces.append(room.room_name)

def clear():
    del Amity.available_living_spaces[:]
    del Amity.available_offices[:]

def assign_office():
    for room in Amity.office_details:
        if room.num_of_occupants < room.max_number:
            office = room.room_name
            room.num_of_occupants += 1
            break
    return office

def assign_living_space():
    for room in Amity.living_space_details:
        if room.num_of_occupants < room.max_number:
            living_space = room.room_name
            room.num_of_occupants += 1
            break
    return living_space

def printer_staff(full_name, role, office):
    print colored("\n*--*--*STAFF SUCCESSFULLY ADDED*--*--*", "yellow")
    print colored("       ------------------------        ", "yellow")
    print "NAME: %s"%full_name
    print "ROLE: %s"%role
    print "OFFICE: %s"%office
    print colored("---------------------------------------\n", "yellow")

def printer_fellow_N(full_name,role, office):
    print colored("\n*--*--*FELLOW SUCCESSFULLY ADDED*--*--*", "yellow")
    print colored("       -------------------------       ", "yellow")
    print "NAME: %s"%full_name
    print "ROLE: %s"%role
    print "OFFICE: %s"%office
    print colored("----------------------------------------\n", "yellow")

def printer_fellow_accomodation_only(full_name, role, living_space):
    print colored("\n*--*--*FELLOW SUCCESSFULLY ADDED*--*--*", "yellow")
    print colored("       -------------------------       ", "yellow")
    print "NAME: %s"%full_name
    print "ROLE: %s"%role
    print "LIVING SPACE: %s"%living_space
    print colored("----------------------------------------\n", "yellow")

def printer_fellow_with_accomodation_and_office(full_name, role, office, living_space):
    print colored("\n*--*--*FELLOW SUCCESSFULLY ADDED*--*--*", "yellow")
    print colored("       -------------------------       ", "yellow")
    print "NAME: %s"%full_name
    print "ROLE: %s"%role
    print "OFFICE: %s"%office
    print "LIVING SPACE: %s"%living_space
    print colored("----------------------------------------\n", "yellow") 