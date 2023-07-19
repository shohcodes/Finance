from psycopg2 import *
from os import getenv
from dotenv import load_dotenv

load_dotenv()

conn = connect(
    host=getenv("DB_HOST"),
    database=getenv('DB_NAME'),
    user=getenv("DB_USER"),
    password=getenv("DB_PASSWORD")
)
cur = conn.cursor()
cur.execute("create table if not exists users(id serial primary key , first_name varchar(255),"
            "last_name varchar(255), username varchar(255) unique , password varchar(255),"
            " phone integer unique,"
            " balance float4 default 0)")

cur.execute("create table if not exists transfers(transfer_id serial primary key, sender varchar(255),"
            " sender_id integer,"
            "receiver varchar(255), receiver_id integer, amount float8, transfer_date timestamp,"
            "foreign key (sender_id) references users(id),"
            "foreign key (receiver_id) references users(id))")

conn.commit()
