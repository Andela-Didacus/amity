from termcolor import cprint, colored
import sys
import datetime
import time
import itertools

from amity import Amity, Persons
from room import Rooms, check_rooms, clear, create_room

class Person(object):
    def get_room(self,full_name, role, accomodation_status):
        self.day = time.time()
        self.timestamp = str(datetime.datetime.fromtimestamp(self.day).strftime("%y-%m-%d"))
        self.role = role
        self.full_name = full_name
        self.accomodation_status = accomodation_status
        amity = Rooms() 
        if self.full_name in Amity.fellows or self.full_name in Amity.staff:
                print colored("\nNOTICE!! NAME ALREADY EXISTS!! USE ANOTHER NAME\n", "red")
                return "DUPLICATE"
        else:
            if self.role == "STAFF":
                amity.allocate_staff_room(self.full_name,  self.role, self.accomodation_status, self.timestamp)

            elif self.role == "FELLOW" and self.accomodation_status == "N":
                amity.allocate_fellow_room_with_no_accomodation(self.full_name, self.role, self.accomodation_status, self.timestamp)

            elif self.role == "FELLOW" and self.accomodation_status == "Y":
                amity.allocate_fellow_with_accomodation(self.full_name, self.role, self.accomodation_status, self.timestamp)

    def get_new_room(self, full_name, new_room):
        self.full_name = full_name
        self.new_room = new_room
        amity = Rooms()
        day = time.time()
        timestamp = str(datetime.datetime.fromtimestamp(day).strftime("%y-%m-%d"))
        if type(self.full_name) is not str or type(self.new_room) is not str:
            print colored("\nINVALID TYPE INPUT PLEASE TRY AGAIN\n", "red")
            return "INVALID TYPE INPUT!!"
        else:
            self.full_name = self.full_name.upper()
            self.new_room = self.new_room.upper()
            if self.full_name not in Amity.fellows and self.full_name not in Amity.staff:
                invalid_input_notifier()
                amity.print_allocations("None")
            else:
                check_rooms()
                if self.new_room not in Amity.offices and self.new_room not in Amity.living_spaces:
                    print colored("\nINVALID ROOM_NAME!! ROOM DOES NOT EXIST\n", "red")
                    print self.new_room
                    amity.print_rooms()
                    return "INVALID ROOM NAME!!"

                elif self.full_name in Amity.staff and self.new_room in Amity.living_spaces:
                    print colored("\nNOTICE!! STAFF CANNOT BE RELOCATED TO LIVING SPACES\n", "red")
                    return "STAFF CANNOT BE REALLOCATED TO LIVING SPACES!!"
                elif self.new_room not in Amity.available_living_spaces and self.new_room not in Amity.available_offices:
                    print colored("\n-------------------------------------------------------------------------------", "red")
                    print colored("ROOM IS FULL PLEASE PICK ANOTHER ROOM OR PERSON CANNOT BE REALLOCATED SAME ROOM\n", "red")
                    amity.print_available_space()
                    print Amity.available_offices
                    print self.new_room
                    return "ROOM FULL!!"
                else:
                    first_name, last_name = self.full_name.split(" ")
                    for person in Amity.allocated_persons:
                        if person.full_name == self.full_name:
                            current_details_printer(self.full_name, person.office, person.living_space)
                            if self.new_room in Amity.living_spaces:
                                unassign_room_living_space(person.living_space)
                                self.living_space = assign_new_room_living_space(new_room, person.living_space)
                                for person in Amity.allocated_persons:
                                    if person.full_name == self.full_name:
                                        self.role = person.role
                                        self.office = person.office
                                        Rooms.allocated_persons.remove(person)
                                        del person
                                        break
                                from amity import Persons
                                first_name = Persons(self.full_name, self.role, self.office, self.living_space)
                                Amity.allocated_persons.append(first_name)
                                Amity.allocated_rooms.append(self.living_space)
                                new_room_printer(self.full_name, self.role, self.office, self.living_space)
                                return "ROOM SUCCESSFULLY ASSIGNED!!"

                            elif self.new_room in Amity.offices:
                                unassign_room_office(self.new_room)
                                self.office = assign_new_room_office(self.new_room, person.office)
                                for person in Rooms.allocated_persons:
                                    if person.full_name == self.full_name:
                                        self.role = person.role
                                        self.living_space = person.living_space
                                        Rooms.allocated_persons.remove(person)
                                        del person
                                        break
                                from amity import Persons
                                first_name = Persons(self.full_name, self.role, self.office, self.living_space)
                                Rooms.allocated_persons.append(first_name)
                                Rooms.allocated_rooms.append(self.office)
                                new_room_printer_office(self.full_name, self.role, self.office, self.living_space)
                                clear()
                                return "ROOM SUCCESSFULLY ASSIGNED!!"

class Staff(Person):
    def __init__(self, first_name, last_name, role, accomodation_status):
        full_name = first_name + " " + last_name
        self.full_name = full_name
        self.role = role
        self.accomodation_status = accomodation_status

class Fellow(Person):
    def __init__(self, first_name, last_name, role, accomodation_status):
        full_name = first_name + " " + last_name
        self.full_name = full_name
        self.role = role
        self.accomodation_status = accomodation_status

def create_person(first_name, last_name, role, accomodation_status):
    role = role.upper()
    if (type(first_name) is not str or type(last_name) is not str) or (type(role) is not str) or (type(accomodation_status) is not str):
        print colored("\nINVALID INPUT! ONLY STRINGS ALLOWED!!\n", "red")
        return "INVALID INPUT!! TYPE ERROR!!"

    elif len(first_name) == 0 or len(last_name) == 0:
        print colored("\nINVALID INPUT! BOTH NAMES MUST BE PROVIDED\n", "red")
        return "INVALID NAME INPUT!!"

    elif accomodation_status not in ["y","Y","N","n"]:
        print colored("\nINVALID INPUT! ACCOMODATION STATUS CAN ONLY BE \'Y\' OR \'N\'\n", "red")
        return "INVALID ACCOMODATION STATUS INPUT"
    
    elif role not in ["STAFF", "FELLOW"]:
        print colored("\nINVALID INPUT! PERSON CAN ONLY BE STAFF OR FELLOW\n", "red")
        return "INVALID ROLE INPUT!!"
    else:
        # try:
        if first_name.isalpha() and last_name.isalpha():
            first_name = first_name.upper()
            last_name = last_name.upper()
            accomodation_status = accomodation_status.upper()
            full_name = first_name + " " + last_name
            if role == "STAFF":
                first_name = Staff(first_name, last_name, role, accomodation_status)
                first_name.get_room(full_name, role, accomodation_status)
                return "staff successfully added!!"
            elif role == "FELLOW":
                first_name = Fellow(first_name, last_name, role, accomodation_status)
                first_name.get_room(full_name, role, accomodation_status)
                return "fellow successfully added!!"
        else:
            print colored("\nNOTICE!! NAMES CANNOT BE A NUMBER", "red")
            print colored("---------------------------------", "red")
            return "INVALID NUMBER NAME!!"
        # except:
        #     print colored("OOPS!! SOMETHING WENT WRONG WITH THE PERSONS!!")
        #     return "something went wrong!!"

def invalid_input_notifier():
    print colored("\n-----------------------------------------", "red")
    print colored("NOTICE!! STAFF NAME INVALID!! STAFF DOES NOT EXIST\n", "red")
    print colored("CHECKOUT THE ALLOCATIONS LIST", "blue")
    print colored("-----------------------------\n", "blue")

def current_details_printer(full_name, office, living_space):
    print colored("\n<==%s'S CURRENT ROOM==>"%full_name, "blue")
    print colored("      ------------------        ", "blue")
    print "OFFICE: %s"%office
    print "LIVING SPACE: %s"%living_space
    print colored("-------------------------------------------\n", "blue") 

def unassign_room_living_space(living_space):
    for room in Amity.living_space_details:
        if room.room_name == living_space:
            room.num_of_occupants -= 1
            break
    
def unassign_room_office(office):
    for room in Amity.office_details:
        if room.room_name == office:
            room.num_of_occupants -= 1
            break
        
def assign_new_room_living_space(room_name,living_space):
    for room in Amity.living_space_details:
        if room.room_name == room_name and room.num_of_occupants < room.max_number and room.room_name != living_space:
            living_space = room.room_name
            room.num_of_occupants += 1
            break

    return living_space

def assign_new_room_office(room_name, office):
    for room in Amity.office_details:
        if room.room_name == room_name and room.num_of_occupants < room.max_number and room.room_name != office:
            office = room.room_name
            break
    return office

def new_room_printer(full_name, role, office, living_space):
    print colored("\n*--*--*LIVING SPACE SUCCESSFULLY REALLOCATED*--*--*", "blue")
    print "       ------------------------------------       "
    print "NAME: %s"%full_name
    print "ROLE: %s"%role
    print "OFFICE: %s"%office
    print "LIVING SPACE: %s\n"%living_space

def new_room_printer_office(full_name, role, office, living_space):
    print colored("\n*--*--*OFFICE SUCCESSFULLY REALLOCATED*--*--*", "blue")
    print colored("       -----------------------------------      ", "blue")
    print "NAME: %s"%full_name
    print "ROLE: %s"%role
    print "OFFICE: %s"%office
    print "LIVING SPACE: %s"%living_space
    print colored("-------------------------------------------------\n", "blue") 

def reallocate_person(full_name, new_room):
    amity = Persons()
    amity.get_new_room(full_name, new_room)
    return "SUCCESS!!"

def full_printer():
    print colored("\n-------------------------------------------------------------------------------", "red")
    print colored("ROOM IS FULL PLEASE PICK ANOTHER ROOM OR PERSON CANNOT BE REALLOCATED SAME ROOM\n", "red")
