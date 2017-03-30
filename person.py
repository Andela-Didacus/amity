
class Person(object):
    pass

class Staff(Person):
    def __init__(self, full_name, role, office):
      self.full_name = full_name
      self.role = role
      self.office = office
      self.living_space = "----"  

class Fellow(Person):
    def __init__(self, full_name, role, office, living_space):
        self.full_name = full_name
        self.role = role
        self.office = office
        self.living_space = living_space
