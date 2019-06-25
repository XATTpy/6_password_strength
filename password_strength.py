from getpass import getpass
import re


def load_blacklist(filename):
    with open(filename, 'r') as opened_file:
        return opened_file.read().split()


def get_password_strength(password, username, blacklist):
    password_rating = 10

    if password in blacklist:
        password_rating = 1
        return password_rating

    if not re.findall(r"[a-z]", password):
        password_rating -= 2
    if not re.findall(r"[A-Z]", password):
        password_rating -= 2
    if not re.findall(r"[0-9]", password):
        password_rating -= 2
    if not re.findall(r"\W", password):
        password_rating -= 2
    if username.lower() in password.lower():
        password_rating -= 2
    return password_rating


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
    password_rating = get_password_strength(password, username, blacklist)
    show_password_rating(password_rating)
