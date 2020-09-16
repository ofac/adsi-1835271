import os
from flask import Flask, render_template, redirect, request, flash, session
from flask_bootstrap import Bootstrap
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
import pymongo
import time
app = Flask(__name__)
app.secret_key = "adsi secret key"
app.config['UPLOAD_FOLDER'] = os.path.dirname(os.path.abspath(__file__))
app.templates_auto_reload = True
bootstrap = Bootstrap(app)
# - + - + - - + - + - - + - + - - + - + -
# Validations
# - + - + - - + - + - - + - + - - + - + -
class LoginForm(FlaskForm):
	firstname = StringField('firstname', validators=[DataRequired()])
	password  = StringField('password', validators=[DataRequired()])
# - + - + - - + - + - - + - + - - + - + -
# Get Documents
# - + - + - - + - + - - + - + - - + - + -
def showUsers():
	cursor = collection.find()
	for doc in cursor:
		print(doc)
def getUsers():
	cursor = collection.find()
	return cursor
def getUser(_id):
	_id    = ObjectId(_id)
	cursor = collection.find_one({"_id": _id })
	return cursor
# Upload files	
def uploadFiles():
	target = os.path.join(app.config['UPLOAD_FOLDER'], 'static/uploads/')
	if not os.path.isdir(target):
		os.mkdir(target)
	for file in request.files.getlist('photo'):
		seconds = int(time.time())
		filename = file.filename
		extension = filename.rsplit('.', 1)[1].lower()
		nfilename = "{}.{}".format(seconds, extension)
		destination = "/".join([target, nfilename])
		file.save(destination)
	return nfilename
# Delete files
def deleteFiles(_id):
	cursor = getUser(_id)
	target = os.path.join(app.config['UPLOAD_FOLDER'] + "/static/", cursor['photo'])
	if os.path.isfile(target):
		os.remove(os.path.join(app.config['UPLOAD_FOLDER'] + "/static/", cursor['photo']))
		return True
	else:
		return False
# Security
def securityPassPort():
	if 'firstname' in session:
		return True
	else:
		return False
# - + - + - - + - + - - + - + - - + - + -
# Connect mongoDB
# - + - + - - + - + - - + - + - - + - + -
try:
	mongo      = pymongo.MongoClient('mongodb://localhost:27017/')
	database   = mongo.adsimongo
	collection = database.users
	#showUsers()
except Exception as e:
	print("Error mongoDB: " + e)
# - + - + - - + - + - - + - + - - + - + -
# Routes
# - + - + - - + - + - - + - + - - + - + -
# Welcome
@app.route('/')
def welcomeView():
	#return "Hello ADSI"
	if securityPassPort():
		return render_template('index.html', cursor=getUsers())
	else:
		form = LoginForm()
		return render_template('login.html', form=form)
# Login
@app.route('/login', methods=['POST'])
def login():
	try:
		form = LoginForm()
		if form.validate_on_submit():
			_firstname = request.form['firstname']
			_password  = request.form['password']
			check_user = collection.find_one({"firstname": _firstname })
			if check_user:
				if check_password_hash(check_user['password'], _password):
					session['firstname'] = check_user['firstname']
					session['lastname']  = check_user['lastname']
					session['photo']     = check_user['photo']
					return redirect('/')
				else:
					flash('Datos de ingreso incorrectos!')
					return redirect('/')
			else:
				flash('Datos de ingreso incorrectos!')
				return redirect('/')
		return render_template('login.html', form=form)
	except Exception as e:
		print(e)
# Logout
@app.route('/logout')
def logout():
    session.pop('firstname',None)
    session.pop('lastname',None)
    session.pop('photo',None)
    return redirect('/')
# Add User		
@app.route('/users/add')
def usersAddForm():
	if securityPassPort():
		return render_template('users/add.html')
	else:
		flash('Acceso Denegado!')
		form = LoginForm()
		return render_template('login.html', form=form)
@app.route('/users', methods=['POST'])
def userAdd():
	try:
		_firstname = request.form['firstname']
		_lastname  = request.form['lastname']
		_password  = request.form['password']
		# upload file
		filename = uploadFiles()
		_photo       = 'uploads/'+filename
		_hashed_pass = generate_password_hash(_password)
		collection.insert_one({'firstname': _firstname, 'lastname': _lastname, 'photo': _photo, 'password': _hashed_pass})
		flash('Usuario Adicionado con exito!')
		return redirect('/')
	except Exception as e:
		print(e)
@app.route('/users/edit/<_id>')
def userEditForm(_id):
	if securityPassPort():
		return render_template('users/edit.html', cursor=getUser(_id))
	else:
		flash('Acceso Denegado!')
		return render_template('login.html')
@app.route('/users/<_id>', methods=['POST'])
def userUpdate(_id):
	try:
		_firstname = request.form['firstname']
		_lastname  = request.form['lastname']
		_id        = ObjectId(_id)
		# upload file
		if not request.files.get('photo', None):
			nvalues    = {"$set":{"firstname": _firstname, "lastname": _lastname}}
		else:
			deleteFiles(_id)
			filename = uploadFiles()
			_photo       = 'uploads/'+filename
			nvalues    = {"$set":{"firstname": _firstname, "lastname": _lastname, "photo": _photo}}
		collection.update_one({"_id": _id }, nvalues)
		flash('Usuario Modificado con exito!')
		return redirect('/')
	except Exception as e:
		print(e)
@app.route('/users/delete/<_id>')
def userDelete(_id):
	_id    = ObjectId(_id)
	if deleteFiles(_id):
		collection.delete_one({"_id": _id })
		flash('Usuario Eliminado con exito!')
		return redirect('/')
@app.errorhandler(404)
def not_found(e):
	return render_template("404.html")
# - + - + - - + - + - - + - + - - + - + -
if __name__ == "__main__":
	app.run(port=5050, debug=True)