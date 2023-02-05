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

       
