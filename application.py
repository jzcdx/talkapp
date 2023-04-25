"""
from flask import Flask, render_template
application = Flask(__name__)

@application.route('/')
def hello_world():
    return render_template("index.html")

if __name__ == "__main__":
    application.run(debug=True, use_reloader=True, threaded=True)
"""
from flask import Flask, render_template
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)


@app.route('/')
def index():
    return render_template('index.html')


@sock.route('/echo')
def echo(sock):
    while True:
        data = sock.receive()
        sock.send(data + " asd")

app.run()