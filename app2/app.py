from flask import Flask
app = Flask(__name__)

@app.route('/app2')
def index():
    return "Hello from App 2!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


