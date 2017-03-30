
class Person(object):
    pass

class Staff(Person):
    def __init__(self, first_name, last_name, role, office):
      self.first_name = first_name
      self.last_name = last_name
      self.role = role
      self.office = office  

class Fellow(Person):
    def __init__(self, first_name, last_name, role, office, living_space):
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.office = office
        self.living_space = living_space
