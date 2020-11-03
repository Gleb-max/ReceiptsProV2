from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    name = StringField("Имя", validators=[DataRequired()])
    email = EmailField("Почта", validators=[DataRequired()])
    phone = IntegerField("Телефон", validators=[DataRequired()])
    submit = SubmitField("Зарегистрироваться")
