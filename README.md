# Simple Flask Test Application

This application shows a simple way to transfer a data visualization to a custom HTML Template backed by Flask.

# Setup

1. Install Python 3.9.6 in a new environment. You need to have this exact version installed on your system. If the code below does not work. Anything from Python 3.8+ will do.

`python -m venv .venv --python=python3.9.6`

2. Activate the environment. The code below works for bash on linux. Check the manual for different operating systems or shells. I moved the venv into a dotfolder and added this folder to .gitignore. No need to ship all modules with git :-)

`source .venv/bin/activate`

3. Install the dependencies from requirements.txt

`pip install -r requirements.txt`

4. Start the application by running Flask in debug mode:

`flask --app app.py --debug run`

5. Play around with the data an different combinations of templates.

