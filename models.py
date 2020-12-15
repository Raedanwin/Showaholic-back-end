from peewee import *
import datetime

DATABASE = PostgresqlDatabase('showaholic')

class Watchlist(Model):
    title = CharField()
    authour = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Watchlist], safe=True)
    print('TABLES Created')
    DATABASE.close()