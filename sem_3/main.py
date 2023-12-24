from flask import Flask, render_template, request
from login_form import LoginForm
from model import db, User
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)

@app.route('/')
def hello():
    return 'Hello!'

@app.route('/registration/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        name = form.username.data
        email = form.email.data
        password = form.password.data
        user = User(username=name, email=email, password=password)
        try:
            db.session.add(user)
            db.session.commit()
            return 'Вы успешно зарегистрировались!'
        except Exception as e:
            print(e)
            return 'Возникла ошибка'
    return render_template('registration.html', form=form)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('OK')


if __name__ == '__main__':
    app.run()