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
