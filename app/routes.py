import io

from flask import render_template, redirect, url_for
from app import app
from app.forms import InputForm
from .db import sql_request
from.config import Config
import qrcode
import base64 as code



@app.route('/', methods=['GET', 'POST'])
def main():
    """
    Main page, offer to enter your data
    """
    form = InputForm()
    if form.validate_on_submit():
        sql = "INSERT INTO users (fio, chip) VALUES (%s, %s) RETURNING id;"
        fio = form.surname.data + " " + form.name.data + " " + form.patronymic.data
        params = (fio, form.chip.choices[int(form.chip.data) - 1][1],)
        result = sql_request(sql, params, True)

        sql = "UPDATE users SET url = %s WHERE id = %s;"
        encoded_id = str(code.b64encode(bytes(result)))[2:-1]
        params = (encoded_id, result,)
        result_2 = sql_request(sql, params, True, False)

        return redirect(url_for('user', user_id=encoded_id))
    return render_template("index.html", form=form)


@app.route('/<user_id>')
def user(user_id,):
    """
    Show user's info
    """
    sql = "SELECT * FROM users WHERE url = %s;"
    params = (user_id,)
    result = sql_request(sql, params)
    img = qrcode.make(Config.WEB_PATH + "/" + result[2])
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    base_64_img = str(code.b64encode(buffer.getvalue()))[2:-1]
    buffer.close()
    return render_template("user.html", user=result, img=base_64_img)


@app.errorhandler(404)
def not_found_error(error):
    """404 or user with chip not in db"""
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    """500 - Server Error"""
    return render_template('500.html'), 500

