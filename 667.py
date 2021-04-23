from flask import Flask, render_template, redirect
from flask_login import LoginManager, login_user, login_required, logout_user
import sqlite3

from data import db_session
from data.login_form import LoginForm
from data.users import User
from data.register import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)
con = sqlite3.connect('db/base.db')
cur = con.cursor()

shirt_description = cur.execute("""SELECT description FROM products
                    WHERE view = 1""").fetchall()

hoodie_description = cur.execute("""SELECT description FROM products
                    WHERE view = 2""").fetchall()

price_shirts = cur.execute("""SELECT price FROM products
                    WHERE view = 1""").fetchall()

price_hoodies = cur.execute("""SELECT price FROM products
                    WHERE view = 2""").fetchall()

con.commit()
con.close()
shirts_cs_go = []  # список футболок кс го
hoodies_cs_go = []  # список толстовок кс го

price_shirt = price_shirts[0][0]
price_hoodie = price_hoodies[0][0]

description_shirt = shirt_description[0][0].split(';')  # описание футболки
description_hoodie = hoodie_description[0][0].split(';')  # описание толстовки



# футболки кс го
@app.route('/shirt_cs_go_1')
def shirt_cs_go_1():
    return render_template('Product.html', price=price_shirt, number="1", spisok_view=description_shirt, size=['XS', 'S', 'M', 'L'], game='CS GO', view='Футболки', view_product='Футболка')


@app.route('/shirt_cs_go_2')
def shirt_cs_go_2():
    return render_template('Product.html', price=price_shirt, number="2", spisok_view=description_shirt, size=['XS', 'S', 'M', 'L'], game='CS GO', view='Футболки', view_product='Футболка')


@app.route('/shirt_cs_go_3')
def shirt_cs_go_3():
    return render_template('Product.html', price=price_shirt, number="3", spisok_view=description_shirt, size=['XS', 'S', 'M', 'L'], game='CS GO', view='Футболки', view_product='Футболка')


@app.route('/shirt_cs_go_4')
def shirt_cs_go_4():
    return render_template('Product.html', price=price_shirt, number="4", spisok_view=description_shirt, size=['XS', 'S', 'M', 'L'], game='CS GO', view='Футболки', view_product='Футболка')


@app.route('/shirt_cs_go_5')
def shirt_cs_go_5():
    return render_template('Product.html', price=price_shirt, number="5", spisok_view=description_shirt, size=['XS', 'S', 'M', 'L'], game='CS GO', view='Футболки', view_product='Футболка')


@app.route('/shirt_cs_go_6')
def shirt_cs_go_6():
    return render_template('Product.html', price=price_shirt, number="6", spisok_view=description_shirt, size=['XS', 'S', 'M', 'L'], game='CS GO', view='Футболки', view_product='Футболка')


# толстовки кс го
@app.route('/hoodie_cs_go_1')
def hoodie_cs_go_1():
    return render_template('Product.html', price=price_hoodie, number="1", spisok_view=description_hoodie, size=['XS', 'S', 'M', 'L'], game='CS GO', view='Толстовки', view_product='Толстовка')


@app.route('/hoodie_cs_go_2')
def hoodie_cs_go_2():
    return render_template('Product.html', price=price_hoodie, number="2", spisok_view=description_hoodie, size=['XS', 'S', 'M', 'L'], game='CS GO', view='Толстовки', view_product='Толстовка')


@app.route('/hoodie_cs_go_3')
def hoodie_cs_go_3():
    return render_template('Product.html', price=price_hoodie, number="3", spisok_view=description_hoodie, size=['XS', 'S', 'M', 'L'], game='CS GO', view='Толстовки', view_product='Толстовка')


@app.route('/hoodie_cs_go_4')
def hoodie_cs_go_4():
    return render_template('Product.html', price=price_hoodie, number="4", spisok_view=description_hoodie, size=['XS', 'S', 'M', 'L'], game='CS GO', view='Толстовки', view_product='Толстовка')


@app.route('/hoodie_cs_go_5')
def hoodie_cs_go_5():
    return render_template('Product.html', price=price_hoodie, number="5", spisok_view=description_hoodie, size=['XS', 'S', 'M', 'L'], game='CS GO', view='Толстовки', view_product='Толстовка')


@app.route('/hoodie_cs_go_6')
def hoodie_cs_go_6():
    return render_template('Product.html', price=price_hoodie, number="6", spisok_view=description_hoodie, size=['XS', 'S', 'M', 'L'], game='CS GO', view='Толстовки', view_product='Толстовка')

# футболки diablo
@app.route('/shirt_diablo_1')
def shirt_diablo_1():
    return render_template('Product.html', price=price_shirt, number="1", spisok_view=description_shirt, size=['XS', 'S', 'M', 'L'], game='DIABLO', view='Футболки', view_product='Футболка')


@app.route('/shirt_diablo_2')
def shirt_diablo_2():
    return render_template('Product.html', price=price_shirt, number="2", spisok_view=description_shirt, size=['XS', 'S', 'M', 'L'], game='DIABLO', view='Футболки', view_product='Футболка')


@app.route('/shirt_diablo_3')
def shirt_diablo_3():
    return render_template('Product.html', price=price_shirt, number="3", spisok_view=description_shirt, size=['XS', 'S', 'M', 'L'], game='DIABLO', view='Футболки', view_product='Футболка')


@app.route('/shirt_diablo_4')
def shirt_diablo_4():
    return render_template('Product.html', price=price_shirt, number="4", spisok_view=description_shirt, size=['XS', 'S', 'M', 'L'], game='DIABLO', view='Футболки', view_product='Футболка')


@app.route('/shirt_diablo_5')
def shirt_diablo_5():
    return render_template('Product.html', price=price_shirt, number="5", spisok_view=description_shirt, size=['XS', 'S', 'M', 'L'], game='DIABLO', view='Футболки', view_product='Футболка')


@app.route('/shirt_diablo_6')
def shirt_diablo_6():
    return render_template('Product.html', price=price_shirt, number="6", spisok_view=description_shirt, size=['XS', 'S', 'M', 'L'], game='DIABLO', view='Футболки', view_product='Футболка')


# толстовки diablo
@app.route('/hoodie_diablo_1')
def hoodie_diablo_1():
    return render_template('Product.html', price=price_hoodie, number="1", spisok_view=description_hoodie, size=['XS', 'S', 'M', 'L'], game='DIABLO', view='Толстовки', view_product='Толстовка')


@app.route('/hoodie_diablo_2')
def hoodie_diablo_2():
    return render_template('Product.html', price=price_hoodie, number="2", spisok_view=description_hoodie, size=['XS', 'S', 'M', 'L'], game='DIABLO', view='Толстовки', view_product='Толстовка')


@app.route('/hoodie_diablo_3')
def hoodie_diablo_3():
    return render_template('Product.html', price=price_hoodie, number="3", spisok_view=description_hoodie, size=['XS', 'S', 'M', 'L'], game='DIABLO', view='Толстовки', view_product='Толстовка')


@app.route('/hoodie_diablo_4')
def hoodie_diablo_4():
    return render_template('Product.html', price=price_hoodie, number="4", spisok_view=description_hoodie, size=['XS', 'S', 'M', 'L'], game='DIABLO', view='Толстовки', view_product='Толстовка')


@app.route('/hoodie_diablo_5')
def hoodie_diablo_5():
    return render_template('Product.html', price=price_hoodie, number="5", spisok_view=description_hoodie, size=['XS', 'S', 'M', 'L'], game='DIABLO', view='Толстовки', view_product='Толстовка')


@app.route('/hoodie_diablo_6')
def hoodie_diablo_6():
    return render_template('Product.html', price=price_hoodie, number="6", spisok_view=description_hoodie, size=['XS', 'S', 'M', 'L'], game='DIABLO', view='Толстовки', view_product='Толстовка')


@app.route('/hoodies_cs_go')
def hoodies_cs_go():
    return render_template('choice.html', choice='hoodie', game_link='cs_go', game='CS GO', view='Толстовки')


@app.route('/shirts_cs_go')
def shirts_cs_go():
    return render_template('choice.html', choice='shirt', game_link='cs_go', game='CS GO', view='Футболки')


@app.route('/choice_diablo')
def choice_diablo():
    return render_template('choice_product.html', choice='shirts', game_link='diablo', game='DIABLO')


@app.route('/choice_cs_go')
def choice_cs_go():
    return render_template('choice_product.html', choice='shirts', game_link='cs_go', game='CS GO')


@app.route('/shirts_diablo')
def shirts_diablo():
    return render_template('choice.html', choice='shirt', game_link='diablo', game='DIABLO', view='Футболки')


@app.route('/hoodies_diablo')
def hoodies_diablo():
    return render_template('choice.html', choice='hoodie', game_link='diablo', game='DIABLO', view='Толстовки')


@app.route('/basket_cs_go_price_shirt_1')
def karzin():
    id_products = cur.execute("""SELECT id_products FROM karzins
                        WHERE view = 1""").fetchall()
    cur.execute(f"""UPDATE karzins SET id_products = {id_products + 1}
                            WHERE view = 1""").fetchall()
    return redirect("/basket")


@app.route('/basket')
def basket():
    return render_template("basket.html")

@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html', message="Неверный логин или пароль", form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/main_page')
def main_page():
    return render_template('main.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация', form=form,
                                   message="Пароли не совпадают")
        session = db_session.create_session()
        if session.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация', form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            surname=form.surname.data)
        user.set_password(form.password.data)
        session.add(user)
        session.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


if __name__ == '__main__':
    db_session.global_init("db/base.db")
    app.run(port=8080, host='127.0.0.1')
