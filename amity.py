class Amity:
    offices = []
    living_spaces = []
    rooms = [offices,living_spaces]
    fellows = []
    staff = []
    persons = [staff,fellows]
    unallocated_staff = []
    unallocated_fellows = []
    available_living_spaces = []
    available_offices = []
    def __init__(self, full_name, role, office, living_space):
        self.full_name = full_name
        self.role = role
        self.office = office
        self.living_space = living_space