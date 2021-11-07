from flask import Flask, render_template, url_for, request
#from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '5765763432dsf2423423d'


@app.route("/")
@app.route("/home", methods=["POST"])
def home():
    return render_template('home.html')

@app.route()

@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
