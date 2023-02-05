# Simple Flask Test Application

This application shows a simple way to transfer a data visualization to a custom HTML Template backed by Flask.

## Problem Statement

This is about developing a tool that can reduce the nurses’ workload and stress and provide a better overview so that all important information, such as drug intolerances, are quickly noticed and taken into consideration. Thus, improving the quality of treatment and safety for patients.

The goal is to develop a digital "Medication Management Tool" in which, on the one hand, it is possible to see immediately during the shift handover whether a patient's medications have been completely administered, partially or not administered during a shift. Secondly, there is need for the existing analog medication schedule to be digitized. Up until now, all medications to be administered, intolerances, and previous illnesses have been recorded in the so-called "curve sheet," which can be found in the patient's file and is still available in paper form in many hospitals, and there is no overview for the shift handover that clearly show whether the administration of medication has been completed during a shift or whether the next shift still had to administer that medication. Since medication is a very crucial part of treatment, where forgetting or overdosing medication can have serious consequences for patients safety and health, this project would serve as an avenue to help improve efficiency and productivity for the nursing staff, who already have too much responsibility.

## Setup

1. Install Python 3.9.6 in a new environment. You need to have this exact version installed on your system. If the code below does not work. Anything from Python 3.8+ will do.

`python -m venv .venv --python=python3.9.6`

2. Activate the environment. The code below works for bash on linux. Check the manual for different operating systems or shells. I moved the venv into a dotfolder and added this folder to .gitignore. No need to ship all modules with git :-)

`source .venv/bin/activate` or `environment_name\Scripts\activate`' (depending on your operating system)

3. Install the dependencies from requirements.txt

`pip install -r requirements.txt`

4. Start the application by running Flask in debug mode:

`flask --app app.py --debug run`

5. Play around with the data and different combinations of templates.

