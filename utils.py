from bcrypt import hashpw, checkpw, gensalt
from colorama import Fore, Style


# styles
def print_menu(message):
    print(Fore.BLUE, message, Style.RESET_ALL)


def print_error(message):
    print(Fore.RED, message, Style.RESET_ALL)


def print_success(message):
    print(Fore.GREEN, message, Style.RESET_ALL)


def print_info(message):
    print(Fore.CYAN, message, Style.RESET_ALL)


# security
def generate_password(password: str):
    hash_pw = hashpw(password.encode('utf-8'), gensalt())
    return hash_pw.decode('utf-8')


def match_password(password, hashed_password):
    return checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
