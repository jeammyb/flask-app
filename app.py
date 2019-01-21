from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')    


@app.route('/hello/<string:name>', methods=['GET'])
def hello(name):
    return render_template('hello.html', message=f'Hello {name}')    


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
