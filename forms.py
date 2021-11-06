from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Equalto


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2,max=20))
    email = StringField('Email',
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confim_password = PasswordField('Password', validators=[DataRequired(), Equalto('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email',
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ChatMessage(FlaskForm):
    chat_message = StringField('Message')
    submit = SubmitField('Send')
