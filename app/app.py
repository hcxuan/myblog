from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

class AdminForm(Form):
	username = StringField('username', validators=[Required()])
 	password = PasswordField('Password', validators=[Required()])
 	submit = SubmitField('Submit')
    

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/admin', methods=['GET', 'POST'])
def admin():
	username = None
	password = None
	form = AdminForm()
	if form.validate_on_submit():
		username = form.username.data
		form.username.data = ''
		password = form.password.data
		form.password.data = ''
	return render_template('admin.html', form=form, username=username,password=password)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'),500

if __name__ == '__main__':
	manager.run()