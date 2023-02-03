# from dotenv import load_dotenv

# load_dotenv()
from flask import Flask, render_template
from collections import defaultdict

import json

with open("Data.json") as f:
    data = json.load(f)



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
    # wards = list(set([patient["Ward"] for patient in data]))
    wards = list(set([patient["Ward"]
                 for patient in data if type(patient["Ward"]) == str]))
    return render_template(
        "wards.html",
        data=wards,
    )


@app.route('/<string:ward>')
def wards(ward):
    filtered_data = [patient for patient in data if patient["Ward"] == ward]
    room_dict = defaultdict(list)
    for patient in filtered_data:
        room_dict[patient["RoomNo"]].append(patient)
    sorted_room_dict = dict(
        sorted(room_dict.items(), key=lambda item: int(item[0])))
    return render_template(
        "patients.html",
        room_dict=sorted_room_dict,
        data=filtered_data,
    )


# @app.route('/<string:ward>/details/<int:Room>')
# def details(ward, Room):
#     patient_data = next(patient for patient in data if patient["Ward"] == ward and patient["RoomNo"] == Room)
#     return render_template("details.html", data=patient_data)

@app.route('/<string:ward>/details/<int:Room>')
def details(ward, Room):
    patients_data = [patient for patient in data if patient["Ward"] == ward and patient["RoomNo"] == Room]
    return render_template("details.html", data=patients_data)


# @app.route('/string:ward/details/<int:Room>/<string:patient_id>')
# def details(ward, Room, patient_id):
#     patients_in_room = [patient for patient in data if patient["Ward"]== ward and patient["RoomNo"] == Room]
#     patient_data = next(patient for patient in patients_in_room if patient["Patient ID"] == patient_id)
#     return render_template("details.html", data=patient_data)


if __name__ == "__main__":
    app.run(debug=True)
