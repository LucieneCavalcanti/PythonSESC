from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Minha página</h1><p>Hello, World!</p>"
app.run()