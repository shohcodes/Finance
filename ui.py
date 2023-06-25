from utils import print_info, print_error, print_menu, print_success
from service import AuthService, FinanceService
from exceptions import UnauthorizedException, FinanceServiceException
from getpass import getpass

session_user: dict = None
auth = AuthService()
finance = FinanceService()


def menu():
    print_info("-------------")
    if session_user is None:
        print_menu("1. Login")
        print_menu("2. Register")
    else:
        print_menu("1. Show balance")
        print_menu("2. Add balance")
        print_menu("3. Transfer Money")
        print_menu("4. Transfer History")
        print_menu("5. Log out")
    print_menu("q. Quit")
    choice = input("-->: ")
    if choice == 'q':
        return
    if session_user:
        user_menu(choice)
    else:
        auth_menu(choice)
    menu()


def user_menu(choice):
    global session_user
    try:
        match choice:
            case "1":
                finance.show_balance(session_user)
            case "2":
                amount = float(input("Enter amount: "))
                finance.add_balance(session_user, amount)
            case "3":
                receiver_username = input("Enter receiver username: ")
                receiver = auth.find_user_by_username(receiver_username)
                amount = float(input("Enter amount: "))
                finance.transfer_money(sender=session_user, receiver=receiver, amount=amount)
            case "4":
                finance.transfer_history()
            case "5":
                session_user = None
    except FinanceServiceException as e:
        print_error(e.message)


def auth_menu(choice):
    global session_user
    try:
        match choice:
            case "1":
                username = input("Enter username: ")
                password = getpass("Enter password: ")
                session_user = auth.login(username=username, password=password)
                print_success("User logged in✅")
            case "2":
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                username = input("Enter username: ")
                password = getpass("Password: ")
                phone = int(input("Phone number: "))
                auth.register(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    phone=phone
                )
                print_success("User registered✅")
    except UnauthorizedException as e:
        print_error(e.message)


if __name__ == '__main__':
    menu()
