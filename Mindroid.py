from flask import Flask, render_template
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
