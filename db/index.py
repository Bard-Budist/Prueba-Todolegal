import mysql.connector
from decouple import config

class Db:
    """
    Class for control operation in data base 
    """
    cursor = None
    conn = None

    def __init__(self):
        self.conn = mysql.connector.connect(
            user=config('USER'), 
            password=config('PASSWORD'),
            host=config('HOST'),
            database=config('DATA_BASE'), port=config('PORT'))

        self.cursor = self.conn.cursor()

    def insert(self, value, date):
        """
        Insert in table
        """
        query =  "INSERT INTO cambio (value_cambio, fecha) VALUES ({}, '{}');".format(float(value), date)
        self.cursor.execute(query)
        self.save()
        
    def get(self, limit):
        """
        Get data in table cambios with limit
        """
        query = "SELECT value_cambio, fecha FROM cambio LIMIT {}".format(limit)
        self.cursor.execute(query)
        result = (self.cursor.fetchall())
        data = []
        for item in result:
            print(item)
            data.append(item)
        return data

    def all(self):
        """
        Get all data in table
        """
        query = "SELECT value_cambio, fecha FROM cambio"
        self.cursor.execute(query)
        result = (self.cursor.fetchall())
        data = []
        for item in result:
            print(item)
            data.append(item)
        return data

    def save(self):
        """
        Save changes in Database
        """
        self.conn.commit()

