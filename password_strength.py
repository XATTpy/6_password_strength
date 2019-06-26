from getpass import getpass
import re
from sys import argv


def load_blacklist(path_to_file):
    with open(path_to_file, 'r') as opened_file:
        return opened_file.read().split()


def is_in_blacklist(password, blacklist):
    return bool(password in blacklist)


def has_lower_case(password):
    return bool(re.findall(r"[a-z]", password))


def has_upper_case(password):
    return bool(re.findall(r"[A-Z]", password))


def has_numbers(password):
    return bool(re.findall(r"[0-9]", password))


def has_special_symbols(password):
    return bool(re.findall(r"\W", password))


def has_username(username, password):
    return bool(not username.lower() in password.lower())


def make_testlist(password, username, blacklist):
    testlist = []
    if is_in_blacklist(password, blacklist):
        testlist.append(False)
    else:
        testlist.append(has_lower_case(password))
        testlist.append(has_upper_case(password))
        testlist.append(has_numbers(password))
        testlist.append(has_special_symbols(password))
        testlist.append(has_username(username, password))
    return testlist


def get_password_strength(testlist):
    if len(testlist) == 1:
        return 1
    else:
        return testlist.count(True) * 2


def show_password_rating(password_rating):
    print("Your password rating: {}".format(password_rating))

    
if __name__ == "__main__":

    password = getpass(prompt="Input your password: ")
    username = input("Input your name: ")

    if not password:
        quit("Password is empty.")
    if len(password) < 6:
        quit("Password must include 6 or more characters")
    
    path_to_file = argv
    if len(path_to_file) > 1:
        try:
            blacklist = load_blacklist(path_to_file[1])
        except(FileNotFoundError, UnicodeDecodeError):
            print("Blacklist not found.")
            blacklist = []
    else:
        blacklist = []

    testlist = make_testlist(password, username, blacklist)
    password_rating = get_password_strength(testlist)
    show_password_rating(password_rating)
