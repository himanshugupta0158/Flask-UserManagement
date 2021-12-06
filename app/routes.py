from flask import render_template , url_for , flash , redirect
from app.models import User , Post    
from markupsafe import escape
from app.forms import RegistrationForm , LoginForm
from app import app


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

@app.route("/register" , methods = ['GET' , 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!' , 'success')
        return redirect(url_for('home'))
    return render_template('register.html' , title = 'Register' , form = form)

@app.route("/login" , methods=['GET' , 'POST'] )
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password' :
            flash('You have been logged in !' , 'success')
            return redirect(url_for('home'))
        else:
            flash('Loggin Unsuccessful. Please Check username and password' , 'danger')
    return render_template('login.html' , title = 'Register' , form = form)
