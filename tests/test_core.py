import unittest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from importlib import import_module
from utils import find_package_name

class TestCore(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pkg_name = find_package_name()
        cls.core = import_module(f"{cls.pkg_name}")
        cls.router = cls.core.router
        cls.prefix = cls.core.prefix

        cls.app = FastAPI()
        cls.app.include_router(
            cls.router,
            prefix=f"/api/{cls.prefix}"
        )
        cls.client = TestClient(cls.app)

    def test_read_main(self):
        response = self.client.get(f"/api/{self.prefix}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["detail"], "OK")

    def test_create_user(self):
        user_data = {"email": "test@example.com", "password": "password123", "privilege": "user"}
        response = self.client.post(f"/api/{self.prefix}/users/", json=user_data)
        self.assertEqual(response.status_code, 200)
        json_dict = response.json()
        self.assertEqual(json_dict["message"], "User created successfully")
        self.assertEqual(json_dict["detail"]["email"], user_data["email"])
        self.assertEqual(json_dict["detail"]["privilege"], user_data["privilege"])

    def test_create_conversation(self):
        # First create a user
        user_data = {"email": "test_conv@example.com", "password": "password123", "privilege": "user"}
        user_response = self.client.post(f"/api/{self.prefix}/users/", json=user_data)
        user_id = user_response.json()["detail"]["id"]

        # Then create conversation
        conv_data = {"title": "Test Conversation", "description": "Test Description", "creator_id": user_id}
        response = self.client.post(f"/api/{self.prefix}/conversations/", json=conv_data)
        self.assertEqual(response.status_code, 200)
        json_dict = response.json()
        self.assertEqual(json_dict["message"], "Conversation created successfully")
        self.assertEqual(json_dict["detail"]["title"], conv_data["title"])
        self.assertEqual(json_dict["detail"]["creator_id"], user_id)

    def test_list_users(self):
        # Create a test user
        user_data = {"email": "test_list@example.com", "password": "password123", "privilege": "user"}
        self.client.post(f"/api/{self.prefix}/users/", json=user_data)

        # Test listing
        response = self.client.get(f"/api/{self.prefix}/users/")
        self.assertEqual(response.status_code, 200)
        json_dict = response.json()
        self.assertEqual(json_dict["message"], "Users retrieved successfully")
        self.assertIsInstance(json_dict["detail"], list)
        self.assertTrue(len(json_dict["detail"]) > 0)

    def test_list_conversations(self):
        # Create test data
        user_data = {"email": "test_conv@example.com", "password": "password123", "privilege": "user"}
        user_response = self.client.post(f"/api/{self.prefix}/users/", json=user_data)
        user_id = user_response.json()["detail"]["id"]
        
        conv_data = {"title": "Test Conversation", "description": "Test Description", "creator_id": user_id}
        self.client.post(f"/api/{self.prefix}/conversations/", json=conv_data)

        # Test listing
        response = self.client.get(f"/api/{self.prefix}/conversations/")
        self.assertEqual(response.status_code, 200)
        json_dict = response.json()
        self.assertEqual(json_dict["message"], "Conversations retrieved successfully")
        self.assertIsInstance(json_dict["detail"], list)
        self.assertTrue(len(json_dict["detail"]) > 0)