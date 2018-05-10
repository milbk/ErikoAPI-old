from flask import Flask
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

@app.route('/ping/<ip>')
def ping(ip):
    import os
    import platform
    if platform.system() == 'Windows':
        out = os.popen('psping -n 8 -w 2 ' + ip).readlines()
    else:
        out = os.popen('ping -w 8 ' + ip).readlines()

    line = out[len(out) - 2] + out[len(out) - 1]
    return line

@app.route('/tcping/<ip>:<port>')
def tcping(ip,port):
    import os
    import platform
    if platform.system() == 'Windows':
        out = os.popen('psping -n 8 -w 2 ' + ip + ':' + port).readlines()
        line = out[len(out) - 2] + out[len(out) - 1]
    else:
        out = os.popen('tcping -x 8 -C ' + ip + ' ' + port).readlines()
        line = out[len(out) - 1]
    return line

@app.route('/')
def index():
    return 'Eriko API'

@app.route('/myip')
def myip():
    from flask import request
    return request.remote_addr

if __name__ == '__main__':
    print('Eriko Network API')
    print('Running')
    import os
    HOST = os.environ.get('SERVER_HOST', '0.0.0.0')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
