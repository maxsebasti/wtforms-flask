from flask import Flask, request, render_template, flash, redirect, url_for
from app import app
from app.forms import RegistrationForm

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        # Insert into database
        #user = User(form.username.data, form.email.data,
        #            form.password.data)
        #db_session.add(user)

        #flash('Thanks for registering')
        #return redirect(url_for('register'))
        results = [
            {
                "username": form.username.data,
                "email": form.email.data,
                "password": form.password.data
            }]

        return {"count": len(results), "users": results}
        #return 'Thanks for registering'
    else:
        return render_template('register.html', form = form)
