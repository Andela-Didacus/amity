class Person(object):
    def get_room(self,full_name, role, accomodation_status):
        self.day = time.time()
        self.timestamp = str(datetime.datetime.fromtimestamp(self.day).strftime("%y-%m-%d"))
        self.role = role
        self.full_name = full_name
        self.accomodation_status = accomodation_status
        

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
        try:
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
        except:
            print colored("OOPS!! SOMETHING WENT WRONG WITH THE PERSONS!!")
            return "something went wrong!!"

        