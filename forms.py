from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField
from flask_wtf.file import FileField


##WTForm

class CreateItemForm(FlaskForm):
    item_name = StringField("Item", validators=[DataRequired()])
    item_code = StringField("Code", validators=[DataRequired()])
    item_unit = StringField("Unit", validators=[DataRequired()])
    submit = SubmitField("Save Item")


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    submit = SubmitField("Log Me In!")
