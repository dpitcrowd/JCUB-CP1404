"""
Email
"""

MENU = """

    This script  allows  you to create 
    a  dictionary  of names and emails 
    starting from the insertion of the 
    user's email address.
    
    For  exit  please press  two times 
        >>>>>>    ENTER    <<<<<<
"""


def main():
    """Create dictionary of names from emails."""
    names_from_emails = {}

    print(MENU)
    email = input("\tInsert your email >>> ")
    while email != "":
        name = get_name_email(email)
        name_verification = input("\tIs your name {}? (Y/n) ".format(name))
        if name_verification.upper() != "Y" and name_verification != "":
            name = input("\tInsert your your real name: ")
        names_from_emails[email] = name
        #print(MENU)
        email = input("\tInsert your email >>> ")

    for email, name in names_from_emails.items():
        print("\t{} ({})".format(name, email))


def get_name_email(email):
    """Get name from email."""
    name = email.split('@')[0]

    return name


if __name__ == '__main__':
    main()
