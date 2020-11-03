from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import PasswordField, StringField, SubmitField


class ReceiptForm(FlaskForm):
    scan_result = StringField("Результат сканирования", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    submit = SubmitField("Добавить")
