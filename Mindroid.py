from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm, Chat

app = Flask(__name__)

app.config['SECRET_KEY'] = '5765763432dsf2423423d'

posts = [
    {
    'author' : 'Corey',
    'title' : 'Blog Post 1',
    'content' : 'First post content',
    'date_posted' : 'April 20, 2018'
    },

    {
        'author' : 'Hanah',
        'title' : 'Blog Post 2',
        'content' : 'Set post content',
        'date_posted' : 'March 20, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

@app.route("/chat")
def chat():
    form = ChatMessage()
    return render_template('chat.html', title='Chat', form=form)

if __name__ == '__main__':
    app.run(debug=True)
