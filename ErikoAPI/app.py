from flask import Flask
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

@app.route('/ping/<ip>')
def ping(ip):
    import os
    out = os.popen('ping ' + ip).readlines()
    str = out[8]
    try:
        str += out[10]
    except:
        pass
    return str

@app.route('/')
def index():
    return "Eriko API"

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
