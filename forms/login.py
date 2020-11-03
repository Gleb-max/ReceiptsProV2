from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import PasswordField, SubmitField, BooleanField, IntegerField


class LoginForm(FlaskForm):
    phone = IntegerField("Телефон", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    remember_me = BooleanField("Запомнить меня")
    submit = SubmitField("Войти")
