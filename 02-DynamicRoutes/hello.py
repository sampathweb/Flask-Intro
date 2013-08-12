from flask import Flask
app = Flask(__name__)

@app.route('/index/<name>')
def index(name):
    return '<h1>Hello, %s!</h1>' % name

if __name__ == '__main__':
    app.run(debug = True)

