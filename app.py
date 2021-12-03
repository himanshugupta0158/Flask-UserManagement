from flask import Flask , render_template , url_for
from markupsafe import escape

app = Flask(__name__)


posts = [
    {
        'author' : 'Corey Schafer' ,
        'title' : 'Blog Post 1' ,
        'content' : 'First post content' ,
        'date_posted' : 'April 20, 2018'
    },
    {
        'author' : 'Jane Doe' ,
        'title' : 'Blog Post 2' ,
        'content' : 'Second post content' ,
        'date_posted' : 'April 22, 2018'
    }
]


@app.route('/index') #by using this we don't get 404 error
def index():
    return render_template('index.html')

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html' , posts = posts)

@app.route("/<name>")
def Showname(name):
    return f"<h2>Hello,{escape(name)}, this is fetching name from url(HTML Escaping)</h2>"

@app.route("/about")
def about():
    return render_template('about.html' , title = 'About')


if __name__ == '__main__':
    app.run(debug=True)