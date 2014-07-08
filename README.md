If you want to run this for yourself, you'll need to create an app in strava.
Put your client id and client secret in a file `config.py` like so:

```python
CLIENT_ID = 1234
CLIENT_SECRET = 'deadbeefdeadbeefdeadbeefdeadbeefdeadbeef'
```

Then run `get_access_token.py`, and visit http://localhost:8282
It will redirect a couple times, then it will generate an `access_token.py` file.

Now run `main.py`, which will generate a fitness form. Easy peasy.

If you don't want to run it for yourself and you'll actually use it, shoot me a message and I'll turn this into a proper webapp.
