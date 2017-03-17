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
