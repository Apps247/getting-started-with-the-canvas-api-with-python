import dotenv
import os
import canvasapi

env_file = 'sample.env'
dotenv.load_dotenv(env_file)

TOKEN = os.environ.get('CANVAS_API_TOKEN')
BASEURL = 'https://ubc.instructure.com'

canvas_api = canvasapi.Canvas(BASEURL, TOKEN)

user = canvas_api.get_user('self')
print(type(user))
print("Welcome, " + user.name)

course = canvas_api.get_course(123413)


users = course.get_users()
for user in users:
    print(user.name)
