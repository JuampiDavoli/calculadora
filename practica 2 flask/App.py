import email
from unicodedata import name
from flask import Flask, render_template, request

app=Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
from form import Form

@app.route("/form/", methods=["GET", "POST"])
def formulario():
    login_form=Form(request.form)
    if request.method =="POST" and login_form.validate():
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        
    return render_template("form.html", form=login_form)


if __name__=="__main__":
    app.run(debug=True,port=8000)