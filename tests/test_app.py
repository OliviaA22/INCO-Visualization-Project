import unittest
from flask import url_for
from flask import Flask
from flask_testing import TestCase
from app import create_app



class TestFlaskApp(unittest.TestCase):

    # Creates an instance of Flask app for testing
    def create_app(self):
        self.app = create_app()
        self.client = self.app.test_client()
        return self.app

    def test_wards(self):
          # Tests the '/' endpoint, which should return a 200 status code
        response = self.client.get('/')
        self.assert200(response)

    def test_patients(self):
          # Tests the '/<string:ward>' endpoint, which should return a 200 status code
        response = self.client.get('/<string:ward>')
        self.assert200(response)

    def test_details(self):
              # test code for the '/<string:ward>/details/<int:Room>' route
        response = self.client.get('/<string:ward>/details/<int:Room>')
        self.assert200(response)

    def test_display_ward_data(self, ward):
      # Tests the display_ward_data() function, which should return a 200 status code and display the ward name and "rooms"
        response = self.client.get(url_for('/', ward=ward))
        self.assertEqual(response.status_code, 200)
        self.assertIn(f"Welcome to {ward} department", response.data.decode())
        self.assertIn("rooms", response.data.decode())


    def test_display_patient_data(self, ward):
    # Tests the display_patient_data() function, which should return a 200 status code and display patient name, ID, and status
        response = self.client.get(url_for('/', ward=ward))
        self.assertEqual(response.status_code, 200)
        self.assertIn("FirstName", response.data.decode())
        self.assertIn("PatientID", response.data.decode())


    def test_display_patient_data(self, ward_name):
    # Tests the display_patient_data() function, which should return a 200 status code and display patient name, ID, and status
        response = self.client.get(url_for('/', ward=ward_name))
        self.assertEqual(response.status_code, 200)



    def test_patient_details_url(self, patient_id):
    # Tests the patient_details_url() function, which should return a 200 status code and display the URL for the patient details page
        response = self.client.get(url_for('details', patient_id=patient_id))
        self.assertEqual(response.status_code, 200)
        self.assertIn(f"/details/{patient_id}", response.data.decode())

    def test_patient_details_data(self, patient_id):
          # Tests the patient_details_data() function, which should return a 200 status code and display patient name, ID, and status
        response = self.client.get(url_for('details', patient_id=patient_id))
        self.assertEqual(response.status_code, 200)
        self.assertIn("FirstName", response.data.decode())
        self.assertIn("PatientID", response.data.decode())

    def test_direct_access_patient_details(self, patient_id):
          # Tests to check if the details can be directly accessed, which should return a 401 status code
        response = self.client.get(url_for('details', patient_id=patient_id))
        self.assertEqual(response.status_code, 401)
        self.assertIn("You are not authorized to view this page directly.", response.data.decode())


if __name__ == '__main__':
    unittest.main()
    

'''
class TestPatientDetails(unittest.TestCase):
    def setUp(self):
        # Set up the test client and populate the data that will be used in the tests
        self.app = self.app.test_client()
        self.data = [{'RoomNo': 1, 'LastName': 'Smith', 'FirstName': 'John', 'Prescribed': 3, 'Status': 'green'},
                     {'RoomNo': 2, 'LastName': 'Doe', 'FirstName': 'Jane', 'Prescribed': 2, 'Status': 'yellow'},
                     {'RoomNo': 3, 'LastName': 'Brown', 'FirstName': 'Bob', 'Prescribed': 1, 'Status': 'red'}]
        
    def test_index_page_loads(self):
        # Test that the index page loads without errors
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_patient_details_page_loads(self):
        # Test that the patient details page loads without errors
        response = self.app.get('/details/1')
        self.assertEqual(response.status_code, 200)
        
    def test_patient_details_correct(self):
        # Test that the patient details displayed on the page are correct
        response = self.app.get('/details/1')
        patient = [patient for patient in self.data if patient['RoomNo'] == 1][0]
        self.assertIn(patient['LastName'].encode(), response.data)
        self.assertIn(patient['FirstName'].encode(), response.data)
        self.assertIn(str(patient['Prescribed']).encode(), response.data)
        self.assertIn(patient['Status'].encode(), response.data)
        
if __name__ == '__main__':
    unittest.main()
'''


# In the above code, the unittest module is imported, and a test class TestPatientDetails is defined. The test class is derived from unittest.TestCase.

# In the setUp method, the test client is created, and the data that will be used in the tests is populated. The app.test_client() method creates a test client that allows you to send HTTP requests to your Flask application and receive the response, without actually running the application in a web server.

# The test_index_page_loads method tests that the index page loads without errors by sending a GET request to the '/' endpoint and checking the status code of the response.

# The test_patient_details_page_loads method tests that the patient details page loads without errors by sending a GET request to the '/details/1' endpoint and checking the status code of the response.

# The test_patient_details_correct method tests that the patient details displayed on the page are correct by sending a GET request to the '/details/1' endpoint, retrieving the patient data from the self.data list, and checking that the patient's last name, first name, prescribed medication,
