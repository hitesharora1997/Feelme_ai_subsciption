import unittest
from app import create_app


class TestSubscriptionAPI(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.client.testing = True

    def test_create_subscription(self):
        response = self.client.post('/api/v1/subscription', json={
            'user_external_id': '123',
            'user_email': 'user@example.com',
            'duration': 1,
            'start_date': '2024-06-29'
        }, headers={'Authorization': 'personalkey'})

        print(f"Response JSON: {response.get_json()}")
        self.assertEqual(response.status_code, 201)
        self.assertIn('subscription_id', response.get_json())

    def test_extend_subscription(self):
        # First, create a subscription
        self.client.post('/api/v1/subscription', json={
            'user_external_id': '123',
            'user_email': 'user@example.com',
            'duration': 1,
            'start_date': '2024-06-29'
        }, headers={'Authorization': 'personalkey'})

        # Then, extend the subscription
        response = self.client.put('/api/v1/subscription', json={
            'user_external_id': '123',
            'duration': 1
        }, headers={'Authorization': 'personalkey'})

        self.assertEqual(response.status_code, 200)
        self.assertIn('new_end_date', response.get_json())

    def test_create_subscription_invalid_date(self):
        response = self.client.post('/api/v1/subscription', json={
            'user_external_id': '124',
            'user_email': 'user@example.com',
            'duration': 1,
            'start_date': 'invalid-date'
        }, headers={'Authorization': 'personalkey'})

        self.assertEqual(response.status_code, 422)

    def test_create_subscription_missing_fields(self):
        response = self.client.post('/api/v1/subscription', json={
            'user_email': 'user@example.com',
            'duration': 1
        }, headers={'Authorization': 'personalkey'})

        self.assertEqual(response.status_code, 422)

    def test_create_subscription_invalid_email(self):
        response = self.client.post('/api/v1/subscription', json={
            'user_external_id': '126',
            'user_email': 'invalid-email',
            'duration': 1,
            'start_date': '2024-06-29'
        }, headers={'Authorization': 'personalkey'})

        self.assertEqual(response.status_code, 422)

    def test_extend_non_existent_subscription(self):
        response = self.client.put('/api/v1/subscription', json={
            'user_external_id': 'non-existent-id',
            'duration': 1
        }, headers={'Authorization': 'personalkey'})

        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
