from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

class MongoDbHandler:
    def __init__(self, database_name):
        self.client = MongoClient()
        try:
            # The ismaster command is cheap and does not require auth.
            self.client.admin.command('ismaster')
        except ConnectionFailure:
            print("Server not available, exit")
            raise SystemExit

        self.db = self.client[database_name]
        print ("Connection to MongoDb established.")
    
    def drop_database(self, database_name):
        self.client.drop_database(database_name)

    def insert_one(self, collection, document):
        return self.db[collection].insert_one(document)

    def insert_many(self, collection, documents):
        return self.db[collection].insert_many(documents)

    def count(self, collection):
        return self.db[collection].count()
