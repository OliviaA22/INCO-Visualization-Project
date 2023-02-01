# from dotenv import load_dotenv

# load_dotenv()
from flask import Flask, render_template

import json

with open("Data.json") as f:
    data = json.load(f)


def set_location(data):
    left = []
    right = []
    for patient in data:
        if patient['Location'] == 'Left':
            left.append(patient)
        else:
            right.append(patient)
    return data


data = set_location(data)


def set_medication_status(data):
    for patient in data:
        if patient['Given'] == 0:
            patient['Status'] = 'red'
        elif patient['Prescribed'] == patient['Given']:
            patient['Status'] = 'green'
        else:
            patient['Status'] = 'orange'
    return data


data = set_medication_status(data)


app = Flask(__name__)


@app.route('/')
def hospital():
    wards = list(set([patient["Ward"] for patient in data]))
    return render_template(
        "wards.html",
        data=wards,
    )


@app.route('/<string:ward>')
def wards(ward):
    filtered_data = [patient for patient in data if patient["Ward"] == ward]
    sorted_data = sorted(
        filtered_data, key=lambda patient: int(patient["RoomNo"]))
    return render_template(
        "patients.html",
        data=sorted_data,
    )


@app.route('/<string:ward>/details/<int:Room>')
def details(ward, Room):
    patient_data = next(patient for patient in data if patient["Ward"] == ward and patient["RoomNo"] == Room)
    return render_template("details.html", data=patient_data)



if __name__ == "__main__":
    app.run(debug=True)
