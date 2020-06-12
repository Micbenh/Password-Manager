from generator_db import GenoratorDB
import time

class PasswordGenerator:
    """ Password Generator Mian"""
    def __init__(self, db=None):
        self._db = db or GenoratorDB('test_passwords') 

    @staticmethod
    def options_menu():
        """ options menu beinng printed """

        print("Welcome to the password Generator!")
        print("Please choose one of the following options")
        print("1) Add a new password")
        print("2) List all current passwords")
        print("3) search for a password by site")
        print("4) search for a password by user ")
        print("5) Delete password")
        print("6) quit")

    def create_random_password(self):
        pass

    def add_new_password(self):
        try:
            user = input("Type your username: ").title()
            password = input("Enter yout password: ")
            service = input("What is the name of the service you signed up to?: ").title()
            self._db.add_a_new_password(user, password, service)
        except Exception as e:
            print("Sorry, something went wrong, {}".format(e))

    def list_passwords(self):
        print('=' * 120)
        for idy, name ,paswrd, serve in self._db.show_all_entries():
            print("\nid: {}\t username: {}\t  password:{}\t service: {}\n ".format(idy, name , paswrd, serve))
        print('=' * 120)

    def search_for_password_by_service(self):
        try:
            service = input("enter the name of your service: ").title()
        except ValueError:
            print("The service must be a string")
        else:
            self._db.search_by_service(service)
            print('=' * 120)
            for idy, name ,paswrd, serve in self._db.search_by_service(service):
                print("\nid: {}\t username: {}\t password: {}\t service: {}\n ".format(idy, name , paswrd, serve))
            print('=' * 120)

    def search_for_password_by_username(self):
        try:
            username = input("What is the user you want to look up?: ")
        except ValueError as e:
            print(e)
        else:
            self._db.search_by_user(username)
            print('=' * 120)
            for idy, name ,paswrd, serve in self._db.search_by_user(username):
                    print("\nid: {}\t username: {}\t password: {}\t service: {}\n ".format(idy, name , paswrd, serve))
            print('=' * 120)
            
    def delete_entry(self):
        self.list_passwords()
        print("Please enter the ID number of the entry you want to delete:")
        try:
            entry = input("> ")
        except ValueError as e:
            print(e)
        else:
            print('=' * 120)
            for idy, name ,paswrd, serve in self._db.select_by_id(entry):
                print("\nid: {}\t username: {}\t password: {}\t service: {}\n ".format(idy, name , paswrd, serve))
            print('=' * 120)
            print("Are you sure you weant to delete this user? (Y/N)")
            final_choice = input("> ").upper()
            if final_choice == 'N':
                print("\nentry was not deleted!\n")
            else:
                if final_choice != "N":
                    self._db.delete_row(entry)
                    print("\nentry was deleted sucessfully!\n")

    def exit(self):
        print("Thanks for using Password Generator!")


def main():
    running = True
    while running:
        genorator = PasswordGenerator()
        genorator.options_menu()

        command = input("> ")

        options = {
            '1': genorator.add_new_password,
            '2': genorator.list_passwords,
            '3': genorator.search_for_password_by_service,
            '4': genorator.search_for_password_by_username,
            '5': genorator.delete_entry,
            '6': genorator.exit
        }

        try: 
            choice = options[command]
        except KeyError:
            print("I dont understand")
        else:
            choice()

        time.sleep(0.5)

        if command == '6':
            break
    print("The program has closed.")
        
     

if __name__ == '__main__':
    main()