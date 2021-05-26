import crud
import server
from test_model import connect_to_db

import unittest

class MeIntegrationTestCase(unittest.TestCase):

  def setUp(self):
      """Stuff to do before every test."""

      # Get the Flask test client
      self.client = server.app.test_client()

      # Show Flask errors that happen during tests
      server.app.config['TESTING'] = True
      connect_to_db(server.app, 'postgresql:///test')

  def test_root(self):
    """Test homepage if no user in session."""

    # client = server.app.test_client()
    result = self.client.get('/')
    self.assertIn(b'Not a member', result.data)

  def test_login(self):
    """Test login if user in db."""

    # client = server.app.test_client()
    result = self.client.post('/login', data={"email": "noelle@gmail.com", "password": 'letsdothis'}, follow_redirects=True)

    self.assertIn(b'<h5>Daily inspiration</h5>', result.data)


if __name__ == "__main__":
  unittest.main()