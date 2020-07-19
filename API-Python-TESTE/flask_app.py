
activate_this = '/home/elder/env/bin/activate_this.py'
with open(activate_this) as file_:
	exec(file_.read(), dict(__file__=activate_this))


# This file contains the WSGI configuration required to serve up your
# web application at http://<your-username>.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#
# The below has been auto-generated for your Flask project

import sys, os
from dotenv import load_dotenv

# add your project directory to the sys.path
project_home = u'/home/elder/BackHackaZenvia/BackEnd'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

project_folder = os.path.expanduser(project_home)  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))

# import flask app but need to call it "application" for WSGI to work
#from flask_app import app as application  # noqa
#from app import app as application
from app.RunOnServer import app as application
