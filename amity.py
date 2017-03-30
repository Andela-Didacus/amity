import time
import datetime
from termcolor import colored
from person import Staff, Fellow
from room import Room, Living_space, Office



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
                timestamp = str(datetime.datetime.fromtimestamp(day).strftime("%y-%m-%d"))
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
                printer_room(room_name.room_name, room_name.room_type, room_name.timestamp)
                return "ROOM SUCCESSFULLY CREATED IN AMITY"

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
    @staticmethod
    def print_allocations(file_name):
        file_name = file_name
        print colored("\n<== AMITY ALLOCATIONS ==> ", "cyan")
        print colored("    -----------------     ", "cyan")
        if len(Amity.allocated_persons) == 0:
            print colored(" NO ALLOCATIONS AVAILABLE", "red")
            print colored("--------------------------\n", "cyan")
        else:
            save_to_file = open("files/"+ self.file_name,"w")
            for person in Amity.allocated_persons:
                print colored("-----------------------------------------", "cyan")
                print colored("|STAFF NAME: %s"%person.full_name, "cyan")
                if person.role == "STAFF":
                    print colored("|ALLOCATED OFFICE: %s"%person.office, "cyan")
                    print colored("-----------------------------------------\n", "cyan")
                    if self.file_name != "None":
                        staff_allocations = "\nSTAFF NAME: %s\nALLOCATED OFFICE: %s\n----------------------------------------------------------\n"%(person.full_name, person.office)
                        save_to_file.write(staff_allocations)
                elif person.role == "FELLOW":
                    if person.living_space == "----":
                        print colored("|ALLOCATED OFFICE: %s"%person.office, "cyan")
                        print colored("-----------------------------------------", "cyan")
                        if self.file_name != "None":
                            fellow_allocations = "\nFELLOW NAME: %s\nALLOCATED OFFICE: %s\n-------------------------------------------------------\n"%(person.full_name, person.office)
                            save_to_file.write(fellow_allocations)
                    else:
                        print colored("|ALLOCATED OFFICE: %s"%person.office, "cyan")
                        print colored("|ALLOCATED LIVING SPACE: %s"%person.living_space, "cyan")
                        print colored("-----------------------------------------", "cyan")
                        if self.file_name != "None":
                            fellow_allocations1 = "\nFELLOW NAME: %s\nALLOCATED OFFICE: %s\nALLOCATED LIVING SPACE: %s\n----------------------------------------------\n"%(person.full_name, person.office, person.living_space)
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
            save_to_file = open("files/"+ file_name, "w")
            for person in Amity.unallocated_fellows:
                first_name, last_name, role, office_status, accomodation_status = person.split(" ")
                print colored("-----------------------------------", "cyan")
                print colored("|NAME: %s %s "%(first_name,last_name), "cyan")
                print colored("|ROLE: FELLOW", "cyan")
                if file_name != "None":
                    data = "\nName: {} {} \nRole: Fellow \n".format(first_name,last_name)
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
                first_name, last_name, role, office_status, accomodation_status = person.split(" ")
                print colored("-----------------------------------", "cyan")
                print colored("|NAME: %s %s "%(first_name,last_name), "cyan")
                print colored("|ROLE: STAFF", "cyan") 
                print colored("|PENDING OFFICE ALLOCATION", "cyan")
                print colored("-----------------------------------", "cyan")
                if file_name != "None":
                    staff_data = "\n\nName: {} {} \nRole: Staff \n Pending Office Allocation".format(first_name,last_name)
                    save_to_file.write(staff_data)    
            save_to_file.close()
            return "SUCCESSFULLY PRINTED UNALLOCATED!!" 

    @staticmethod
    def add_person(first_name, last_name, role, accomodation_status)
    
    

def printer_room(room_name, room_type, timestamp): #Helper function
    print colored("\n*--* AMITY *--*", "cyan")
    print colored("     ----------      ", "cyan")
    print colored("ROOM_NAME: %s"%room_name , "cyan")
    print colored("ROOM TYPE: %s"%room_type , "cyan")
    print colored("DATE CREATED: %s"%timestamp , "cyan")
    print colored("*--*--*--*--*--*--*--*--*--*\n", "cyan")


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

def printer_room(room_name, room_type, timestamp): #Helper function
    print colored("\n*--* AMITY *--*", "cyan")
    print colored("     ----------      ", "cyan")
    print colored("ROOM_NAME: %s"%room_name , "cyan")
    print colored("ROOM TYPE: %s"%room_type , "cyan")
    print colored("DATE CREATED: %s"%timestamp , "cyan")
    print colored("*--*--*--*--*--*--*--*--*--*\n", "cyan")