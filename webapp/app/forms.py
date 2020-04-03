from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField 
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app import bcrypt
from app.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                        validators=[DataRequired(), 
                        Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(),
                        Email()])
    password = PasswordField('Password', validators=[DataRequired(),])
    confirm_password = PasswordField('Confirm password', 
                                    validators=[DataRequired(),
                                    EqualTo('password')])
    submit = SubmitField('Sign up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data.lower()).first()
        if user:
            raise ValidationError('That username is taken. Please choose another one. This fild is not case sensitive.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is associated to an account. Try resetting the password.')

class LoginForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(),
                        Email()])
    password = PasswordField('Password', validators=[DataRequired(),])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log in')



class UpdateAccountForm(FlaskForm):

    profile_image_file = FileField('Update Profile picture.', validators=[FileAllowed(['jpg','png'])])
    email = StringField('Email', validators=[Email()])
    new_password = PasswordField('New password')
    confirm_new_password = PasswordField('Confirm new password', 
                                         validators=[EqualTo('new_password')])
    last_password = PasswordField('Actual password:', validators=[DataRequired(),])                    
    submit = SubmitField('Update')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is associated to other account. Try resetting the password.')

# class UpdateUserImagesForm(FlaskForm):

    


