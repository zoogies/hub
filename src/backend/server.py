# imports
import psutil
import requests
from flask import Flask
from flask_cors import CORS

# create flask app
app = Flask(__name__, static_folder='filmfest/server')

# cors-ify the app
CORS(app)

# set the public ip address
ip=requests.get('https://api64.ipify.org?format=json').json()['ip']

# api route for getting server statistics
@app.route('/api/getstats')
def admin():
    return {
        #"user":str(os.getlogin()),
        "ip":ip,
        "boot-time":round(psutil.boot_time()),
        "cpu-count":psutil.cpu_count(),
        "load-average":psutil.cpu_percent(interval=None),
        "memory":{
            "total":round(psutil.virtual_memory().total * 0.000000001,2),
            "used":round(psutil.virtual_memory().used * 0.000000001,2),
            "percent":psutil.virtual_memory().percent,
        },
        "swap":{
            "total":round(psutil.swap_memory().total * 0.000000001,2),
            "used":round(psutil.swap_memory().used * 0.000000001,2),
           "percent":psutil.swap_memory().percent,
        },
        "disk":{
            "total":round(psutil.disk_usage('/').total * 0.000000001,2),
            "used":round(psutil.disk_usage('/').used * 0.000000001,2),      
            "percent":psutil.disk_usage('/').percent
        }
    }

# run the server on port 5000 locally
if __name__ == '__main__':
    app.run(host='127.0.0.1', use_reloader=True, port=5000, threaded=True, debug=True)
