from peewee import *

# Define a database object
db = SqliteDatabase('/tmp/my_database.db')

# Define a model class
class Person(Model):
    name = CharField()
    age = IntegerField()

    class Meta:
        database = db

# Create the table in the database
db.connect()
db.create_tables([Person])