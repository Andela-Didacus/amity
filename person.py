import sys
import datetime
import time
import database
from amity import Amity
from termcolor import cprint, colored
from room import allocate_room, create_room, print_available_rooms,print_rooms, Room, print_allocations, print_room, print_unallocated, check_rooms, clear


class Person:
    staff = []
    fellows = []
    persons = [staff, fellows]

    def __init__(self, first_name, last_name, role, accomodation_status):
        full_name = first_name + " " + last_name
        self.full_name = full_name
        self.role = role
        self.accomodation_status = accomodation_status

    def add_person(self):
        self.day = time.time()
        self.timestamp = str(datetime.datetime.fromtimestamp(self.day).strftime("%y-%m-%d"))
        try:
            if self.full_name in Amity.fellows or self.full_name in Amity.staff:
                print
                print colored("NOTICE!! NAME ALREADY EXISTS!! USE ANOTHER NAME", "red")
                print
                return "DUPLICATE"
            else:
                allocate_room(self.full_name, self.role, self.accomodation_status, self.timestamp)
                # if self.role == "STAFF":
                #     Amity.staff.append(self.full_name)
                # else:
                #     Amity.fellows.append(self.full_name)

        except:
            pass

def create_person(first_name, last_name, role, accomodation_status):
    if (type(first_name) is not str or type(last_name) is not str) or (type(role) is not str) or (type(accomodation_status) is not str):
            print colored("INVALID INPUT! ONLY STRINGS ALLOWED!!", "red")
            return "INVALID INPUT!! TYPE ERROR!!"
    else:  
        if len(first_name) == 0 or len(last_name) == 0:
            print colored("INVALID INPUT! BOTH NAMES MUST BE PROVIDED", "red")
            return "INVALID NAME INPUT!!"
        else:
            if accomodation_status not in ["y","Y","N","n"]:
                print colored("INVALID INPUT! ACCOMODATION STATUS CAN ONLY BE \'Y\' OR \'N\'", "red")
                return "INVALID ACCOMODATION STATUS INPUT"
            else:
                try:
                    role = role.upper()
                    if role not in ["STAFF","FELLOW"]:
                        print colored("INVALID INPUT! PERSON CAN ONLY BE STAFF OR FELLOW", "red")
                        return "INVALID ROLE INPUT!!"
                    else:
                        first_name = first_name.upper()
                        last_name = last_name.upper()
                        accomodation_status = accomodation_status.upper()
                        first_name = Person(first_name, last_name, role, accomodation_status)
                        first_name.add_person()
                        if role == "STAFF":
                            Person.staff.append(first_name)
                        elif role == "FELLOW":
                            Person.fellows.append(first_name)
                        return "successfully added!!"

                except:
                    print colored("NAMES, ROLES OR ACCOMODATION STATUS CANNOT BE A NUMBER", "red")
                    return "INVALID NUMBER INPUT"

def reallocate_room(full_name, room_name):
    day = time.time()
    timestamp = str(datetime.datetime.fromtimestamp(day).strftime("%y-%m-%d"))
    if type(room_name) is not str or type(full_name) is not str:
        print colored("INVALID TYPE INPUT PLEASE TRY AGAIN", "red")
        print
        return "INVALID TYPE INPUT!!"
    else:
        room_name = room_name.upper()
        full_name = full_name.upper()
        if full_name not in Amity.fellows and full_name not in Amity.staff:
            print colored("-----------------------------------------", "red")
            print colored("NOTICE!! STAFF NAME INVALID!! STAFF DOES NOT EXIST", "red")
            print colored("CHECKOUT THE ALLOCATIONS LIST", "blue")
            print colored("-----------------------------", "blue")
            print_allocations()
            print
            return "STAFF DOES'NT EXIST!!"
        else:
            if room_name not in Amity.offices and room_name not in Amity.living_spaces:
                print colored("INVALID ROOM_NAME!! ROOM DOES NOT EXIST", "red")
                print
                print_available_rooms()
                return "INVALID! ROOM DOES NOT EXIST!!"
            else:
                if full_name in Amity.staff and room_name in Amity.living_spaces:
                    print colored("NOTICE!! STAFF CANNOT BE RELOCATED TO LIVING SPACES", "red")
                    print 
                    return "STAFF CANNOT BE REALLOCATED TO LIVING SPACES!!"
                else:
                    first_name, last_name = full_name.split(" ")
                    for person in Room.allocated_persons:
                        if person.full_name == full_name:
                            print
                            print colored("<==%s'S CURRENT ROOM==>"%full_name, "blue")
                            print colored("      -----------------------------         ")
                            print "OFFICE: %s"%person.office
                            print "LIVING SPACE: %s"%person.living_space
                            print colored("-------------------------------------------", "blue")
                            print 
                            if room_name in Amity.living_spaces:
                                for room in Room.living_spaces:
                                    if room.room_name == person.living_space:
                                        room.num_of_occupants -= 1
                                        database.update_room(room.num_of_occupants, room.room_name )
                                        break
                                for room in Room.living_spaces:
                                    if room.room_name == room_name and room.num_of_occupants < room.max_number and room.room_name != person.living_space:
                                        living_space = room.room_name
                                        break
                                else:
                                    print colored("-------------------------------------------------------------------------------", "red")
                                    print colored("ROOM IS FULL PLEASE PICK ANOTHER ROOM OR PERSON CANNOT BE REALLOCATED SAME ROOM", "red")
                                    print 
                                    print_available_rooms()
                                    print
                                    return "ROOM FULL!!"
                                 
                                for person in Room.allocated_persons:
                                    if person.full_name == full_name:
                                        role = person.role
                                        office = person.office
                                        Room.allocated_persons.remove(person)
                                        del person
                                        break
                                database.delete_person(full_name)
                                first_name = Amity(full_name, role, office, living_space)
                                Room.allocated_persons.append(first_name)
                                database.add_person(full_name, role, office, living_space, timestamp)
                                Room.allocated_rooms.append(living_space)
                                room.num_of_occupants += 1
                                database.update_room(room.num_of_occupants, room.room_name)
                                print colored("*--*--*LIVING SPACE SUCCESSFULLY REALLOCATED*--*--*", "blue")
                                print "       ------------------------------------       "
                                print "NAME: %s"%full_name
                                print "ROLE: %s"%role
                                print "OFFICE: %s"%office
                                print "LIVING SPACE: %s"%living_space
                                print 
                                return "ROOM SUCCESSFULLY ASSIGNED!!"
                                break
                            elif room_name in Amity.offices:
                                for room in Room.offices:
                                    if room.room_name == person.office:
                                        room.num_of_occupants -= 1
                                        database.update_room(room.num_of_occupants, room.room_name)
                                        break
                                for room in Room.offices:
                                    if room.room_name == room_name and room.num_of_occupants < room.max_number and room.room_name != person.office:
                                        office = room.room_name
                                        break
                                else:
                                    print colored("ROOM IS FULL PLEASE PICK ANOTHER ROOM AND PERSON CANNOT BE REALLOCATED SAME ROOM", "red")
                                    print_available_rooms()
                                    return "ROOM FULL!!"
                                 
                                for person in Room.allocated_persons:
                                    if person.full_name == full_name:
                                        role = person.role
                                        living_space = person.living_space
                                        Room.allocated_persons.remove(person)
                                        del person
                                        break

                                database.delete_person(full_name)
                                first_name = Amity(full_name, role, office, living_space)
                                Room.allocated_persons.append(first_name)
                                database.add_person(full_name, role, office, living_space, timestamp)
                                Room.allocated_rooms.append(living_space)
                                room.num_of_occupants += 1
                                database.update_room(room.num_of_occupants, room.room_name)
                                print colored("*--*--*OFFICE SUCCESSFULLY REALLOCATED*--*--*", "blue")
                                print colored("       -------------------------       ", "blue")
                                print colored("NAME: %s"%full_name ,"blue")
                                print "ROLE: %s"%role
                                print "OFFICE: %s"%office
                                print "LIVING SPACE: %s"%living_space
                                print 
                                return "ROOM SUCCESSFULLY ASSIGNED!!"
                                break

def allocate_unallocated():
    check_rooms()
    day = time.time()
    timestamp = str(datetime.datetime.fromtimestamp(day).strftime("%y-%m-%d"))
    if len(Amity.available_offices) != 0 or len(Amity.available_living_spaces) !=0:   #checks for availability of room
        if len(Amity.unallocated_fellows) != 0 or len(Amity.unallocated_staff) != 0: #checks if any person unallocated
            for person in Amity.unallocated_fellows:
                first_name, last_name, role, office_status, living_space_status = person.split(" ")
                full_name = first_name + ' ' + last_name
                # print colored(role, "red")
                if office_status == "Y" and living_space_status == "Y":
                    allocate_room(full_name, role, "Y", timestamp)
                    Amity.unallocated_fellows.remove(person)
                    clear()
                elif office_status == "Y" and living_space_status == "N":
                        if len(Amity.available_offices) != 0:
                            for room in Room.offices:
                                if room.num_of_occupants < room.max_number:
                                    office = room.room_name
                                    database.update_room(room.num_of_occupants, room.room_name)
                                    break
                            if isinstance(first_name, Amity):
                                check_rooms()
                                reallocate_room(full_name, office)
                                Amity.unallocated_fellows.remove(person)
                                clear()

                            else:
                                allocate_room(full_name, role, "N", timestamp)
                                Amity.unallocated_fellows.remove(person)
                                clear()
                        else:
                            print
                            print colored("NOTICE!! NO ROOMS AVAILABLE FOR ALLOCATION", "red")
                            print
            
                elif office_status == "N" and living_space_status == "Y":
                    check_rooms()
                    if len(Amity.available_living_spaces) != 0:
                        for room in Room.living_spaces:
                            if room.num_of_occupants < room.max_number:
                                living_space = room.room_name
                                database.update_room(room.num_of_occupants, room.room_name)
                                break
                        reallocate_room(full_name, living_space)
                        Amity.unallocated_fellows.remove(person)
                        clear()
                    else:
                        print 
                        print colored("NO LIVING SPACES AVAILABLE!!", "red")
                    clear()
                             
            for person in Amity.unallocated_staff:
                check_rooms()
                if len(Amity.available_offices) != 0:
                    first_name, last_name, role, office_status, living_space_status = person.split(" ")
                    full_name = first_name + ' ' + last_name
                    create_person(first_name, last_name, "staff", "N")
                    Amity.unallocated_staff.remove(person)
                    clear()
                else:
                    print "OFFICES FULL!! STAFF NOT ALLOCATED"
                clear()
        else:
            print colored("NO PERSON IS UNALLOCATED!!", "magenta")
    else:
        print colored("NO ROOMS AVAILABLE FOR ALLOCATION", "magenta")
        return "ROOMS FULL!!"
    clear()
