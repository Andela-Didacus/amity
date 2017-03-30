import unittest
import database
import amity
from amity import Amity

class MyTests(unittest.TestCase):
    # room
    def test_accepts_only_string_room_name(self):
        self.assertEqual(Amity.create_room(True, "office"), "INVALID input!!")

    def test_it_creates_room(self):
        self.assertEqual(Amity.create_room("aseey", "office"),"ROOM SUCCESSFULLY CREATED IN AMITY")

    def test_it_does_not_aaccept_duplicate_names(self):
        self.assertEqual(Amity.create_room("Aseey", "office"), "ROOM EXISTS!")
    
    def test_does_not_allocate_staff_room_if_no_room(self):
        self.assertEqual(Amity.allocate_staff_room("didah", "aseey","STAFF","N"), "NO ROOMS AVAILABLE!!")

    def test_does_not_allocate_fellow_room_if_no_room(self):
        self.assertEqual(Amity.allocate_fellow_with_no_accomodation("didah", "aseey","FELLOW","N"), "NO ROOMS AVAILABLE!!")
    
    def test_does_not_allocate_fellow_room_if_no_room(self):
        self.assertEqual(Amity.allocate_fellow_with_accomodation("didah", "aseey","FELLOW","N"), "NO ROOMS AVAILABLE!!")

    def test_it_allocates_office(self):
        Amity.create_room("narnia", "office")
        self.assertEqual(Amity.allocate_staff_room("didah", "aseey","STAFF","N"), 'ROOM SUCCESSFULLY ASSIGNED!!')
    
    def test_it_allocates_fellow_office(self):
        Amity.create_room("narnia", "office")
        self.assertEqual(Amity.allocate_fellow_with_no_accomodation("didah", "aseey","FELLOW","N"), 'ROOM SUCCESSFULLY ASSIGNED!!')

    def test_it_allocates_fellow_living_space(self):
        Amity.create_room("narnia", "office")
        Amity.create_room("dojo", "living space")
        self.assertEqual(Amity.allocate_fellow_with_accomodation("didah", "aseey","FELLOW","Y"), 'ROOM SUCCESSFULLY ASSIGNED!!')

    def test_does_not_accept_number_room_names(self):
        self.assertEqual(Amity.create_room("123", "office"), "INVALID input!!")

    def test_it_does_not_accept_blank_room_names(self):
        self.assertEqual(Amity.create_room("", "office"), "INVALID input!!")
        
    def test_does_not_duplicate_room_names(self):
        Amity.create_room("dojo","office")
        self.assertEqual(Amity.create_room("dojo", "living space"), "ROOM EXISTS!")

    def test_only_accepts_office_or_living_space(self):
        self.assertEqual(Amity.create_room("java", "watchtower"), "INVALID ROOM TYPE INPUT!!")

    def test_it_prints_rooms(self):
        self.assertEqual(Amity.print_all_rooms(), "SUCCESS!!")

    def test_it_prints_available_space(self):
        self.assertEqual(Amity.print_available_space(), "SUCCESS!!")

    def test_it_does_not_accept_invalid_name_for_room_print(self):
        self.assertEqual(Amity.print_room(True), "INVALID TYPE INPUT!!")
    
    def test_it_does_not_accept_blank_names(self):
        self.assertEqual(Amity.print_room(""), "INVALID TYPE INPUT!!")
    
    def test_it_does_not_accept_number(self):
        self.assertEqual(Amity.print_room("123"), "INVALID TYPE INPUT!!")

    def test_it_does_not_accept_invalid_room(self):
        self.assertEqual(Amity.print_room("quietroom"), "INVALID ROOM INPUT!!")

    def test_if_room_allocated_before_printing(self):
        Amity.create_room("msa", "office")
        self.assertEqual(Amity.print_room("msa"), "UNALLOCATED!!")

    def test_it_prints_room_occupants(self):
        self.assertEqual(Amity.print_room("narnia"), "UNALLOCATED!!")

    def test_it_prints_allocations(self):
        self.assertEqual(Amity.print_allocations("amity.txt"), "SUCCESSFULLY PRINTED!!")

    def test_it_prints_unallocated_people(self):
        self.assertEqual(Amity.print_unallocated_people("amity.txt"), "SUCCESSFULLY PRINTED UNALLOCATED!!")

    def test_it_only_accepts_string_people_names(self):
        self.assertEqual(Amity.add_person(True, "aseey", "fellow", "N"), "INVALID INPUT!! TYPE ERROR!!")

    def test_it_not_allow_blank_names(self):
        self.assertEqual(Amity.add_person("", "", "fellow", "N"),"INVALID NAME INPUT!!") 

    def test_only_Y_or_N_for_accomodation(self):
        self.assertEqual(Amity.add_person("dida", "aseey", "fellow", "x"),"INVALID ACCOMODATION STATUS INPUT") 

    def test_only_staff_or_fellow_for_role(self):
        self.assertEqual(Amity.add_person("dida", "aseey", "worker", "Y"),"INVALID ROLE INPUT!!")

    def test_does_not_accept_number_names(self):
         self.assertEqual(Amity.add_person("123", "aseey", "fellow", "Y"),"INVALID NUMBER NAME!!")

    #tests for reallocation
    def test_does_not_accept_non_string(self):
        self.assertEqual(Amity.reallocate_person(True, "java"), "INVALID TYPE INPUT!!")
    
    def test_if_staff_exists(self):
        self.assertEqual(Amity.reallocate_person("denis Gathu", "java"), "STAFF DOES'NT EXIST!!")

    def test_if_room_exists(self):
        Amity.add_person("john","doe","staff", "N")
        self.assertEqual(Amity.reallocate_person("john doe", "dddd"), "INVALID! ROOM DOES NOT EXIST!!")

    def test_staff_cannot_be_moved_to_living_space(self):
        Amity.add_person("john","doe","staff", "N")
        Amity.create_room("tsavo", "living space")
        self.assertEqual(Amity.reallocate_person("john doe", "Tsavo"), "STAFF CANNOT BE REALLOCATED TO LIVING SPACES!!")

    def test_reallocates_staff(self):
        Amity.add_person("jane", "doe", "staff", "n")
        Amity.create_room("Home", "office")
        self.assertEqual(Amity.reallocate_person("jane doe", "home"), "ROOM SUCCESSFULLY ASSIGNED!!")
    
    def test_reallocates_fellow(self):
        Amity.add_person("jack", "doe", "fellow", "n")
        Amity.create_room("Home", "office")
        self.assertEqual(Amity.reallocate_person("jack doe", "home"), "ROOM SUCCESSFULLY ASSIGNED!!")

    def test_reallocates_living_place(self):
        Amity.add_person("mike", "jacobs", "fellow", "y")
        Amity.create_room("bingo", "living_space")
        self.assertEqual(Amity.reallocate_person("mike jacobs", "bingo"), "ROOM SUCCESSFULLY ASSIGNED!!")

    def test_it_allocates_unallocated(self):
        self.assertEqual(Amity.allocate_unallocated(), "SUCCESS!!")

    #test for helper functions
    def test_check_room_helper_fnction(self):
        self.assertEqual(amity.check_rooms(), None)
    

    def test_clear_helper_function(self):
        self.assertEqual(amity.clear(), None)

    def test_helper_print_room_persons_function(self):
        self.assertEqual(amity.print_room_persons("didah"), None)

    def test_helper_printer_room(self):
        self.assertEqual(amity.printer_room("d", "i", "aseey"), None)

    def test_printer_staff_helper_function(self):
        self.assertEqual(amity.printer_staff("dd", "fgf", "gdgd"), None)

    def test_printer_fellow_helper(self):
        self.assertEqual(amity.printer_fellow_N('full_name', 'role', 'office'), None)

    def test_living_space_reallocator_printer_helper(self):
        self.assertEqual(amity.living_space_reallocator_printer('full_name', 'role', 'office', 'living_space'), None)
        
    #database tests
    def test_it_saves_state(self):
        self.assertEqual(database.save_state("test.db"), "SUCCESSFULLY SAVED" )

    def test_it_loads_state(self):
        self.assertEqual(database.load_state("test.db"), "SUCCESSFULLY LOADED" )

    def test_it_loads_people(self):
        self.assertEqual(database.load_people(), "PERSONS SUCCESSFULLY LOADED")
        

        
if __name__=='__main__':
    unittest.main()