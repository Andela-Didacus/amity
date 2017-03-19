"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.

Usage:
    amity create_room <room_name>
    amity delete_room <room_name> 
    amity add_person <first_name> <last_name> <role> <accomodation>
    amity reallocate_person <person_identifier> <new_room_name>
    amity load_people
    amity print_rooms
    amity print_allocations [-o=filename]
    amity print_unallocated [-o=filename]
    amity print_available_rooms
    amity print_room <room_name>
    amity save_state [--db=sqlite_database]
    amity load_state <sqlite_database>
    amity (-i | --interactive)
    amity (-h | --help | --version)
    amity exit
 
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.

Note:
    use interactive for best perfomance
"""


import sys
import cmd
import database
import room
import amity
from room import print_allocations,print_available_rooms, create_room, delete_room,print_room, print_rooms, print_unallocated
from person import create_person, reallocate_room, allocate_unallocated
from termcolor import cprint, colored
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format
from docopt import docopt, DocoptExit

def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:

            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print ('Invalid Command!')
            print (e)
            print
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

class MyInteractive(cmd.Cmd):
    cprint(figlet_format('   AMITY   ', font='epic'),
           'red', attrs=['bold'])

    intro = 'WELCOME TO AMITY ROOM ALLOCATION SYSTEM' \
        + colored("""
Usage:
    AMITY create_room <room_name>
    AMITY delete_room <room_name> 
    AMITY add_person <first_name> <last_name> <role> <accomodation>         
    AMITY reallocate_person <person_first_name> <person_last_name> <new_room_name>
    AMITY load_people
    AMITY print_rooms
    AMITY print_allocations [-o=filename]
    AMITY print_unallocated [-o=filename]
    AMITY print_available_rooms
    AMITY print_room <room_name>
    AMITY save_state [--db=sqlite_database]
    AMITY load_state <sqlite_database>
    AMITY (-i | --interactive)
    AMITY (-h | --help)
    AMITY exit

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
""", "white")
    prompt = 'Enter a command: AMITY  '
    file = None

    def do_exit(self, arg):
        """Usage: exit"""
        print
        print colored("CLOSING AMITY APPLICATION!", "magenta")
        print colored("  *--*--* BYE *--*--*", "magenta")
        print

        exit()


    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_name>..."""
        try:
            for room_name in arg["<room_name>"]:
                create_room(room_name)
        except:
            print "AN ERROR HAS OCCURED"

    @docopt_cmd
    def do_delete_room(self,arg):
        """Usage: delete_room <room_name> """
        try:
           room_name = arg["<room_name>"]
           delete_room(room_name)
        except:
            print "error ocurred"
    @docopt_cmd
    def do_add_person(self, arg):
        # '''Usage: add_person <first_name> <last_name> <role> [--accomodation=accom]'''
        # if  arg['--accomodation'] == None:
        #     create_person(first_name=arg['<first_name>'], last_name=arg['<last_name>'], role =arg['<role>'], "N")
        # elif  arg['--accomodation'].upper() == 'Y':
        #     create_person(first_name=arg['<first_name>'], last_name=arg['<last_name>'], role =arg['<role>'], "Y")
        # elif  arg['--accomodation'].upper() == 'N':
        #     create_person(first_name= arg['<first_name>'], last_name=arg['<last_name>'], role =arg['<role>'], "N")
        """
        Usage: add_person <first_name> <last_name> <title> <accomodation>
        """
        first_name = arg["<first_name>"]
        last_name = arg["<last_name>"]
        role = arg["<title>"]
        accomodation = arg["<accomodation>"]
        # if arg["--accomodate"] == "y" or arg["--accomodate"] == "n":
        #     wants_accomodation = arg["--accomodate"]
        # else:
        #     wants_accomodation = "N"
        create_person(first_name, last_name, role, accomodation)
   

    @docopt_cmd
    def do_load_people(self, arg):
        """usage: load_people"""

    @docopt_cmd
    def do_print_rooms(self,arg):
        """usage: print_rooms"""
        try:
            print_rooms()
            print

        except:
            print "OOPS!! An error has occurred!"
            
        

    @docopt_cmd
    def do_reallocate_person(self, arg):
        """Usage: reallocate_person <person_first_name> <person_last_name> <new_room_name>"""
        
        first_name = arg["<person_first_name>"]
        last_name = arg["<person_last_name>"]
        new_room_name = arg["<new_room_name>"]
        person_identifier = first_name + " " + last_name
        reallocate_room(person_identifier, new_room_name) 

    @docopt_cmd
    def do_print_allocations(self, arg):
        """Usage: print_allocations [-o=filename]"""
        try:
            print_allocations()
        except:
            print "AN ERROR HAS OCCURED"

    @docopt_cmd
    def do_print_unallocated(self, arg):
        """Usage: print_unallocated [-o=filename]"""
        try:
            print_unallocated()
            print colored("PRESS 1 TO ALLOCATE ROOMS OR PRESS 2 TO CANCEL?", "cyan")
            allocate = str(input("==> "))
            if allocate == "1":
                allocate_unallocated()
            elif allocate == "2":
                print colored("THANK YOU ! :-)", "cyan")
                
            else:
                print colored("INVALID NUMBER INPUT!! ENTER 1 OR 2", "cyan")
                print colored("------------------------------------", "cyan")
                
        except:
            print colored("OOPS! AN ERROR HAS OCCURED", "red")

    @docopt_cmd
    def do_print_available_rooms(self, arg):
        """Usage: print_available_rooms"""
        try:
            print_available_rooms()
        except:
            print colored("OOPS! AN ERROR HAS OCCURED", "red")
        
    @docopt_cmd
    def do_print_room(self,arg):
        """Usage: print_room <room_name>"""
        try:
            room_name = arg["<room_name>"]
            print_room(room_name)
            print
        except:
            print "OOPS!! AN ERROR HAS OCCURED"
    @docopt_cmd
    def do_save_state(self,arg):
        """Usage: save_state [--db=sqlite_database]"""
    @docopt_cmd
    def do_load_state(self,arg):
        """Usage: load_state <sqlite_database>"""
        



opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    try:
        # print (__doc__)
        MyInteractive().cmdloop()
    except KeyboardInterrupt:
        print "\n"