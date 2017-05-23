from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', title="Home page", name="Hello")
    elif request.method == 'POST':
        return render_template('index.html', title='Home post result', name='hello result')


@app.route('/about')
def about():
    return render_template('about.html', title="About page")


@app.route('/contacts')
def contacts():
    return render_template('contacts.html', title="Contacts page")


if __name__ == '__main__':
    app.run()
