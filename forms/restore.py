from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import SubmitField, IntegerField


class RestoreForm(FlaskForm):
    phone = IntegerField("Телефон", validators=[DataRequired()])
    submit = SubmitField("Восстановить")
