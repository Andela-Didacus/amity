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

class Persons(Amity):
    def __init__(self, full_name, role, office, living_space):
        self.full_name = full_name
        self.role = role
        self.office = office
        self.living_space = living_space