from flask import Flask

app = Flask (__name__)

@app.get("/")
def index():
    me = {
        "first_name": "John",
        "last_name": "Doe",
        "is_online": True,
        "hobbies": "DIY stuff"
    }

    return me