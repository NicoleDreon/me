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
    self.assertIn(b'<p>Not a member, <a href="/sign_up">sign up</a>.</p>', result.data)

  def test_login(self):
    """Test login if user in db."""

    # client = server.app.test_client()
    result = self.client.post('/login', data={"email": "noelle@gmail.com", "password": 'letsdothis'}, follow_redirects=True)

    self.assertIn(b'<li><a href="/logout">Logout</a></li>', result.data)

  def test

class CheckLoginTestCase(unittest.TestCase):
  """Unit test to test check_login fuction."""
  
  def setUp(self):
      """Stuff to do before every test."""

      # Get the Flask test client
      self.client = server.app.test_client()

      # Show Flask errors that happen during tests
      server.app.config['TESTING'] = True
      connect_to_db(server.app, 'postgresql:///test')

  def test_check_login(self):
    """."""

    assert crud.check_login('noelle@gmail.com') == '< User user_id = 1 fname = Noelle lname = Smith email = noelle@gmail.com, phone=None password = letsdothis dob = 1982-09-12 00:00:00 gender = Female >'


if __name__ == "__main__":
  unittest.main()