from config import Db


class Users(Db):
    def __init__(self, *fields):
        self.fields = fields


class Transfers(Db):
    def __init__(self, *fields):
        self.fields = fields
