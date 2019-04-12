from flask import Flask, render_template, send_from_directory,url_for,redirect
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)
@app.route('/js/<path:filename>')
def serve_static(filename):
    url=url_for('static',filename=os.path.join('js',filename))
    return redirect(url)

@app.route("/")
def hello():
    # try:
    #     visits = redis.incr("counter")
    # except RedisError:
    #     visits = "<i>cannot connect to Redis, counter disabled</i>"

    # html = "<h3>Hello {name}!</h3>" \
    #        "<b>Hostname:</b> {hostname}<br/>" \
    #        "<b>Visits:</b> {visits}"
    # return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)