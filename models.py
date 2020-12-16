from peewee import *
import datetime

DATABASE = PostgresqlDatabase('showaholic')

class Watchlist(Model):
    title = CharField()
    authour = CharField()
    watchlist_id = PrimaryKeyField()
    class Meta:
        database = DATABASE

class Show(Model):
    show_id = PrimaryKeyField()
    title = CharField()
    where_to_watch = CharField()
    genre = CharField()
    cover = CharField()
    release_date = CharField()
    runtime = CharField()
    synopsis = CharField()
    watchlist_id = ForeignKeyField(Watchlist, to_field="watchlist_id")
    
    class Meta: 
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Watchlist, Show], safe=True)
    print('TABLES Created')
    DATABASE.close()