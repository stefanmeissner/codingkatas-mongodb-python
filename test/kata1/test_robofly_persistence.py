import unittest
from app.mongo_db_handler import MongoDbHandler

class RoboFlyPersistenceTestCase(unittest.TestCase):
    DATABASE_NAME = "mobilerobotics"
    COLLECTION_NAME = "roboflies"

    def setUp(self):
        self.mongodb_handler = MongoDbHandler(self.__class__.DATABASE_NAME)

    def tearDown(self):
        self.mongodb_handler.drop_database(self.__class__.DATABASE_NAME)

    def test_safe_robofly(self):
        self.assertEqual(self.mongodb_handler.count(self.__class__.COLLECTION_NAME), 0)

        # TODO Robofly Class
        robofly = {"_id": "RoboFly_ID_1",
            "name": "Calliphora",
            "constructionYear": 2014,
            "size": 2,
            "serviceTime": 60,
            "status": "OK"}
        object_id = self.mongodb_handler.insert_one(self.__class__.COLLECTION_NAME, robofly).inserted_id
        self.assertIsNotNone(object_id)

        self.assertEqual(self.mongodb_handler.count(self.__class__.COLLECTION_NAME), 1)

    def test_save_multiple_roboflies(self):
        self.assertEqual(self.mongodb_handler.count(self.__class__.COLLECTION_NAME), 0)

        roboflies = []

        robofly1 = {"_id": "RoboFly_ID_1",
            "name": "Calliphora",
            "constructionYear": 2014,
            "size": 2,
            "serviceTime": 60,
            "status": "OK"}
        roboflies.append(robofly1)

        robofly2 = {"_id": "RoboFly_ID_2",
            "name": "Lucilia",
            "constructionYear": 2014,
            "size": 2,
            "serviceTime": 60,
            "status": "OK"}
        roboflies.append(robofly2)

        robofly3 = {"_id": "RoboFly_ID_3",
            "name": "Onesia",
            "constructionYear": 2014,
            "size": 2,
            "serviceTime": 60,
            "status": "OK"}
        roboflies.append(robofly3)

        object_ids = self.mongodb_handler.insert_many(self.__class__.COLLECTION_NAME, roboflies).inserted_ids
        self.assertIsNotNone(object_ids)

        self.assertEqual(self.mongodb_handler.count(self.__class__.COLLECTION_NAME), 3)
