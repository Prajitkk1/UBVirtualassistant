from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField , BooleanField, TextAreaField,SelectField
from wtforms.validators import DataRequired,Length,Email, EqualTo,ValidationError
from virtualassistant.models import User
from flask_wtf.file import FileField, FileAllowed




class RegistrationForm(FlaskForm):
    email = StringField('EMail',validators=[DataRequired(),Email()])
    name = StringField('Name',validators=[DataRequired()])
    mobile_no = StringField('Mobile number')
    department = StringField('Department')
    submit = SubmitField('sign up')

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('E-mail already exist')


