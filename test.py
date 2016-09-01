# UNIT TEST:
# check to see if the map gets displayed.



# INTEGRATION TEST:START WITH THESE TESTS FIRST!!
# test to see if the route function return the right html.
# test to see URL path maps to the right functions?
# test if the route shows up for start and end.
# test if user can log in.

# NOTE: integration test is written with unittest.


# FUNCTIONAL TEST:
# Does it work in a real browser?

import json
from unittest import TestCase
from model import User, Trip, GasStation, connect_to_db, db, example_data
import server



from server import app

#############  TESTING HOMEPAGE ########################

class FlaskTestsBasic(TestCase):
    """Flask tests."""
# what are the specific task requirements for this test?
    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client. Client is the browser.
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True

    def test_homepage(self):
        """Test homepage"""
        result = self.client.get("/")
        self.assertIn("Login", result.data)

    def tearDown(self):
        """Stuff to do after each test."""

        pass





######################### MUST CREATE A FAKE DATABASE? ##############


class FlaskTestsDatabase(TestCase):
    """Flask tests that use the database."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()
        app.config['TESTING'] = True

        # Connect to test database
        connect_to_db(app, "postgresql:///testdb")

        # Create tables and add sample data
        db.create_all()
        example_data()

    def tearDown(self):
        """Do at end of every test."""

        db.session.close()
        db.drop_all()


    def test_login(self):
        """Test login page."""
        result = self.client.post("/log_in", 
                                data={"email": "zahra@gmail.com", "password": "hackbright"},
                                follow_redirects=True)
        self.assertIn("start", result.data)

class FlaskTestsLoggedIn(TestCase):
    def setUp(self):
        """Stuff to do before every test."""

        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'key'
        self.client = app.test_client()

        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = 1

    def test_destination_form(self):
        """Test destination page."""
        result = self.client.get("/destination-form", 
                            query_string={"start": "start", "end": "end"},
                            follow_redirects=True)
        self.assertIn("Start Location:", result.data)



    def test_map_display(self):
        """Test destination page."""
        result = self.client.get("/destination-form", 
                                query_string={"start": "start", "end": "end"},
                                follow_redirects=True)
        # result = self.client.get('/destination-process')
        self.assertIn("start", result.data)


class FlaskTestsLoggedOut(TestCase):
    """Flask tests with user logged in to session."""

    def setUp(self):
        """Stuff to do before every test."""

        app.config['TESTING'] = True
        self.client = app.test_client()

        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = 1

    def test_log_out(self):

        result = self.client.get("/logout", follow_redirects=True)
        self.assertIn("Login", result.data)

    def test_important_page(self):
        """Test that user can't see important page when logged out."""

        result = self.client.get("/", follow_redirects=True)
        self.assertIn("Email", result.data)




if __name__ == "__main__":
    import unittest

    unittest.main()

  



