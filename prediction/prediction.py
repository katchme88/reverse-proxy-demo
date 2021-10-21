from flask import Flask
app = Flask(__name__)
import socket

port = 5000
@app.route("/")
def hello_world():

    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return f"<h1>Prediction is running on IP <i>{local_ip}</i> & Port <i>{port}</i></h1>"

if __name__=="__main__":
    app.run(debug=True, port=port, host="0.0.0.0")