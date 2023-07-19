import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()


class Db:
    connect = psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port='5432'
    )
    cursor = connect.cursor()

    def select(self, **where):
        fields = ','.join(self.fields) if self.fields else '*'
        table_name = self.__class__.__name__.lower()
        query = f"""select {fields} from {table_name}"""
        if where.keys():
            query += f' where {list(where.keys())[0]} = %s'
        param = tuple(where.values())
        self.cursor.execute(query, param)
        return self.cursor

    def insert_into(self, **params):
        fields = ','.join(params.keys())
        values = tuple(params.values())

        table_name = self.__class__.__name__.lower()
        query = f"""insert into {table_name}({fields}) values ({','.join(['%s'] * len(params))})"""
        self.cursor.execute(query, values)
        self.connect.commit()

    def update(self, **kwargs):
        w = list(self.where.keys())
        w.append(" ")

        table_name = self.__class__.__name__.lower()
        f = list(kwargs.keys())
        f.append(' ')

        set_fields = " = %s,".join(f).strip(', ')
        where_fields = " = %s and ".join(w).strip('and ')

        params = list(kwargs.values())
        params.extend(list(self.where.values()))

        query = f"""update {table_name} set {set_fields} where {where_fields}"""
        self.cursor.execute(query, params)
        self.connect.commit()
