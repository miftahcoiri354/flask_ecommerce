# **Tutorial Flask Ecommerce-Series**

### **1. Online Shop using flask**
Open `gitbash`
```
> pip install virtualenv
> python -m venv myenv
> source myenv/Scripts/activate
> pip install flask
> pip install flask-SQLAlchemy
> vscode .
```
OR you can also use `pipenv` to create the virtual environment. But, after you create the pipenv, you must set the environment variable for the sqlite3. To do that follow the following instructions, in here you need to specify the sqlite installation directory, which is my directory is `C:/sqlite`.
```
(base) > pipenv install -r requirements.txt
(base) > pipenv shell
(new_env) > set PATH=%PATH%;C:/sqlite
```
To create or open the database you can use the following command
```
> sqlite3 myshop.db
```
But if you have a problem with importing the `sqlite3.dll` and put it into the `C:/sqlite` folder. To download that you can go to this [link](https://www.sqlite.org/2021/sqlite-dll-win64-x64-3340100.zip) and also the tools [link](https://www.sqlite.org/2021/sqlite-tools-win32-x86-3340100.zip), download it and copy into the `myenv/Lib/site-packages/sqlite`.

Then create a folder `shop` and a `run.py`. Inside the `shop` folder, create `__init__.py`, `routes.py`.

Then create a connection to the databases with the following script
```py
#__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myshop.db'
db  = SQLAlchemy(app)

from shop import routes
```
```py
#routes.py
from flask import render_template, session, request, redirect, url_for
from shop import app, db

@app.route('/')
def home():
    return "Home page of your shop"
```
```py
#run.py
from shop import app

if __name__=='__main__':
    app.run(debug=True)
```
Then you cun `run.py`
### **2. Render template with Flask**
Let's go to bootstrap 4 documentation and copy the template as `layout.html` in templates folder
```html
<!-- layout.html -->
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
    <h1>Hello, world!</h1>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
  </body>
</html>
```
- Then copy the `css` url : `https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css`, then save the script into the `static` folder in `css` folder. 
- Also copy the `jQuery` file : `https://code.jquery.com/jquery-3.2.1.slim.min.js`, `https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js`, `https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js` and save the script into the `static` folder in `js` folder 

After that you can go to the `layout.html` script and change the css source folder into.
```html
<!-- layout.html -->
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="{{ url_for('static', filename='css/bootstrap.min.css') }}" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <title>{{title}}</title>
  </head>
  <body>
    {% block content %}
    {% endblock content %}

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="{{ url_for('static', filename='js/jquery-3.2.1.slim.min.js') }}" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="{{ url_for('static', filename='js/popper.min.js') }}" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="{{ url_for('static', filename='js/bootstrap.min.js') }}" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
  </body>
</html>
```
Then move to the `routes.py` and create another routes
```py
#routes.py
@app.route('/register')
def register():
    return render_template('admin/register.html', title="Register User")
```
And organize the directory into the following directory:
```
C:.
│   README.md
│   run.py
│
└───shop
    │   __init__.py
    │
    ├───admin
    │       __init__.py
    │       routes.py
    │
    ├───static
    │   ├───css
    │   │       bootstrap.min.css
    │   │
    │   └───js
    │           bootstrap.min.js
    │           jquery-3.2.1.slim.min.js
    │           popper.min.js
    │
    └───templates
        │   layout.html
        │
        └───admin
               register.html
```
Create a `register.html` page
```html
{% extends "layout.html"%}

{% block content %}

<div class="text-center h1 text-danger">Register</div>

{% endblock content %}
```

### **3. User regristration online shop with Flask WTForm**
Ih here you need to install `flsk-wtf`
```
> pip install flask-wtf
```
Then go to `flask-wtf` documentations and copy the template into python script as `forms.py`.
```py
from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    name = StringField('Name', [validators.Length(min=4, max=25)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35), validators.Email()])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
```
Then back to the `routes.py` and create the routes with the sources code from `flask-wtf` documentations. 
```py
from flask import flash
from .forms import registrationForm

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        #user = User(form.username.data, form.email.data,
        #            form.password.data)
        #db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('admin/register.html', form=form, title="Registration page")
```
And back into the `flask-wtf` documentation and copy the html script as `_formhelper.html`
```html
{% macro render_field(field) %}
  <dt>{{ field.label }}
  <dd>{{ field(**kwargs)|safe }}
  {% if field.errors %}
    <ul class=errors>
    {% for error in field.errors %}
      <li>{{ error }}</li>
    {% endfor %}
    </ul>
  {% endif %}
  </dd>
{% endmacro %}
```
And the last one copy the html script into the `registration.html` inside the container
```html
<div class="container">
    {% from "_formhelpers.html" import render_field %}
    <form method="post" enctype="multipart/form-date">
        <dl>
            {{ render_field(form.name, class="form-control") }}
            {{ render_field(form.username, class="form-control") }}
            {{ render_field(form.email, class="form-control") }}
            {{ render_field(form.password, class="form-control") }}
            {{ render_field(form.confirm, class="form-control") }}
            <input type="file" name="photo">
        </dl>
    <p><input type=submit value=Register class="btn btn-info">
</form>
```
Now you can run your app and your folder will be  
```
C:.
│   README.md
│   run.py
│
└───shop
    │   __init__.py
    │
    ├───admin
    │   │   forms.py
    │   │   routes.py
    │   │   
    │   └───__init__.py
    │
    ├───static
    │   ├───css
    │   │       bootstrap.min.css
    │   │
    │   └───js
    │           bootstrap.min.js
    │           jquery-3.2.1.slim.min.js
    │           popper.min.js
    │
    └───templates
        │   layout.html
        │   _formhelpers.html
        │
        └───admin
                register.html
```
### **4. How to registration user system database with flask**
In this session, you need to install other dependencies
```
> pip install flask-bcrypt
```
Then go to the "shop/__init__.py" and add the following script
```py
#__init__.py
from flask_bcrypt import Bcrypt

app.config['SECRET_KEY'] = 'mysecretkeydonotstealit'
bcrypt = Bcrypt(app)
``` 
Then go to `SQLAlchemy` documentation and go to `Quickstart` and copy the following scripts into a new file `admin/models.py`
```py
#models.py
from shop import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(180), unique=False, nullable=False)
    profile = db.Column(db.String(180), unique=False, nullable=False, default='profile.jpg')

    def __repr__(self):
        return '<User %r>' % self.username

db.create_all()
```
```py
#routes.py
from shop import bcrypt
from .models import User
import os

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data, username=form.username.data, email=form.email.data, password=hash_password)
        db.session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('home'))
    return render_template('admin/register.html', form=form, title="Registration page")
```
You can add the session to show the current user which logged into the account
```py
#routes.py
@app.route('/')
def home():
    return render_template('admin/index.html', title='Admin Page')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data, username=form.username.data, email=form.email.data, password=hash_password)
        db.session.add(user)
        flash(f'Welcome {form.name.data} Thanks for registering', 'success')
        
        return redirect(url_for('home'))
    return render_template('admin/register.html', form=form, title="Registration page")
```
To show that you can create the `index.html` that you can copy from flask flash documentation
```html
<!-- index.html -->
{% extends "layout.html"%}
{% block content %}

{% with messages = get_flashed_messages(with_categories=true) %}
  {% if messages %}
    <ul class=flashes>
    {% for category, message in messages %}
      <li class="alert alert-{{ category }}">{{ message }}</li>
    {% endfor %}
    </ul>
  {% endif %}
{% endwith %}

{% endblock content %}
```
To commit the inputed data to database, you can add the following script db.`session.commit()` into your `routes.py`
```py
#routes.py
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data, username=form.username.data, email=form.email.data, password=hash_password)
        db.session.add(user)
        db.session.commit()
        
        flash(f'Welcome {form.name.data} Thanks for registering', 'success')
        return redirect(url_for('home'))
    return render_template('admin/register.html', form=form, title="Registration page")
```
```
C:.
│   README.md
│   run.py
│
└───shop
    │   myshop.db
    │   myshop2.db
    │   __init__.py
    │
    ├───admin
    │       forms.py
    │       models.py
    │       routes.py
    │       __init__.py
    │
    ├───static
    │   ├───css
    │   │       bootstrap.min.css
    │   │
    │   └───js
    │           bootstrap.min.js
    │           jquery-3.2.1.slim.min.js
    │           popper.min.js
    │
    └───templates
        │   layout.html
        │   _formhelpers.html
        │
        └───admin
                index.html
                register.html  
```
### **5. How to make user login system online shop with flask**
Let's go to admin and find the `forms.py` 
```py
#forms.py
class loginForm(Form):
    email = StringField('Email Address', [validators.Length(min=6, max=35), validators.Email()])
    password = PasswordField('New Password', [validators.DataRequired()])
```
Create the session if the user have not login yet, so you can create new page called `/login`
```py
#routes.py
from .forms import loginForm

@app.route('/admin')
def admin():
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login')
    return render_template('admin/index.html', title='Admin Page')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request, form)
    return render_template('admin/login.html', form=form, title='Login Page')
```
Then go to `template` and create new html file `login.html`
```html
<!-- login.html -->
{% extends "layout.html"%}
{% block content %}

<div class="container">
    {% from "_formhelpers.html" import render_field %}
    <div class="row">
        <div class="col-md-4"></div>
        <div class="col-md-4">
        <div class="text-center h1 text-white bg-primary p-2">Login</div>
        <form method="post" enctype="multipart/form-date">
          <dl>
            {{ render_field(form.email, class="form-control") }}
            {{ render_field(form.password, class="form-control") }}
            <input type="file" name="photo">
          </dl>
      <p><input type=submit value="Login" class="btn btn-info">
    </form>
  </div>
  <div class="col-md-4"></div>
  </div>
</div>
{% endblock content %}
```
Back into `routes.py` and create the function to detect the current session if the user has been logged in. 
```py
#routes.py
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = loginForm(request.form)
    if request.method == 'POST' and form.validate():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            flash(f'Welcome {form.email.data} You are logged in now', 'success')
            return redirect(request.args.get('next') or url_for('admin'))
        else:
            flash('Wrong Password, Please Try Again!', 'danger')
    return render_template('admin/login.html', form=form, title='Login Page')
```
Now, create new `-messages.html` to create script helper for message notifications.
```html
<!-- _messages.html -->
{% with messages = get_flashed_messages(with_categories=true) %}
  {% if messages %}
    <ul class=flashes>
    {% for category, message in messages %}
      <li class="alert alert-{{ category }}">{{ message }}</li>
    {% endfor %}
    </ul>
  {% endif %}
{% endwith %}
```
```html
<!-- index.html -->
{% extends "layout.html"%}
{% block content %}

{% include '_messages.html' %}

{% endblock content %} 
```
Then go to the login and put the message with the `-messages.html` script
```html
        <div class="text-center h1 text-white bg-primary p-2">Login</div>
        {% include '_messages.html'%}
        <form method="post" enctype="multipart/form-date">
```

### **6. SQLAlchemy how to add brand & category**
Now, create new folder `products` inside the `shop`, and create new file `__init__.py`, `models.py` and `routes.py`
```py
#models.py
from shop import db

class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)

db.create_all()
```
```py
#routes.py
from flask import redirect, render_template, url_for, flash, request
from shop import db, app

@app.route('/addbrand', method=['GET', 'POST'])
def addbrand():
    return render_template('products/addbrand.html')
```
Now create new `addbrand.html` page and type the following scripts.
```html
{% extends "layout.html"%}
{% block content %}

<div class="container">
    <div class="row">
        <div class="col-md-3"></div>
        <div class="col-md-6">
            {% if brands %}
            <h1 class="text-center mt-5">Add a Brand</h1>
            {% include "_messages.html" %}
            <form action="" method="POST">
                <input type="text" name="brand" class="form-control">
                <input type="submit" value="Add brand" class="btn btn-info mt-2">
            </form>
            {% else %}
            <h1 class="text-center mt-5">Add a Category</h1>
            {% include "_messages.html" %}
            <form action="" method="POST">
                <input type="text" name="category" class="form-control">
                <input type="submit" value="Add category" class="btn btn-info mt-2">
            </form>
            {% endif %}
        </div>
    </div>
</div>

{% endblock content %} 
```
Now you can back to the `__init__.py` to call the `routes` from products folder.
```py
#__init__.py
from shop.products import routes
```
Now back to `routes.py` and define the function to get the brand and category
```py
#routes.py
from .models import Brand, Category

@app.route('/addbrand',methods=['GET','POST'])
def addbrand():
    if request.method =="POST":
        getbrand = request.form.get('brand')
        brand = Brand(name=getbrand)
        db.session.add(brand)
        flash(f'The brand {getbrand} was added to your database','success')
        db.session.commit()
        return redirect(url_for('addbrand'))
    return render_template('products/addbrand.html', title='Add brand',brands='brands')

@app.route('/addcat',methods=['GET','POST'])
def addcat():
    if request.method =="POST":
        getcat = request.form.get('category')
        category = Category(name=getcat)
        db.session.add(category)
        flash(f'The brand {getcat} was added to your database','success')
        db.session.commit()
        return redirect(url_for('addcat'))
    return render_template('products/addbrand.html', title='Add category')
```
```
C:.
│   README.md
│   run.py
│
└───shop
    │   myshop.db
    │   myshop2.db
    │   __init__.py
    │
    ├───admin
    │       forms.py
    │       models.py
    │       routes.py
    │       __init__.py
    │
    ├───products
    │       models.py
    │       routes.py
    │       __init__.py
    │
    ├───static
    │   ├───css
    │   │       bootstrap.min.css
    │   │
    │   └───js
    │           bootstrap.min.js
    │           jquery-3.2.1.slim.min.js
    │           popper.min.js
    │
    └───templates
        │   layout.html
        │   _formhelpers.html
        │   _messages.html
        │
        ├───admin
        │       index.html
        │       login.html
        │       register.html
        │
        └───products
                addbrand.html
```
### **7. How to addproduct form with Flask WTForms**
Install another dependencies
```
> pipenv install flask-wtf
> pipenv install wtforms
```
Create another new python script as `forms.py`
```py
#forms.py
from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import Form, IntegerField, StringField, BooleanField, TextAreaField, validators

class Addproducts(Form):
  name = StringField("Name", [validators.DataRequired()])
  price = IntegerField('Price', [validators.DataRequired()])
  discount = IntegerField('Discount', default=0)
  stock = IntegerField('Stock', [validators.DataRequired()])
  colors = TextAreaField('Color', [validators.DataRequired()])
  description = TextAreaField('Description', [validators.DataRequired()])

  image_1 = FileField('image 1', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
  image_2 = FileField('image 2', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
  image_3 = FileField('image 3', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
```
```py
from .forms import Addproducts
import secrets

@app.route('/')
def home():
    return " "

@app.route('/addproduct', methods=['POST', 'GET'])
def addproduct():
    form = Addproducts(request.form)
    return render_template('products/addproduct.html', title="Add Product page", form=form)
```
Now create the templates for forms input.
```html
<!-- addproduct.html -->
{% extends "layout.html"%}
{% block content %}
{% include "_messages.html" %}

<div class="container">
        <div class="col-md-2"></div>
        <div class="col-md-8">
            <h1 class="text-center bg-info p-2">Add a Product</h1>
            {% from "_formhelpers.html" import render_field %}
            <form action="" method="POST" enctype="multipart/form-data">
                {{ render_field(form.name, class="form-control", placeholder='Add product name') }}
                {{ render_field(form.price, class="form-control", placeholder='Add product price') }}
                {{ render_field(form.discount, class="form-control", placeholder='Add product discount') }}
                {{ render_field(form.stock, class="form-control", placeholder='Add product stock') }}
                {{ render_field(form.colors, class="form-control", placeholder='Add product color') }}
                {{ render_field(form.description, class="form-control", placeholder='Add product detail', rows="10") }}
            
                <div class="container">
                    <div class="row">
                        <div class="col-md-4">{{ form.image_1(class="form-control") }}</div>
                        <div class="col-md-4">{{ form.image_2(class="form-control") }}</div>
                        <div class="col-md-4">{{ form.image_3(class="form-control") }}</div>
                    </div>
                </div>
            <button type="submit" class="btn btn-outline-info mt-4"> Add Product </button>
            </form>
        </div>

    <div class="col-md-2"></div>
</div>

{% endblock content %} 
```
### **8. How to deploy brands and categories for admin using flask**
In here will will show the product brands and categories, now go to `routes.py`
```py
#routes.py
@app.route('/addproduct', methods=['POST', 'GET'])
def addproduct():
    brands = Brand.query.all()
    categories = Category.query.all()
    form = Addproducts(request.form)
    return render_template('products/addproduct.html', title="Add Product page", form=form, brands=brands, categories=categories)
```
And go to the `addproduct.html`
```html
                {{ render_field(form.stock, class="form-control", placeholder='Add product stock') }}
                
                <label for="brand">Add a brand</label>
                <select name="brand" id="brand" class="form-control" required> 
                    <option value=""> Select a Brand</option>
                    {% for brand in brands %}
                    <option value="brand.id">{{brand.name}}</option>
                    {% endfor %}
                </select>
                <label for="category">Add a Category</label>
                <select name="category" id="category" class="form-control" required>
                    <option value=""> Add a category</option>
                    {% for category in categories %}
                    <option value="{{category.id}}">{{category.name}}</option>
                    {% endfor %}
                </select>

                {{ render_field(form.colors, class="form-control", placeholder='Add product color') }}
```

### **9. Create product table to database SQLAlchemy flask**
Go to the `models.py` and go to SQLAlchemy documentation and copy the script with the datetime.
```py
from datetime import datetime

class Addproduct(db.Model):
    __seachbale__ = ['name','desc']
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Numeric(10,2), nullable=False)
    discount = db.Column(db.Integer, default=0)
    stock = db.Column(db.Integer, nullable=False)
    colors = db.Column(db.Text, nullable=False)
    desc = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),nullable=False)
    category = db.relationship('Category',backref=db.backref('categories', lazy=True))

    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'),nullable=False)
    brand = db.relationship('Brand',backref=db.backref('brands', lazy=True))

    image_1 = db.Column(db.String(150), nullable=False, default='image1.jpg')
    image_2 = db.Column(db.String(150), nullable=False, default='image2.jpg')
    image_3 = db.Column(db.String(150), nullable=False, default='image3.jpg')

    def __repr__(self):
        return '<Post %r>' % self.name
```
Then you can run the script and take a look into the table info using the following command
```
> sqlite3 myshop2.db
sqlite > .table
sqlite > pragma table_info(addproduct); 
```

### **10. Upload images files using flask**
In here we will try to create a program to grab the image file, but to do that we need to install `flask-uploads` dependencies
```
> pipenv install flask-uploads
```
Now go to the `__init__.py` and then type the following script
```py
#__init__.py
from flask_uploads import IMAGES.UploadSet, configure_uploads, patch_request_class
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/images')

photos =UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)
```
```py
#routws.py
from shop import photos

@app.route('/addproduct', methods=['POST', 'GET'])
def addproduct():
    brands = Brand.query.all()
    category = Category.query.all()
    form = Addproducts(request.form)
    if request.method == "POST":
        image_1 = photos.save(request.files.get('image_1') ,  name=secrets.token_hex(10) + ".")
        image_2 = photos.save(request.files.get('image_2') ,  name=secrets.token_hex(10) + ".")
        image_3 = photos.save(request.files.get('image_3') ,  name=secrets.token_hex(10) + ".")
    return render_template('products/addproduct.html', form=form, title='Add product', brands=brands, categories=categories)
```

### **11. Online shop with flask add product in database**
In here, we will add the product data into database
```py
#routes.py
@app.route('/addproduct', methods=['POST', 'GET'])
def addproduct():
    brands = Brand.query.all()
    categories = Category.query.all()
    form = Addproducts(request.form)
    if request.method == "POST" and 'image_1' in request.files:
        name = form.name.data
        price = form.price.data
        discount = form.discount.data
        stock = form.stock.data
        colors = form.colors.data
        desc = form.description.data
        brand = request.form.get('brand')
        category = request.form.get('category')
        image_1 = photos.save(request.files.get('image_1') ,  name=secrets.token_hex(10) + ".")
        image_2 = photos.save(request.files.get('image_2') ,  name=secrets.token_hex(10) + ".")
        image_3 = photos.save(request.files.get('image_3') ,  name=secrets.token_hex(10) + ".")
        addproduct = Addproduct(name=name,price=price,discount=discount,stock=stock,colors=colors,desc=desc,category_id=category,brand_id=brand,image_1=image_1,image_2=image_2,image_3=image_3)
        db.session.add(addproduct)
        flash(f'The product {name} was added in database','success')
        db.session.commit()
        return redirect(url_for('admin'))
    return render_template('products/addproduct.html', title="Add Product page", form=form, brands=brands, categories=categories)
```

### **12. Online shop display products in admin page**
First, you need go to `admin/routes.py` and type the following script
```py
#admin/routes.py
from shop.products.models import Addproduct, Category, Brand

@app.route('/admin')
def admin():
    print(session)
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    products = Addproduct.query.all()
    return render_template('admin/index.html', title='Admin Page', products=products)

@app.route('/brands')
def brands():
    brands = Brand.query.order_by(Brand.id.desc()).all()
    return render_template('admin/brand.html', title='brands',brands=brands)


@app.route('/categories')
def categories():
    categories = Category.query.order_by(Category.id.desc()).all()
    return render_template('admin/brand.html', title='categories',categories=categories)
```
And go to the `products/routes.py`
```py
#products/routes.py
import os

@app.route('/updatecat/<int:id>',methods=['GET','POST'])
def updatecat(id):
    if 'email' not in session:
        flash('Login first please','danger')
        return redirect(url_for('login'))
    updatecat = Category.query.get_or_404(id)
    category = request.form.get('category')  
    if request.method =="POST":
        updatecat.name = category
        flash(f'The category {updatecat.name} was changed to {category}','success')
        db.session.commit()
        return redirect(url_for('categories'))
    category = updatecat.name
    return render_template('products/addbrand.html', title='Update cat',updatecat=updatecat)

@app.route('/updatebrand/<int:id>',methods=['GET','POST'])
def updatebrand(id):
    if 'email' not in session:
        flash('Login first please','danger')
        return redirect(url_for('login'))
    updatebrand = Brand.query.get_or_404(id)
    brand = request.form.get('brand')
    if request.method =="POST":
        updatebrand.name = brand
        flash(f'The brand {updatebrand.name} was changed to {brand}','success')
        db.session.commit()
        return redirect(url_for('brands'))
    brand = updatebrand.name
    return render_template('products/addbrand.html', title='Udate brand',brands='brands',updatebrand=updatebrand)

@app.route('/updateproduct/<int:id>', methods=['GET','POST'])
def updateproduct(id):
    form = Addproducts(request.form)
    product = Addproduct.query.get_or_404(id)
    brands = Brand.query.all()
    categories = Category.query.all()
    brand = request.form.get('brand')
    category = request.form.get('category')
    if request.method =="POST":
        product.name = form.name.data 
        product.price = form.price.data
        product.discount = form.discount.data
        product.stock = form.stock.data 
        product.colors = form.colors.data
        product.desc = form.discription.data
        product.category_id = category
        product.brand_id = brand
        if request.files.get('image_1'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_1))
                product.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
            except:
                product.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
        if request.files.get('image_2'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_2))
                product.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
            except:
                product.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
        if request.files.get('image_3'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_3))
                product.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")
            except:
                product.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")

        flash('The product was updated','success')
        db.session.commit()
        return redirect(url_for('admin'))
    form.name.data = product.name
    form.price.data = product.price
    form.discount.data = product.discount
    form.stock.data = product.stock
    form.colors.data = product.colors
    form.discription.data = product.desc
    brand = product.brand.name
    category = product.category.name
    return render_template('products/addproduct.html', form=form, title='Update Product',getproduct=product, brands=brands,categories=categories)

@app.route('/deletebrand/<int:id>', methods=['GET','POST'])
def deletebrand(id):
    brand = Brand.query.get_or_404(id)
    if request.method=="POST":
        db.session.delete(brand)
        flash(f"The brand {brand.name} was deleted from your database","success")
        db.session.commit()
        return redirect(url_for('admin'))
    flash(f"The brand {brand.name} can't be  deleted from your database","warning")
    return redirect(url_for('admin'))

@app.route('/deletecat/<int:id>', methods=['GET','POST'])
def deletecat(id):
    category = Category.query.get_or_404(id)
    if request.method=="POST":
        db.session.delete(category)
        flash(f"The brand {category.name} was deleted from your database","success")
        db.session.commit()
        return redirect(url_for('admin'))
    flash(f"The brand {category.name} can't be  deleted from your database","warning")
    return redirect(url_for('admin'))


@app.route('/deleteproduct/<int:id>', methods=['POST'])
def deleteproduct(id):
    product = Addproduct.query.get_or_404(id)
    if request.method =="POST":
        try:
            os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_1))
            os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_2))
            os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_3))
        except Exception as e:
            print(e)
        db.session.delete(product)
        db.session.commit()
        flash(f'The product {product.name} was delete from your record','success')
        return redirect(url_for('adim'))
    flash(f'Can not delete the product','success')
    return redirect(url_for('admin'))
```
And go to the `admin/index.html` and crete the template
```html
{% extends "layout.html"%}
{% block content %}

<div class="container">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="{{url_for('admin')}}">Navbar</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavDropdown">
          <ul class="navbar-nav">
            <li class="nav-item active">
              <a class="nav-link" href="{{url_for('admin')}}">product <span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{{url_for('brands')}}">brand</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{{url_for('categories')}}">catgory</a>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                Add products
              </a>
              <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                <a class="dropdown-item" href="{{url_for('addproduct')}}">Add product</a>
                <a class="dropdown-item" href="{{url_for('addbrand')}}">add brand</a>
                <a class="dropdown-item" href="{{url_for('addcat')}}">add category</a>
              </div>
            </li>
          </ul>
        </div>
      </nav>
</div>

<!--==========END NAVBAR ==============-->

<div class="container">
    {% include '_messages.html' %}
    <table class="table tbale-sm">
        <thead>
            <th>Sr</th>
            <th>Image</th>
            <th>Name</th>
            <th>Price</th>
            <th>Discount</th>
            <th>Brand</th>
            <th>Edit</th>
            <th>Delete</th>
        </thead>
        <tbody>
          {% for product in products %}
          <tr>
            <td>{{loop.index}}</td>
            <td> <img src="{{url_for('static',filename='images/' + product.image_1)}}" alt="{{product.name}}" width="50" height="20"></td>
            <td>{{ product.name }}</td>
            <td>{{ product.price }}</td>
            <td>{{ product.discount }}</td>
            <td>{{ product.brand.name}}</td>
            <td> <a href="{{url_for('updateproduct', id=product.id)}}" class="btn btn-sm btn-info">Edit </a> </td>
            <td><button type="button" class="btn btn-danger btn-sm" data-toggle="modal" data-target="#exampleModal-{{product.id}}">
              Delete
            </button></td>
          </tr>

 <!--============= MODEL ===================-->
        <div class="modal fade" id="exampleModal-{{product.id}}" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog" role="document">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">{{product.name }}</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                  <span aria-hidden="true">&times;</span>
                </button>
              </div>
              <div class="modal-body">
                <p class="text-danger">Are you Sure that you want to delete this Category ({{ product.name }})</p>
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Cancel</button>
                <form action="{{url_for('deletecat',id=product.id)}}" method="post">
                  <button type="submit" class="btn btn-danger">Delete</button>
                </form>
                
              </div>
            </div>
          </div>
        </div>
<!--==============MODEL ===================-->

          {% endfor %}
        </tbody>
    </table>
</div>

{% endblock content %} 
```

### **13. Display brands and Categories**
```py
#admin/routes.py
from shop.products.models import Addproduct, Category,Brand

@app.route('/brands')
def brands():
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    brands = Brand.query.order_by(Brand.id.desc()).all()
    return render_template('admin/brand.html', title='Brand Page',brands=brands)

@app.route('/categories')
def categories():
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    categories = Category.query.order_by(Category.id.desc()).all()
    return render_template('admin/brand.html', title='categories',categories=categories)
```
Then go to template and create the `admin/brand.html` 
```html
<!-- admin/brand.html -->
{% extends 'layout.html' %}
{% block content %}
<div class="container">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="{{url_for('admin')}}">Navbar</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavDropdown">
          <ul class="navbar-nav">
            <li class="nav-item active">
              <a class="nav-link" href="{{url_for('admin')}}">product <span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{{url_for('brands')}}">brand</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{{url_for('categories')}}">catgory</a>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                Add products
              </a>
              <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                <a class="dropdown-item" href="{{url_for('addproduct')}}">Add product</a>
                <a class="dropdown-item" href="{{url_for('addbrand')}}">add brand</a>
                <a class="dropdown-item" href="{{url_for('addcat')}}">add category</a>
              </div>
            </li>
          </ul>
        </div>
      </nav>
</div>

<!--==========END NAVBAR ==============-->

<div class="container">
    {% include '_messages.html' %}
    <table class="table tbale-sm">
        <thead>
            <th>Sr</th>
            <th>Name</th>
            <th>Edit</th>
            <th>Delete</th>
        </thead>
        <tbody>
         {% if brands %}
          {% for brand in brands %}
          <tr>
            <td>{{loop.index}}</td>
            <td>{{ brand.name }}</td>
            <td><a href="{{url_for('updatebrand', id=brand.id)}}" class="btn btn-sm btn-info">Edit</a></td>
            <td><button type="button" class="btn btn-danger btn-sm" data-toggle="modal" data-target="#exampleModal-{{brand.id}}">
              Delete
            </button></td>
          </tr>


<!--============= MODEL ===================-->

<div class="modal fade" id="exampleModal-{{brand.id}}" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">{{ brand.name }}</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <p class="text-danger">Are you Sure that you want to delete this brand ({{ brand.name }}) </p>
       </div>
       <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Cancel</button>
        <form action="{{url_for('deletebrand',id=brand.id)}}" method="post">
          <button type="submit" class="btn btn-danger">Delete</button>
        </form>
        
      </div>
    </div>
  </div>
</div>
<!--==============MODEL ===================-->

          {% endfor %}
          {% else %}
          {% for category in categories %}
          <tr>
            <td>{{loop.index}}</td>
            <td>{{ category.name }}</td>
            <td> <a href="{{url_for('updatecat', id=category.id)}}" class="btn btn-sm btn-info">Edit</a></td>
            <td><button type="button" class="btn btn-danger btn-sm" data-toggle="modal" data-target="#exampleModal-{{category.id}}">
              Delete
            </button></td>
          </tr>


<!--============= MODEL ===================-->
      <div class="modal fade" id="exampleModal-{{category.id}}" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalLabel">{{category.name }}</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              <p class="text-danger">Are you Sure that you want to delete this Category ({{ category.name }}) </p>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Cancel</button>
              <form action="{{url_for('deletecat',id=category.id)}}" method="post">
                <button type="submit" class="btn btn-danger">Delete</button>
              </form>
              
            </div>
          </div>
        </div>
      </div>
<!--==============MODEL ===================-->

          {% endfor %}
          {% endif %}
        </tbody>
    </table>
</div>
{% endblock content %}
```
### **14. Update brands and categories**
```py
#products/routes.py
@app.route('/updatebrand/<int:id>',methods=['GET','POST'])
def updatebrand(id):
    if 'email' not in session:
        flash('Login first please','danger')
        return redirect(url_for('login'))
    updatebrand = Brand.query.get_or_404(id)
    brand = request.form.get('brand')
    if request.method =="POST":
        updatebrand.name = brand
        flash(f'The brand {updatebrand.name} was changed to {brand}','success')
        db.session.commit()
        return redirect(url_for('brands'))
    brand = updatebrand.name
    return render_template('products/addbrand.html', title='Udate brand',brands='brands',updatebrand=updatebrand)


@app.route('/updatecat/<int:id>',methods=['GET','POST'])
def updatecat(id):
    if 'email' not in session:
        flash('Login first please','danger')
        return redirect(url_for('login'))
    updatecat = Category.query.get_or_404(id)
    category = request.form.get('category')  
    if request.method =="POST":
        updatecat.name = category
        flash(f'The category {updatecat.name} was changed to {category}','success')
        db.session.commit()
        return redirect(url_for('categories'))
    category = updatecat.name
    return render_template('products/addbrand.html', title='Update cat',updatecat=updatecat)
```
Create new file `updatebrand.html`
```html
```
### **15. Update items using flask online shop**
```py
#products/routes.py
@app.route('/updateproduct/<int:id>', methods=['GET','POST'])
def updateproduct(id):
    form = Addproducts(request.form)
    product = Addproduct.query.get_or_404(id)
    brands = Brand.query.all()
    categories = Category.query.all()
    brand = request.form.get('brand')
    category = request.form.get('category')
    if request.method =="POST":
        product.name = form.name.data 
        product.price = form.price.data
        product.discount = form.discount.data
        product.stock = form.stock.data 
        product.colors = form.colors.data
        product.desc = form.description.data
        product.category_id = category
        product.brand_id = brand
        if request.files.get('image_1'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_1))
                product.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
            except:
                product.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
        if request.files.get('image_2'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_2))
                product.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
            except:
                product.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
        if request.files.get('image_3'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_3))
                product.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")
            except:
                product.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")

        flash('The product was updated','success')
        db.session.commit()
        return redirect(url_for('admin'))
    form.name.data = product.name
    form.price.data = product.price
    form.discount.data = product.discount
    form.stock.data = product.stock
    form.colors.data = product.colors
    form.description.data = product.desc
    brand = product.brand.name
    category = product.category.name
    return render_template('products/addproduct.html', form=form, title='Update Product',getproduct=product, brands=brands,categories=categories)
```
Create new file `updateproducts.html`
```html
```
### **16. Delete files and update images**
```py
#forms.py
class Addproducts(Form):
  name = StringField("Name", [validators.DataRequired()])
  price = DecimalField('Price', [validators.DataRequired()])
  discount = IntegerField('Discount', default=0)
  stock = IntegerField('Stock', [validators.DataRequired()])
  colors = TextAreaField('Color', [validators.DataRequired()])
  description = TextAreaField('Description', [validators.DataRequired()])

  image_1 = FileField('image 1', validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
  image_2 = FileField('image 2', validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
  image_3 = FileField('image 3', validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
```
```html
<!-- addproduct.html-->
                        <div class="col-md-4">{{ render_field(form.image_1, class="form-control", required) }}</div>
                        <div class="col-md-4">{{ render_field(form.image_2, class="form-control", required) }}</div>
                        <div class="col-md-4">{{ render_field(form.image_3, class="form-control", required) }}</div>
```
```html
<!-- updateproduct.html-->
                        <div class="col-md-4">{{ render_field(form.image_1, class="form-control") }}</div>
                        <div class="col-md-4">{{ render_field(form.image_2, class="form-control") }}</div>
                        <div class="col-md-4">{{ render_field(form.image_3, class="form-control") }}</div>
```
```py
from flask import current_app

@app.route('/updateproduct/<int:id>', methods=['GET','POST'])
def updateproduct(id):
    form = Addproducts(request.form)
    product = Addproduct.query.get_or_404(id)
    brands = Brand.query.all()
    categories = Category.query.all()
    brand = request.form.get('brand')
    category = request.form.get('category')
    if request.method =="POST":
        product.name = form.name.data 
        product.price = form.price.data
        product.discount = form.discount.data
        product.stock = form.stock.data 
        product.colors = form.colors.data
        product.desc = form.description.data
        product.category_id = category
        product.brand_id = brand
        if request.files.get('image_1'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_1))
                product.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
            except:
                product.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
        if request.files.get('image_2'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_2))
                product.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
            except:
                product.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
        if request.files.get('image_3'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_3))
                product.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")
            except:
                product.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")

        flash('The product was updated','success')
        db.session.commit()
        return redirect(url_for('admin'))
    form.name.data = product.name
    form.price.data = product.price
    form.discount.data = product.discount
    form.stock.data = product.stock
    form.colors.data = product.colors
    form.description.data = product.desc
    brand = product.brand.name
    category = product.category.name
    return render_template('products/updateproduct.html', form=form, title='Update Product',getproduct=product, brands=brands,categories=categories)
```
### **17. Delete brands and categories flask**
```py
#product/routes.py
@app.route('/deletebrand/<int:id>', methods=['GET','POST'])
def deletebrand(id):
    brand = Brand.query.get_or_404(id)
    set_query = set([idx for br_id in Addproduct.query.with_entities(Addproduct.brand_id).distinct().all() for idx in br_id]) 
    if request.method=="POST":
        if brand.id in set_query:
            flash(f"The brand {brand.name} can't be  deleted from your database because some products use this Brand","warning")
            return redirect(url_for('admin'))
        else:
            flash(f"The brand {brand.name} was deleted from your database","success")
            db.session.delete(brand)
            db.session.commit()
            return redirect(url_for('admin'))
    flash(f"The brand {brand.name} can't be  deleted from your database","warning")
    return redirect(url_for('admin'))

@app.route('/deletecat/<int:id>', methods=['GET','POST'])
def deletecat(id):
    category = Category.query.get_or_404(id) 
    set_query = set([idx for cat_id in Addproduct.query.with_entities(Addproduct.category_id).distinct().all() for idx in cat_id]) 
    if request.method=="POST":
        if category.id in set_query:
            flash(f"The Category {category.name} can't be  deleted from your database because some products use this Category","warning")
            return redirect(url_for('admin'))
        else:
            flash(f"The Category {category.name} was deleted from your database","success")
            db.session.delete(category)
            db.session.commit()
            return redirect(url_for('admin'))
    flash(f"The Category {category.name} can't be  deleted from your database","warning")
    return redirect(url_for('admin'))
```
```html
<!-- brand.html-->
            <td><button type="button" class="btn btn-danger btn-sm" data-toggle="modal" data-target="#exampleModal-{{brand.id}}">
              Delete
            </button></td>
          </tr>


<!--============= MODEL ===================-->

<div class="modal fade" id="exampleModal-{{brand.id}}" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">{{ brand.name }}</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <p class="text-danger">Are you Sure that you want to delete this brand ({{ brand.name }}) </p>
       </div>
       <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Cancel</button>
        <form action="{{url_for('deletebrand',id=brand.id)}}" method="post">
          <button type="submit" class="btn btn-danger">Delete</button>
        </form>
        
      </div>
    </div>
  </div>
</div>
<!--==============MODEL ===================-->
```
### **18. Delete items online shop flask**
```html
<!-- index.html-->
          {% for product in products %}
          <tr>
            <td>{{loop.index}}</td>
            <td> <img src="{{url_for('static',filename='images/' + product.image_1)}}" alt="{{product.name}}" width="50" height="20"></td>
            <td>{{ product.name }}</td>
            <td>{{ product.price }}</td>
            <td>{{ product.discount }}</td>
            <td>{{ product.brand.name}}</td>
            <td>{{ product.category.name}}</td>
            <td> <a href="{{url_for('updateproduct', id=product.id)}}" class="btn btn-sm btn-info">Edit </a> </td>
            <td><button type="button" class="btn btn-danger btn-sm" data-toggle="modal" data-target="#exampleModal-{{product.id}}">
              Delete
            </button></td>
          </tr>

 <!--============= MODEL ===================-->
        <div class="modal fade" id="exampleModal-{{product.id}}" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog" role="document">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">{{product.name }}</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                  <span aria-hidden="true">&times;</span>
                </button>
              </div>
              <div class="modal-body">
                <p class="text-danger">Are you Sure that you want to delete this Category ({{ product.name }})</p>
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Cancel</button>
                <form action="{{url_for('deleteproduct',id=product.id)}}" method="post">
                  <button type="submit" class="btn btn-danger">Delete</button>
                </form>
                
              </div>
            </div>
          </div>
        </div>
<!--==============MODEL ===================-->

          {% endfor %}
```
```py
#routes.py
@app.route('/deleteproduct/<int:id>', methods=['POST'])
def deleteproduct(id):
    product = Addproduct.query.get_or_404(id)
    if request.method =="POST":
        try:
            os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_1))
            os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_2))
            os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_3))
        except Exception as e:
            print(e)
        db.session.delete(product)
        db.session.commit()
        flash(f'The product {product.name} was delete from your record','success')
        return redirect(url_for('adim'))
    flash(f'Can not delete the product','success')
    return redirect(url_for('admin'))
```

### **19. Display items online shop**

### **20. Display brands online shop and join tables**

### **21. Display categories with flask**

### **22. Online shop pagination**


### **23. Display single product with flask**

### **24. Add to cart online shop**

### **25. How to display cart items with flask**


### **26. How to update shopping cart items with flask**

### **27. How to remove cart items with flask**

### **28. How to clear cart items with Flask**

### **29. Create customer registration form with python**

### **30. Create customer regirstation template form**

### **31. Create customer registration model**

### **32. Form validation & user login**

### **33. How to logout user in flask**

### **34. SQLAlchemy Migrations using Flask-Migrate**

### **35. Create customer order table**

### **36. Insert customer order into table as json**

### **37. Display customer orders**

### **38. How to generate Dynamic PDF using Flask**

### **39. How to integrate stripe payment**