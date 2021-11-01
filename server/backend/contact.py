import requests, os
from flask import request

def sendmail():
  name = request.args.get('name')
  email = request.args.get('email')
  topic = request.args.get('topic')
  message = request.args.get('message')

  return requests.post(
    os.getenv('mailgun_url'),
    auth=("api", os.getenv('mailgun_api_key')),
    data={"from": os.getenv('mailgun_from'),
      "to": "Gustav Andersson <gustav87and@gmail.com>",
      "subject": f'From {name} on gstav.se',
      "text": f'Name: {name}\nEmail: {email}\nTopic: {topic}\nMessage: {message}'})
