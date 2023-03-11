
import unittest
from dotenv import load_dotenv
from flask_starterkit.main.config import create_app


# def test_auth_endpoint():
#     test_runner = get_client_instance()
#     response = test_runner.get("/api/auth/")
#     assert response.status_code == 200


class TestAuthRoutes(unittest.TestCase):
    def setUp(self) -> None:
        # load_dotenv(dotenv_path="../../../../.env")
        load_dotenv()
        self.client = create_app().test_client()
        # return super().setUp()

    def test_auth_global_endpoint(self):
        print("DO YOU SEE ME ?")
        auth_endpoint_request = self.client.get('/api/auth/')
        self.assertDictEqual(auth_endpoint_request.json, {
            "message": "Welcome to your awesome auth endpoint", "success": True})


if __name__ == '__main__':
    unittest.main()
