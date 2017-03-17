import sys
import datetime
import time
import database

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
                print colored("NAME ALREADY EXISTS!! USE ANOTHER NAME", "red")
                return "DUPLICATE"
            else:
                allocate_room(self.full_name, self.role, self.accomodation_status, self.timestamp)
                if self.role == "STAFF":
                    Amity.staff.append(self.full_name)
                else:
                    Amity.fellows.append(self.full_name)

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
                        print colored("INVALID INPUT! STAFF CAN ONLY BE STAFF OR FELLOW", "red")
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

                except:
                    print colored("NAMES, ROLES OR ACCOMODATION STATUS CANNOT BE A NUMBER", "red")
                    return "INVALID NUMBER INPUT"

def reallocate_room(full_name, room_name):
    day = time.time()
    timestamp = str(datetime.datetime.fromtimestamp(day).strftime("%y-%m-%d"))
    if type(room_name) is not str or type(full_name) is not str:
        print colored("INVALID TYPE INPUT PLEASE TRY AGAIN", "red")
        print
        return "INVALID INPUT"
    else:
        room_name = room_name.upper()
        full_name = full_name.upper()
        if full_name not in Amity.fellows and full_name not in Amity.staff:
            print colored("STAFF NAME INVALID!! STAFF DOES NOT EXIST", "red")
            print
            return "INVALID NAME!!"
        else:
            if room_name not in Amity.offices and room_name not in Amity.living_spaces:
                print colored("INVALID ROOM_NAME!! ROOM DOES NOT EXIST", "red")
                print
                return "INVALID ROOM!!"
            else:
                if full_name in Amity.staff and room_name in Amity.living_spaces:
                    print colored("STAFF CANNOT BE RELOCATED TO LIVING SPACES", "red")
                    print 
                    return "INVALID STAFF ROOM!!"
                else:
                    first_name, last_name = full_name.split(" ")
                    for person in Room.allocated_persons:
                        if person.full_name == full_name:
                            print colored("<==CURRENT ROOM==>", "blue")
                            print "OFFICE: %s"%person.office
                            print "LIVING SPACE: %s"%person.living_space
                            print "--------------------"
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
                                    # # elif room.room_name == room_name and room.num_of_occupants >= room.max_number:
                                    # #     print "SELECTED ROOM IS FULL!! PICK ANOTHER ROOM"
                                    # #     print_available_rooms()
                                    # #     return "ROOM FULL!!"
                                    # #     break
                                else:
                                    print colored("ROOM IS FULL PLEASE PICK ANOTHER ROOM AND PERSON CANNOT BE REALLOCATED SAME ROOM", "red")
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
                            