import unittest
from app.mongo_db_handler import MongoDbHandler
from app.kata1.robofly import Robofly
from app.kata1.robofly_object_mapper import encode_robofly

class RoboFlyPersistenceTestCase(unittest.TestCase):
    DATABASE_NAME = "mobilerobotics"
    COLLECTION_NAME = "roboflies"

    def setUp(self):
        self.mongodb_handler = MongoDbHandler(self.__class__.DATABASE_NAME)

    def tearDown(self):
        self.mongodb_handler.drop_database(self.__class__.DATABASE_NAME)

    def test_safe_robofly(self):
        self.assertEqual(self.mongodb_handler.count(self.__class__.COLLECTION_NAME), 0)

        robofly = Robofly(
            robofly_id="RoboFly_ID_1",
            name="Calliphora",
            construction_year=2014,
            size=2,
            service_time=60,
            status="OK")

        robofly_document = encode_robofly(robofly)

        object_id = self.mongodb_handler.insert_one(self.__class__.COLLECTION_NAME, robofly_document).inserted_id
        self.assertIsNotNone(object_id)

        self.assertEqual(self.mongodb_handler.count(self.__class__.COLLECTION_NAME), 1)

    def test_save_multiple_roboflies(self):
        self.assertEqual(self.mongodb_handler.count(self.__class__.COLLECTION_NAME), 0)

        roboflies = []

        robofly1 = Robofly(
            robofly_id="RoboFly_ID_1",
            name="Calliphora",
            construction_year=2014,
            size=2,
            service_time=60,
            status="OK")
        roboflies.append(encode_robofly(robofly1))

        robofly2 = Robofly(
            robofly_id="RoboFlRoboFly_ID_2y_ID_1",
            name="Lucilia",
            construction_year=2014,
            size=2,
            service_time=60,
            status="OK")
        roboflies.append(encode_robofly(robofly2))

        robofly3 = Robofly(
            robofly_id="RoboFly_ID_3",
            name="Onesia",
            construction_year=2014,
            size=2,
            service_time=60,
            status="OK")
        roboflies.append(encode_robofly(robofly3))

        object_ids = self.mongodb_handler.insert_many(self.__class__.COLLECTION_NAME, roboflies).inserted_ids
        self.assertIsNotNone(object_ids)

        self.assertEqual(self.mongodb_handler.count(self.__class__.COLLECTION_NAME), 3)
