import time
import datetime
from termcolor import colored
from person import Staff, Fellow
from room import Room, Living_space, Office


class Amity(object):
    offices = []
    living_spaces = []
    rooms = [offices, living_spaces]
    fellows = []
    staff = []
    persons = [staff, fellows]
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
    def create_room(room_name, room_type):
        if type(room_name) != str or type(room_type) != str or room_name.isalpha() == False:
            print colored("\nINVALID NAME INPUT, NAME CANNOT BE A NUMBER\n", "red")
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
                timestamp = str(datetime.datetime.fromtimestamp(
                    day).strftime("%y-%m-%d"))
                if room_type == "OFFICE":
                    room_name = Office(room_name, room_type, timestamp)
                    Amity.office_details.append(room_name)
                    Amity.offices.append(room_name.room_name)
                elif room_type == "LIVING SPACE":
                    room_name = Living_space(room_name, room_type, timestamp)
                    Amity.living_space_details.append(room_name)
                    Amity.living_spaces.append(room_name.room_name)
                else:
                    print colored("\nINVALID INPUT!! ROOM CAN ONLY BE OFFICE OR \ LIVING SPACE\n", "red")
                    return "INVALID ROOM TYPE INPUT!!"
                printer_room(room_name.room_name,
                             room_name.room_type, room_name.timestamp)
                return "ROOM SUCCESSFULLY CREATED IN AMITY"

    @staticmethod
    def print_all_rooms():
        print colored("\n<== AMITY ROOMS ==>", "blue")
        print colored("    -----------    ", "blue")
        if (len(Amity.office_details) == 0) and (len(Amity.living_space_details) == 0):
            print colored("NO ROOMS AVAILABLE IN AMITY", "red")
            return "EMPTY"
        else:
            for room in Amity.office_details:
                print "ROOM NAME: %s" % room.room_name
                print "ROOM TYPE: %s" % room.room_type
                print "NUMBER OF OCCUPANTS: %s" % room.num_of_occupants
                print "DATE CREATED: %s" % room.timestamp
                print colored("------------------------------", "blue")

            for room in Amity.living_space_details:
                print "ROOM NAME: %s" % room.room_name
                print "ROOM TYPE: %s" % room.room_type
                print "NUMBER OF OCCUPANTS: %s" % room.num_of_occupants
                print "DATE CREATED: %s" % room.timestamp
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
                    print "ROOM NAME: %s" % room.room_name
                    print "ROOM TYPE: %s" % room.room_type
                    print "AVAILABLE SPACE: %s" % (room.max_number - room.num_of_occupants)
                    print colored("------------------------------", "green")
            for room in Amity.office_details:
                if room.num_of_occupants < room.max_number:
                    print "ROOM NAME: %s" % room.room_name
                    print "ROOM TYPE: %s" % room.room_type
                    print "AVAILABLE SPACE: %s" % (room.max_number - room.num_of_occupants)
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
                return "INVALID ROOM INPUT!!"
            else:
                if room_name not in Amity.allocated_rooms:
                    print colored("\n ROOM DOES HAS NOT BEEN ALLOCATED YET\n", "blue")
                    return "UNALLOCATED!!"
                else:
                    print_room_persons(room_name)
                    return "SUCCESS!!"

    @staticmethod
    def print_allocations(file_name):
        file_name = file_name.upper()
        print colored("\n<== AMITY ALLOCATIONS ==> ", "cyan")
        print colored("    -----------------     ", "cyan")
        if len(Amity.allocated_persons) == 0:
            print colored(" NO ALLOCATIONS AVAILABLE", "red")
            print colored("--------------------------\n", "cyan")
        else:
            save_to_file = open("files/" + file_name, "w")
            for person in Amity.allocated_persons:
                print colored("-----------------------------------------", "cyan")
                print colored("|STAFF NAME: %s" % person.full_name, "cyan")
                if person.role == "STAFF":
                    print colored("|ALLOCATED OFFICE: %s" % person.office, "cyan")
                    print colored("-----------------------------------------\n", "cyan")
                    if file_name != "NONE":
                        staff_allocations = "\nSTAFF NAME: %s\nALLOCATED OFFICE: %s\n----------------------------------------------------------\n" % (
                            person.full_name, person.office)
                        save_to_file.write(staff_allocations)
                elif person.role == "FELLOW":
                    if person.living_space == "----":
                        print colored("|ALLOCATED OFFICE: %s" % person.office, "cyan")
                        print colored("-----------------------------------------", "cyan")
                        if file_name != "NONE":
                            fellow_allocations = "\nFELLOW NAME: %s\nALLOCATED OFFICE: %s\n-------------------------------------------------------\n" % (
                                person.full_name, person.office)
                            save_to_file.write(fellow_allocations)
                    else:
                        print colored("|ALLOCATED OFFICE: %s" % person.office, "cyan")
                        print colored("|ALLOCATED LIVING SPACE: %s" % person.living_space, "cyan")
                        print colored("-----------------------------------------", "cyan")
                        if file_name != "NONE":
                            fellow_allocations1 = "\nFELLOW NAME: %s\nALLOCATED OFFICE: %s\nALLOCATED LIVING SPACE: %s\n----------------------------------------------\n" % (
                                person.full_name, person.office, person.living_space)
                            save_to_file.write(fellow_allocations1)
            save_to_file.close()
        return "SUCCESSFULLY PRINTED!!"

    @staticmethod
    def print_unallocated_people(file_name):
        file_name = file_name
        if len(Amity.unallocated_fellows) == 0 and len(Amity.unallocated_staff) == 0:
            print colored("\nOOPS!! ALL PERSONS ARE ALLOCATED!!\n", "magenta")
            return "ALL ALLOCATED"
        else:
            print colored("<== UNALLOCATED PERSONS IN AMITY ==>", "cyan")
            print colored("    ----------------------------    ", "cyan")
            save_to_file = open("files/" + file_name, "w")
            for person in Amity.unallocated_fellows:
                first_name, last_name, role, office_status, accomodation_status = person.split(
                    " ")
                print colored("-----------------------------------", "cyan")
                print colored("|NAME: %s %s " % (first_name, last_name), "cyan")
                print colored("|ROLE: FELLOW", "cyan")
                if file_name != "None":
                    data = "\nName: {} {} \nRole: Fellow \n".format(
                        first_name, last_name)
                    save_to_file.write(data)
                if office_status == "Y":
                    print colored("|PENDING OFFICE ALLOCATION", "cyan")
                    if file_name != "None":
                        office_data = "Pending office Allocation\n"
                        save_to_file.write(office_data)
                if accomodation_status == "Y":
                    print colored("|PENDING LIVING SPACE ALLOCATION", "cyan")
                    if file_name != "None":
                        ls_data = "Pending Living Space Allocation"
                        save_to_file.write(ls_data)
                print colored("-----------------------------------\n", "cyan")

            for person in Amity.unallocated_staff:
                first_name, last_name, role, office_status, accomodation_status = person.split(
                    " ")
                print colored("-----------------------------------", "cyan")
                print colored("|NAME: %s %s " % (first_name, last_name), "cyan")
                print colored("|ROLE: STAFF", "cyan")
                print colored("|PENDING OFFICE ALLOCATION", "cyan")
                print colored("-----------------------------------", "cyan")
                if file_name != "None":
                    staff_data = "\n\nName: {} {} \nRole: Staff \n Pending Office Allocation".format(
                        first_name, last_name)
                    save_to_file.write(staff_data)
            save_to_file.close()
            return "SUCCESSFULLY PRINTED UNALLOCATED!!"

    @staticmethod
    def add_person(first_name, last_name, role, accomodation_status):
        if (type(first_name) is not str or type(last_name) is not str) or (type(role) is not str) or (type(accomodation_status) is not str):
            print colored("\nINVALID INPUT! ONLY STRINGS ALLOWED!!\n", "red")
            return "INVALID INPUT!! TYPE ERROR!!"
        elif len(first_name) == 0 or len(last_name) == 0:
            print colored("\nINVALID INPUT! BOTH NAMES MUST BE PROVIDED\n", "red")
            return "INVALID NAME INPUT!!"
        else:
            first_name = first_name.upper()
            last_name = last_name.upper()
            role = role.upper()
            accomodation_status = accomodation_status.upper()
            if accomodation_status not in ["Y", "N"]:
                print colored("\nINVALID INPUT! ACCOMODATION STATUS CAN ONLY BE \'Y\' OR \'N\'\n", "red")
                return "INVALID ACCOMODATION STATUS INPUT"
            elif role not in ["STAFF", "FELLOW"]:
                print colored("\nINVALID INPUT! PERSON CAN ONLY BE STAFF OR FELLOW\n", "red")
                return "INVALID ROLE INPUT!!"
            else:
                if first_name.isalpha() and last_name.isalpha():
                    full_name = first_name + ' ' + last_name
                    if full_name in Amity.staff or full_name in Amity.fellows:
                        print colored("\nNOTICE!! NAME ALREADY EXISTS!! USE ANOTHER NAME\n", "red")
                        return "DUPLICATE"
                    else:
                        if role == "STAFF":
                            Amity.allocate_staff_room(
                                first_name, last_name, role, accomodation_status)
                        elif role == "FELLOW" and accomodation_status == "N":
                            Amity.allocate_fellow_with_no_accomodation(
                                first_name, last_name, role, accomodation_status)
                        elif role == "FELLOW" and accomodation_status == "Y":
                            Amity.allocate_fellow_with_accomodation(
                                first_name, last_name, role, accomodation_status)
                else:
                    print colored("\nNOTICE!! NAMES CANNOT BE A NUMBER", "red")
                    print colored("---------------------------------", "red")
                    return "INVALID NUMBER NAME!!"
              

    @staticmethod
    def allocate_staff_room(first_name, last_name, role, accomodation_status):
        if role == "STAFF":
            living_space = "----"
            for room in Amity.office_details:
                if room.num_of_occupants < room.max_number:
                    office = room.room_name
                    full_name = first_name + " " + last_name
                    first_name = Staff(full_name, role, office)
                    Amity.allocated_persons.append(first_name)
                    Amity.allocated_rooms.append(office)
                    Amity.staff.append(full_name)
                    room.num_of_occupants += 1
                    if accomodation_status == "Y":
                        print colored("\nNB: STAFF ARE NOT ALLOWED LIVING SPACES!!\n", "red")
                    break
            else:
                full_name = first_name + " " + last_name
                Amity.unallocated_staff.append(
                    full_name + " " + "STAFF" + " " + "Y" + " " + "N")
                print colored("\nNO ROOMS AVAILABLE!! ADDED TO WAITING LIST", "red")
                print colored("------------------------------------------\n", "red")
                return "NO ROOMS AVAILABLE!!"
            printer_staff(full_name, role, office)
            return "ROOM SUCCESSFULLY ASSIGNED!!"

    @staticmethod
    def allocate_fellow_with_no_accomodation(first_name, last_name, role, accomodation_status):
        if role == "FELLOW" and accomodation_status == "N":
            living_space = "----"
            for room in Amity.office_details:
                if room.num_of_occupants < room.max_number:
                    office = room.room_name
                    full_name = first_name + " " + last_name
                    first_name = Fellow(full_name, role, office, living_space)
                    Amity.allocated_persons.append(first_name)
                    Amity.allocated_rooms.append(office)
                    Amity.fellows.append(full_name)
                    room.num_of_occupants += 1
                    break
            else:
                full_name = first_name + " " + last_name
                Amity.unallocated_fellows.append(
                    full_name + " " + "FELLOW" + " " + "Y" + " " + "N")
                print colored("NO ROOMS AVAILABLE!! ADDED TO WAITING LIST", "red")
                print colored("------------------", "red")
                return "NO ROOMS AVAILABLE!!"
            printer_fellow_N(full_name, role, office)  # printer
            return "ROOM SUCCESSFULLY ASSIGNED!!"

    @staticmethod
    def allocate_fellow_with_accomodation(first_name, last_name, role, accomodation_status):
        clear()
        check_rooms()
        if len(Amity.available_offices) == 0 and len(Amity.available_offices) == 0:
            full_name = first_name + " " + last_name
            Amity.unallocated_fellows.append(
                full_name + " " + "FELLOW" + " " + "Y" + " " + "Y")
            print
            print colored("NO ROOMS AVAILABLE!! FELLOW ADDED TO THE WAITING LIST", "blue")
            print colored("-----------------------------------------------------", "red")
            clear()
            return "NO ROOMS AVAILABLE!!"
        else:
            full_name = first_name + " " + last_name
            for room in Amity.living_space_details:
                if room.num_of_occupants < room.max_number:
                    living_space = room.room_name
                    room.num_of_occupants += 1
                    break
            else:
                print colored("\nNO LIVING SPACES AVAILABLE!! ONLY OFFICE ASSIGNED AND ADDED TO WAITING LIST\n", "blue")
                living_space = "----"
                Amity.unallocated_fellows.append(
                    full_name + " " + "FELLOW" + " " + "N" + " " + "Y")

            for room in Amity.office_details:
                if room.num_of_occupants < room.max_number:
                    office = room.room_name
                    first_name = Fellow(full_name, role, office, living_space)
                    Amity.allocated_persons.append(first_name)
                    Amity.allocated_rooms.append(office)
                    Amity.allocated_rooms.append(living_space)
                    Amity.fellows.append(full_name)
                    room.num_of_occupants += 1
                    break

            else:
                if living_space != "----":
                    office = "----"
                    Amity.unallocated_fellows.append(
                        full_name + " " + "FELLOW" + " " + "Y" + " " + "N")  # NEED WORK
                    print colored("ONLY LIVING SPACE AVAILABLE!! ADDED TO OFFICE WAITING LIST", "red")
                    print colored("----------------------------------------------------------", "red")
                    first_name = Fellow(full_name, role, office, living_space)
                    Amity.allocated_persons.append(first_name)
                    Amity.allocated_rooms.append(office)
                    Amity.allocated_rooms.append(living_space)
                    Amity.fellows.append(full_name)

            printer_fellow_Y(full_name, role, office, living_space)
            return "ROOM SUCCESSFULLY ASSIGNED!!"

    @staticmethod
    def reallocate_person(full_name, room_name):
        day = time.time()
        timestamp = str(datetime.datetime.fromtimestamp(
            day).strftime("%y-%m-%d"))
        if type(room_name) is not str or type(full_name) is not str:
            print colored("\nINVALID TYPE INPUT PLEASE TRY AGAIN\n", "red")
            return "INVALID TYPE INPUT!!"
        else:
            room_name = room_name.upper()
            full_name = full_name.upper()
            if full_name not in Amity.fellows and full_name not in Amity.staff:
                reallocation_error_printer1(full_name)
                return "STAFF DOES'NT EXIST!!"
            elif room_name not in Amity.offices and room_name not in Amity.living_spaces:
                print colored("\nINVALID ROOM_NAME!! %s DOES NOT EXIST\n" % room_name, "red")
                return "INVALID! ROOM DOES NOT EXIST!!"
            elif full_name in Amity.staff and room_name in Amity.living_spaces:
                print colored("\nNOTICE!! STAFF CANNOT BE RELOCATED TO LIVING SPACES\n", "red")
                return "STAFF CANNOT BE REALLOCATED TO LIVING SPACES!!"
            else:
                first_name, last_name = full_name.split(" ")
                for person in Amity.allocated_persons:
                    if person.full_name == full_name:
                        current_details_printer(
                            full_name, person.office, person.living_space)
                        if room_name in Amity.living_spaces:
                            for room in Amity.living_space_details:
                                if room.room_name == person.living_space:
                                    room.num_of_occupants -= 1
                                    break

                            for room in Amity.living_space_details:
                                if room.room_name == room_name and room.num_of_occupants < room.max_number and room.room_name != person.living_space:
                                    living_space = room.room_name
                                    room.num_of_occupants += 1
                                    break
                            else:
                                print colored("\n-------------------------------------------------------------------------------", "red")
                                print colored("ROOM IS FULL PLEASE PICK ANOTHER ROOM OR PERSON CANNOT BE REALLOCATED SAME ROOM\n", "red")
                                return "ROOM FULL!!"

                            for person in Amity.allocated_persons:
                                if person.full_name == full_name:
                                    role = person.role
                                    office = person.office
                                    Amity.allocated_persons.remove(person)
                                    del person
                                    break

                            first_name = Fellow(
                                full_name, role, office, living_space)
                            Amity.allocated_persons.append(first_name)
                            Amity.allocated_rooms.append(living_space)
                            living_space_reallocator_printer(
                                full_name, role, office, living_space)
                            return "ROOM SUCCESSFULLY ASSIGNED!!"

                        elif room_name in Amity.offices:
                            for room in Amity.office_details:
                                if room.room_name == person.office:
                                    room.num_of_occupants -= 1
                                    break

                            for room in Amity.office_details:
                                if room.room_name == room_name and room.num_of_occupants < room.max_number and room.room_name != person.office:
                                    office = room.room_name
                                    room.num_of_occupants += 1
                                    break

                            else:
                                print colored("\nROOM IS FULL PLEASE PICK ANOTHER ROOM AND PERSON CANNOT BE REALLOCATED SAME ROOM\n", "red")
                                return "ROOM FULL!!"

                            for person in Amity.allocated_persons:
                                if person.full_name == full_name:
                                    role = person.role
                                    living_space = person.living_space
                                    Amity.allocated_persons.remove(person)
                                    del person
                                    break
                            if role == "STAFF":
                                first_name = Staff(full_name, role, office)
                            elif role == "FELLOW":
                                first_name = Fellow(
                                    full_name, role, office, living_space)
                            Amity.allocated_persons.append(first_name)
                            Amity.allocated_rooms.append(office)
                            office_reallocator_printer(
                                full_name, role, office, living_space)
                            return "ROOM SUCCESSFULLY ASSIGNED!!"

    @staticmethod
    def allocate_unallocated():
        day = time.time()
        timestamp = str(datetime.datetime.fromtimestamp(
            day).strftime("%y-%m-%d"))
        clear()
        check_rooms()
        # checks for availability of room
        if len(Amity.available_offices) != 0 or len(Amity.available_living_spaces) != 0:
            if len(Amity.unallocated_fellows) != 0 or len(Amity.unallocated_staff) != 0:
                for person in Amity.unallocated_fellows:
                    first_name, last_name, role, office_status, living_space_status = person.split(
                        " ")
                    full_name = first_name + ' ' + last_name
                    if office_status == "Y" and living_space_status == "Y":
                        Amity.add_person(first_name, last_name, role, "Y")
                        Amity.unallocated_fellows.remove(person)
                        clear()
                    elif office_status == "Y" and living_space_status == "N":
                        clear()
                        check_rooms()
                        if len(Amity.available_offices) != 0:
                            for room in Amity.office_details:
                                if room.num_of_occupants < room.max_number:
                                    office = room.room_name
                                    room.num_of_occupants += 1
                                    break
                            if isinstance(first_name, Fellow):
                                Amity.reallocate_person(full_name, office)
                                Amity.unallocated_fellows.remove(person)
                                clear()
                            elif isinstance(first_name, Fellow) == False:
                                Amity.add_person(
                                    first_name, last_name, "FELLOW", "N")
                                Amity.unallocated_fellows.remove(person)
                                clear()
                        else:
                            print colored("\nNOTICE!! NO ROOMS AVAILABLE FOR ALLOCATION\n", "red")
                            clear()

                    elif office_status == "N" and living_space_status == "Y":
                        clear()
                        check_rooms()
                        if len(Amity.available_living_spaces) != 0:
                            for room in Amity.living_space_details:
                                if room.num_of_occupants < room.max_number:
                                    living_space = room.room_name
                                    room.num_of_occupants += 1
                                    break
                            Amity.reallocate_person(full_name, living_space)
                            Amity.unallocated_fellows.remove(person)

                        else:
                            print colored("\nNO LIVING SPACES AVAILABLE!!\n", "red")

                for person in Amity.unallocated_staff:
                    clear()
                    check_rooms()
                    if len(Amity.available_offices) != 0:
                        first_name, last_name, role, office_status, living_space_status = person.split(
                            " ")
                        full_name = first_name + ' ' + last_name
                        Amity.add_person(first_name, last_name, "STAFF", "N")
                        Amity.unallocated_staff.remove(person)
                        clear()
                    else:
                        print "OFFICES FULL!! STAFF NOT ALLOCATED"
                    clear()
                return "SUCCESS!!"
            else:
                print colored("NO PERSON IS UNALLOCATED!!", "magenta")
                return "ALL PERSONS ALLOCATED!!"
        else:
            print colored("NO ROOMS AVAILABLE FOR ALLOCATION", "magenta")
            return "ROOMS FULL!!"


def printer_room(room_name, room_type, timestamp):  # Helper function
    print colored("\n*--* AMITY *--*", "cyan")
    print colored("     ----------      ", "cyan")
    print colored("ROOM_NAME: %s" % room_name, "cyan")
    print colored("ROOM TYPE: %s" % room_type, "cyan")
    print colored("DATE CREATED: %s" % timestamp, "cyan")
    print colored("*--*--*--*--*--*--*--*--*--*\n", "cyan")


def check_rooms():  # helper function for checking available rooms
    for room in Amity.office_details:
        if room.num_of_occupants < room.max_number:
            Amity.available_offices.append(room.room_name)

    for room in Amity.living_space_details:
        if room.num_of_occupants < room.max_number:
            Amity.available_living_spaces.append(room.room_name)


def clear():  # helper function for clearing available rooms list
    del Amity.available_living_spaces[:]
    del Amity.available_offices[:]


# helper function to print allocated people in a room
def print_room_persons(room_name):
    print colored("<== %s ALLOCATIONS ==>" % room_name, "blue")
    print colored("------------------------    ", "blue")
    for person in Amity.allocated_persons:
        if person.office == room_name:
            print "-----------------------------------"
            print "NAME: %s" % person.full_name
            print "ROLE: %s" % person.role
            print "-----------------------------------\n"
        elif person.living_space == room_name:
            print "-----------------------------------"
            print "NAME: %s" % person.full_name
            print "ROLE: %s" % person.role
            print "-----------------------------------\n"
    print colored("-----------------------------------\n", "blue")


def printer_room(room_name, room_type, timestamp):  # Helper function
    print colored("\n*--* AMITY *--*", "cyan")
    print colored("     ----------      ", "cyan")
    print colored("ROOM_NAME: %s" % room_name, "cyan")
    print colored("ROOM TYPE: %s" % room_type, "cyan")
    print colored("DATE CREATED: %s" % timestamp, "cyan")
    print colored("*--*--*--*--*--*--*--*--*--*\n", "cyan")


# helper function to print staff info after assignment
def printer_staff(full_name, role, office):
    print colored("\n*--*--*STAFF SUCCESSFULLY ADDED*--*--*", "yellow")
    print colored("       ------------------------        ", "yellow")
    print "NAME: %s" % full_name
    print "ROLE: %s" % role
    print "OFFICE: %s" % office
    print colored("---------------------------------------\n", "yellow")


# helper function to print fellow details
def printer_fellow_N(full_name, role, office):
    print colored("\n*--*--*FELLOW SUCCESSFULLY ADDED*--*--*", "yellow")
    print colored("       -------------------------       ", "yellow")
    print "NAME: %s" % full_name
    print "ROLE: %s" % role
    print "OFFICE: %s" % office
    print colored("----------------------------------------\n", "yellow")


# helper function to print fellow details
def printer_fellow_Y(full_name, role, office, living_space):
    print colored("\n*--*--*FELLOW SUCCESSFULLY ADDED*--*--*", "yellow")
    print colored("       -------------------------       ", "yellow")
    print "NAME: %s" % full_name
    print "ROLE: %s" % role
    print "OFFICE: %s" % office
    print "LIVING SPACE: %s" % living_space
    print colored("----------------------------------------\n", "yellow")


def reallocation_error_printer1(full_name):
    print colored("\n-----------------------------------------", "red")
    print colored("NOTICE!! STAFF NAME INVALID!! %s DOES NOT EXIST" % full_name, "red")
    print colored("CHECKOUT THE ALLOCATIONS LIST", "blue")
    print colored("-----------------------------\n", "blue")


def current_details_printer(full_name, office, living_space):
    print colored("\n<==%s'S CURRENT ROOM==>" % full_name, "blue")
    print colored("      -----------------------------         ")
    print "OFFICE: %s" % office
    print "LIVING SPACE: %s" % living_space
    print colored("-------------------------------------------\n", "blue")


def living_space_reallocator_printer(full_name, role, office, living_space):
    print colored("*--*--*LIVING SPACE SUCCESSFULLY REALLOCATED*--*-*", "blue")
    print "       ------------------------------------       "
    print "NAME: %s" % full_name
    print "ROLE: %s" % role
    print "OFFICE: %s" % office
    print "LIVING SPACE: %s" % living_space
    print "---------------------------------------------------------"


def office_reallocator_printer(full_name, role, office, living_space):
    print colored("\n*--*--*OFFICE SUCCESSFULLY REALLOCATED*--*--*", "blue")
    print "       ------------------------------------       "
    print "NAME: %s" % full_name
    print "ROLE: %s" % role
    print "OFFICE: %s" % office
    print "LIVING SPACE: %s" % living_space
    print "-------------------------------------------------------\n"
