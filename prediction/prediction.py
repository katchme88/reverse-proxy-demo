from flask import Flask
app = Flask(__name__)

port = 5000
@app.route("/")
def hello_world():
    return f"<h1>Prediction is running on port <i>{port}</i></h1>"

if __name__=="__main__":
    app.run(debug=True, port=port, host="0.0.0.0")