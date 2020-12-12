# import datetime
# from peewee import *
# from flask_login import UserMixin

# DATABASE = PostgresqlDatabase('showaholic')

# class User(UserMixin, Model):
#     username = CharField(unique = True)
#     password = CharField()
#     email = CharField(unqiue = True)
    
#     class Meta:
#         database = DATABASE

# def initialize():
#     DATABASE.connect()
#     DATABASE.create_tables([User], safe = True)
#     print('Tables Created')
#     DATABASE.close()