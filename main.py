from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return 'Hello, World!'

def ping_site():
    urls = ["https://gerenciamentojaguar.onrender.com", "https://pedrorochaconsultoria.onrender.com", "https://gremiofalcao.onrender.com"]
    headers = {'User-Agent': 'Mozilla/5.0'}  # Adicionando cabeçalhos para simular uma requisição legítima

    for url in urls:
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                print(f'Request successful for {url}')
            else:
                print(f'Failed request for {url}, Status code: {response.status_code}')
        except Exception as e:
            print(f'Error pinging {url}: {e}')

scheduler = BackgroundScheduler()
scheduler.add_job(ping_site, 'interval', minutes=3)  # Ajustar o intervalo conforme necessário
scheduler.start()

if __name__ == '__main__':
    app.run(debug=False)
