import re
from flask import Flask, render_template, url_for
from flask import request
#from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '5765763432dsf2423423d'


@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        message = request.form.get('message')
    print(message)
    return render_template('home.html', text="TOsting")


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
