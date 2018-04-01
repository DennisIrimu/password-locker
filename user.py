import random
from credentials import credentials

def create_credentials(fname,lname,phone,email):
    '''
    Create new User
    '''
    new_user = Credentials(fname,lname,phone,email)
    return new_contact
def save_credentials(credentials):
    '''
    saves credentials
    '''
    credentials.save_credentials()

def display_credentials(credentials):
    '''
    displays user Credentials
    '''
    return Credentials.display_credentials()

def user():
    print("We're here to save your credentials and as a bonus we even help with password generation.")

    user_name = input()

    print(f"Hello {user_name}. What are you here to do?")
    print('\n')

    while True:
        print("Use the following to navigate through the app: new - create new account,display - display contacts,pg - password generation,exit - if you wanna leave")
        initials = input().lower()

        if initials =='new':
            print("Sign up")
            print("-"*10)

            print("Enter your first name")
            f_name = input()

            print("Enter your last name")
            f_name = input()

            print("Enter your mobile phone number")
            p_number = input()

            print("Enter your email address")
            e_address = input()

            save_credentials(create_credentials(f_name,l_name,p_number,e_address))

            print ('\n')
            print(f"New Account {f_name}{l_name} is saved")

        elif initials == 'display':

            if display_credentials():
                print(f"Here are your currently saved credentials Mrs/Madam {f_name} {l_name}")
                print('\n')
                for credentials in display_credentials():
                    print(f"{credentials.first_name} {credentials.last_name}...{credentials.number}")
                    print('\n')
                else:
                    print('\n')
                    print("No accounts yet")
                    print ('\n')

            elif initials == 'pg':

                random_password = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ?()@#$%^&*!"
                passlen = 8
                sample_password = "".join(random.sample(random_password,passlen ))
                print(f"generated password is{sample_password})

            elif initials == 'exit':

                print("Thank you, come again soon")
                break

            else:
                print("Please use required inputs")

if __name__ == '__main__':
    main()
