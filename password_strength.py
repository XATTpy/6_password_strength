from getpass import getpass
import re


def load_blacklist(filename):
    with open(filename, 'r') as opened_file:
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


def make_testlist(password, blacklist, username):
    testlist = []
    if is_in_blacklist(password, blacklist):
        testlist.append(1)
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
    if not password:
        quit("Password is empty.")
    if len(password) < 6:
        quit("Password must include 6 or more characters")

    username = input("Input your name: ")
    blacklist = load_blacklist("blacklist.txt")
    testlist = make_testlist(password, blacklist, username)
    password_rating = get_password_strength(testlist)
    show_password_rating(password_rating)
