from flask import render_template, redirect
from flask_login import current_user, login_user
from app import create_app, db
from data.models import User
from fns.api import FnsApi
from forms.login import LoginForm
from forms.register import RegisterForm
from forms.restore import RestoreForm

app = create_app()


@app.route("/")
def index():
    receipts = []
    if current_user.is_authenticated:
        return "1"
        # session = db.create_session()
        # receipts = session.query(Receipt).filter(Receipt.user == current_user).order_by(Receipt.date.desc()).all()
        # session.close()
    db.session.add(User("54822348843", "4847378fggf43", "vrtvirgfdfdfj"))
    db.session.commit()
    return redirect("/api/v2/users")
    # return render_template("index.html", receipts=receipts, title="Receipts Pro")


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect("/")
    form = LoginForm()
    if form.validate_on_submit():
        phone = str(form.phone.data)[1:]
        password = form.password.data
        result = FnsApi.login(phone, password)
        print(result.text, result.status_code)

        if result.status_code == 403:
            return render_template("login.html",
                                   message="Неправильный логин или пароль",
                                   form=form)
        elif result.status_code == 500:
            return render_template("login.html",
                                   message="ФНС поломался",
                                   form=form)

        session = db.session
        user = User.query.filter_by(phone=phone).first()
        if user is None:
            user = User(phone=phone)
            result_json = result.json()
            user.email = result_json["email"]
            user.name = result_json["name"]
            session.add(user)
            session.commit()
        login_user(user, remember=form.remember_me.data)
        session.close()
        return redirect("/")
    return render_template("login.html", title="Авторизация", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect("/")
    form = RegisterForm()
    if form.validate_on_submit():
        phone = str(form.phone.data)[1:]
        email = form.email.data
        name = form.name.data
        session = db.session

        if session.query(User).filter(User.phone == phone).first():
            session.close()
            return render_template("register.html", title="Регистрация",
                                   form=form,
                                   message="К этому номеру уже привязан аккаунт")

        result = FnsApi.register(phone, email, name)
        print(result.text, result.status_code)

        if result.status_code == 204:
            user = User(phone=phone, name=name, email=email)
            session.add(user)
            session.commit()
            session.close()
            return redirect("/login")
        if result.status_code == 409:
            session.close()
            return render_template("register.html", title="Регистрация",
                                   form=form,
                                   message="К этому номеру уже привязан аккаунт")
        if result.status_code == 500:
            session.close()
            return render_template("register.html", title="Регистрация",
                                   form=form,
                                   message="Неверно указан номер телефона")
        # default:
        session.close()
        return render_template("register.html", title="Регистрация",
                               form=form,
                               message="К этому номеру уже привязан аккаунт")
    return render_template("register.html", title="Регистрация", form=form)


@app.route("/restore", methods=["GET", "POST"])
def restore():
    if current_user.is_authenticated:
        return redirect("/")
    form = RestoreForm()
    if form.validate_on_submit():
        phone = str(form.phone.data)[1:]
        result = FnsApi.restore(phone)
        print(result.text, result.status_code)

        if not result.text:
            return redirect("/login")

        return render_template("restore.html",
                               message="Неверный номер телефона",
                               form=form)
    return render_template("restore.html", title="Восстановление", form=form)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()
