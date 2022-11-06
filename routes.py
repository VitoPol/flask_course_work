from app import app, db
from models import Employees
from flask import render_template, request, redirect

@app.route("/")
def index():
    employees = Employees.query.all()
    return render_template("index.html", employees=employees)


@app.route("/update", methods=["POST"])
def update():
    form = request.form.to_dict()
    res = Employees.query.get(form['id'])
    res.name = form['name']
    res.email = form['email']
    res.phone = form['phone']
    db.session.add(res)
    db.session.commit()
    return redirect("/")


@app.route("/delete/<emp_id>")
def delete(emp_id):
    res = Employees.query.get(emp_id)
    db.session.delete(res)
    db.session.commit()
    return redirect("/")


@app.route("/insert", methods=["POST"])
def insert():
    form = request.form.to_dict()
    new = Employees(
        name=form['name'],
        email=form['email'],
        phone=form['phone']
    )
    db.session.add(new)
    db.session.commit()
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
