import datetime

from exceptions import UnauthorizedException, FinanceServiceException
from models import Users, Transfers
from utils import print_info, generate_password, match_password, print_success

session_user: dict = None


class AuthService:
    def get_data(self):
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
        return result

    def login(self, username: str, password: str):
        users = self.get_data()
        login_user: dict = None
        for user in users:
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
            if username == '':
                raise Exception("Username cant be None!")
            password = kwargs.get('password')
            if password == '':
                raise Exception("Password cant be None!")
            phone = kwargs.get('phone')
            if phone == '':
                raise Exception("Phone cant be None!")
            Users().insert_into(
                first_name=kwargs.get('first_name'),
                last_name=kwargs.get('last_name'),
                username=username,
                password=str(generate_password(password)),
                phone=phone,
            )
        else:
            raise UnauthorizedException("Username and/or phone number is already taken!")

    def check_username_unique(self, username: str):
        users = self.get_data()
        users_list = [user.get('username') for user in users]
        return False if username in users_list else True

    def check_phone_unique(self, phone):
        users = self.get_data()
        phones_list = [phone.get('phone') for phone in users]
        return False if phone in phones_list else True

    def find_user_by_username(self, username):
        users = self.get_data()
        found_user = None
        for user in users:
            if user['username'] == username:
                found_user = user
        if found_user is None:
            raise UnauthorizedException("Receiver not found!")
        return found_user


class FinanceService:
    def get_data(self):
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
        return result

    def check_balance_enough(self, user: dict, amount):
        if user['balance'] < amount:
            raise FinanceServiceException("Balance is not enough")

    def show_balance(self, user):
        print_info(f"Your balance: {user['balance']}")

    def add_balance(self, user, amount):
        user['balance'] += amount
        print_success('Done✅')

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
        print_success('Done✅')

    def transfer_history(self, sender_id):
        transfers = Transfers().select(sender_id=sender_id).fetchall()
        if transfers:
            for i in transfers:
                print("Transfer ID:", i[0],
                      'Sender:', i[1],
                      'Receiver:', i[3],
                      'Amount:', i[5],
                      'Date:', i[6])
        else:
            print_info('No transfers yet!')


