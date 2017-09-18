import json
from flask_testing import TestCase
from api import app


class TestUserService(TestCase):
    """Tests for the Users Service."""

    def create_app(self):
        app.config.from_object('config.TestingConfig')
        return app

    def test_add(self):
        response = self.client.post('/users',
                                    data=json.dumps({'name': 'John Lemon'}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_add2(self):
        response = self.client.post('/users',
                                    data=json.dumps({'name': 'John Smith'}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_add_empty(self):
        response = self.client.post('/users',
                                    data=json.dumps({'name': ''}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_add_wrong(self):
        response = self.client.post('/users',
                                    data=json.dumps({'no_name': 'nobody'}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_add_none(self):
        response = self.client.post('/users')
        self.assertEqual(response.status_code, 400)

    def test_get_users(self):
        response = self.client.get('/users')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertItemsEqual(data.values(), ['John Lemon', 'John Smith'])
        self.remove_id = data.keys()[0]  # Used in next test.

    def test_remove_user(self):
        response = self.client.get('/users')

        response = self.client.get('/users/' + data.keys()[0])
        self.assertEqual(response.status_code, 204)
