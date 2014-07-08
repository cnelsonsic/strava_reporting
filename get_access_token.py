from stravalib.client import Client

from flask import Flask, request, redirect

from config import *

app = Flask(__name__)

client = Client()

@app.route("/")
@app.route("/authorized")
def index():
    authorize_url = client.authorization_url(client_id=CLIENT_ID, redirect_uri='http://localhost:8282/authorized')
    print "Click this url:", authorize_url
    code = request.args.get('code')
    if code:
        access_token = client.exchange_code_for_token(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, code=code)
        with open("access_token.py", 'w') as f:
            f.write("ACCESS_TOKEN='{}'\n\n".format(access_token))
        return "Access token acquired. You're ready to roll!"
    else:
        return redirect(authorize_url)

app.run(port=8282, host='0.0.0.0', debug=True)
