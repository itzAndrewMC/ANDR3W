from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Heya! ANDR3W is now online and running | Join my support server if there is any issues / bugs : https://discord.gg/JdTDVhVnNW"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()