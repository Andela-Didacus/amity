import unittest
import database
from room import create_room,delete_room,allocate_room, print_rooms, print_allocations, print_unallocated
from person import create_person, reallocate_room


class MyTests(unittest.TestCase):
    # room
    def test_accepts_only_string_room_name(self):
        self.assertEqual(create_room(7428), "INVALID input!!")

    def test_it_creates_room(self):
        self.assertEqual(create_room("aseey"),"ROOM SUCCESSFULLY CREATED IN AMITY")

    def test_it_does_not_aaccept_duplicate_names(self):
        self.assertEqual(create_room("Aseey"), "ROOM EXISTS!")

    def test_deletes_room(self):
        create_room("didah")
        self.assertEqual(delete_room("DIDAh"),"SUCCESSFULLY DELETED!!")

    def test_does_not_delete_room_notExisting(self):
        self.assertEqual(delete_room("PLATFORM"), "ROOM DOES NOT EXIST!!")
    
    def test_does_not_allocate_room_if_no_room(self):
        self.assertEqual(allocate_room("didah aseey","STAFF","N","---"), "NO ROOMS AVAILABLE!!")

    def test_it_allocates_room(self):
        create_room("narnia")
        self.assertEqual(allocate_room("didah aseey","STAFF","N","---"), 'ROOM SUCCESSFULLY ASSIGNED!!')

    def test_it_adds_staffs(self):
        create_room("php")
        self.assertEqual(create_person("Didacus", "ODhiamBO", "staff", "N"), "successfully added!!")
    
    def test_it_adds_fellow(self):
        create_room("java")
        self.assertEqual(create_person("Didacus", "ODhiamBO", "fellow", "y"), "successfully added!!")
    
    def test_it_does_duplicate_names(self):
        create_person("Didacus", "ODhiamBO", "fellow", "y")
        self.assertEqual(create_person("Didacus", "OdhiamBO", "staff", "y"), "successfully added!!")

    def test_it_accepts_only_string_person(self):
        self.assertEqual(create_person(334, "didah","staff", "y"), "INVALID INPUT!! TYPE ERROR!!")

    def test_it_only_accepts_staff_or_fellow(self):
        self.assertEqual(create_person("dida", "aseey", "student", "y"), "INVALID ROLE INPUT!!")

    def test_it_only_accepts_yes_or_no(self):
        self.assertEqual(create_person("dida", "aseey", "student", "x"), "INVALID ACCOMODATION STATUS INPUT")

    def test_it_does_not_reallocate_rooma_to_invalid_name(self):
        self.assertEqual(reallocate_room("JANE DOE", "php"), "STAFF DOES'NT EXIST!!")
        
    def test_it_does_not_reallocate_staff_to_living(self):
        create_person("JAKE", "JUMA", "STAFF", "Y")
        self.assertEqual(reallocate_room("JAKE JUMA", "php"), "STAFF CANNOT BE REALLOCATED TO LIVING SPACES!!")

    def test_it_does_not_reallocate_staff_to_living(self):
        create_person("paul", "kagame", "STAFF", "Y")
        self.assertEqual(reallocate_room("paul kagame", "dojo"), "INVALID! ROOM DOES NOT EXIST!!")

    def test_it_prints_rooms(self):
        self.assertEqual(print_rooms(),"SUCCESS!!")

    def test_it_prints_allocations(self):
        self.assertEqual(print_allocations(), "SUCCESSFULLY PRINTED!!")

    def test_it_prints_unallocated(self):
        self.assertEqual(print_unallocated(), "SUCCESSFULLY PRINTED UNALLOCATED!!")
        

if __name__=='__main__':
    unittest.main()