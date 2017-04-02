from abc import ABCMeta, abstractmethod


class Person(object):
    __metaclass__ = ABCMeta

    def __init__(self, full_name, office):
        self.full_name = full_name
        self.office = office

    @abstractmethod
    def get_name(self):
        print self.full_name


class Staff(Person):

    def __init__(self, full_name,  office):
        self.role = "STAFF"
        self.living_space = None
        super(Staff, self).__init__(full_name, office)

    def get_name(self):
        print "Name: %s" % self.full_name


class Fellow(Person):

    def __init__(self, full_name, office, living_space=None):
        self.role = "FELLOW"
        self.living_space = living_space
        super(Fellow, self).__init__(full_name, office)

    def get_name(self):
        print "Name: %s" % self.full_name

