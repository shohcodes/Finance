import datetime

from exceptions import UnauthorizedException, FinanceServiceException
from models import Users, Transfers
from utils import print_info, generate_password, match_password, print_error

session_user: dict = None


class AuthService:
    users = []

    def __init__(self):
        self.__get_data()

    def __get_data(self):
        data = Users().select().fetchall()
        result = []
        if data:
            for item in data:
                dict_item = {
                    "id": item[0],
                    "name": item[1],
                    "last_name": item[2],
                    "username": item[3],
                    "password": item[4],
                    "phone": item[5],
                    "balance": item[6]
                }
                result.append(dict_item)
        self.users = result

    def login(self, username: str, password: str):
        login_user: dict = None
        for user in self.users:
            if user['username'] == username:
                login_user = user
                break
        else:
            raise UnauthorizedException("Username not found!")

        if not match_password(password, login_user.get('password')):
            raise UnauthorizedException('Incorrect password!')
        return login_user

    def register(self, **kwargs):
        check_username = self.check_username_unique(kwargs.get('username'))
        check_phone = self.check_phone_unique(kwargs.get('phone'))
        if check_username and check_phone:
            username = kwargs.get('username')
            if username is None:
                raise Exception("Username cant be None!")

            password = kwargs.get('password')
            if password is None:
                raise Exception("Password cant be None!")

            phone = kwargs.get('phone')
            if phone is None:
                raise Exception("Phone cant be None!")
            Users().insert_into(
                first_name=kwargs.get('first_name'),
                last_name=kwargs.get('last_name'),
                username=username,
                password=str(generate_password(password)),
                phone=phone,
            )
        else:
            raise Exception("Username and/or phone number is already taken!")

    def __commit(self):
        pass

    def check_username_unique(self, username: str):
        for user in self.users:
            if user['username'] == username:
                return False
            return True

    def check_phone_unique(self, phone):
        for user in self.users:
            if user['phone'] == phone:
                return False
            return True

    def find_user_by_username(self, username):
        found_user = None
        for user in self.users:
            if user['username'] == username:
                found_user = user
        if found_user is None:
            raise Exception("Receiver not found!")
        return found_user


class FinanceService:
    transfers = []

    def __get_data(self):
        data = Transfers().select().fetchall()
        result = []
        if data:
            for item in data:
                dict_item = {
                    "transfer_id": item[0],
                    "sender": item[1],
                    "sender_id": item[2],
                    "receiver": item[3],
                    "receiver_id": item[4],
                    "amount": item[5],
                    "transfer_date": item[6]
                }
                result.append(dict_item)
        self.transfers = result

    def check_balance_enough(self, user: dict, amount):
        if user['balance'] < amount:
            raise FinanceServiceException("Balance is not enough")

    def show_balance(self, user):
        print_info(f"Your balance {user['balance']}")

    def add_balance(self, user, amount):
        user['balance'] += amount

    def transfer_money(self, sender: dict, receiver: dict, amount: float):
        self.check_balance_enough(sender, amount)
        sender['balance'] -= amount
        receiver['balance'] += amount
        sender_id = Users('id').select(username=sender['username']).fetchone()
        receiver_id = Users('id').select(username=receiver['username']).fetchone()
        Transfers().insert_into(
            sender=sender['username'],
            sender_id=sender_id,
            receiver=receiver['username'],
            receiver_id=receiver_id,
            amount=amount,
            transfer_date=datetime.datetime.now()
        )
        print_info('Done✅')

    def transfer_history(self):
        transfers = Transfers().select().fetchall()
        if not transfers:
            print_error("No transfers yet!")
        else:
            for i in transfers:
                print_info(i)
