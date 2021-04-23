# import crud
import server

import unittest

class MeIntegrationTestCase(unittest.TestCase):

  def test_root(self):
    client = server.app.test_client()
    result = client.get('/')
    self.assertIn(b'<p>Not a member, <a href="/sign_up">sign up</a>.</p>', result.data)


# class CheckLoginTestCase(unittest.TestCase):
#   """Unit test to test check_login fuction."""

#   def test_check_login(self):
#     assert crud.check_login('noelle@gmail.com', 'letsdothis') == 


if __name__ == "__main__":
  unittest.main()