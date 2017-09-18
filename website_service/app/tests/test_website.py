from flask_testing import TestCase
from app import app, mongo


class TestUserService(TestCase):
    """Tests for the Users Service."""

    def create_app(self):
        app.config.from_object('app.config.TestingConfig')
        return app

    def test_default_settings(self):
        self.assertEqual(mongo.db.settings.find_one()['api_url'], 'http://127.0.0.1:5001')

    def test_get_site(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_static_js(self):
        response = self.client.get('/static/js/base.js')
        self.assertEqual(response.status_code, 200)

    def test_static_css(self):
        response = self.client.get('/static/css/base.css')
        self.assertEqual(response.status_code, 200)
