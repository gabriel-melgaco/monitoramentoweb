from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
import requests


app = Flask(__name__)

@app.route("/")
def index():
    return 'Hello, World!'


def ping_site():
    try:
        requests.get("https://gerenciamentojaguar.onrender.com")
        requests.get("https://pedrorochaconsultoria.onrender.com")
        print('Request Sent')
    except Exception as e:
        print(f'Error: {e}')

scheduler = BackgroundScheduler()
scheduler.add_job(ping_site, 'interval', minutes=5)
scheduler.start()

if __name__ == '__main__':
    app.run(debug=False)
