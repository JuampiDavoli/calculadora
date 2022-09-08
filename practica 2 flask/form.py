from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length

class Form(FlaskForm):

#completar lo de abajo
    name=StringField("Name", validators=[DataRequired(), Length(min=3, max=20, message="none")])
    password=PasswordField("Password",validators=[DataRequired(), Length(min=8)])
    email=StringField("Email",validators=[DataRequired(), Email()])
    submit=SubmitField("Registrar")