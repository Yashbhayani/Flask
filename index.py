import os
from distutils.log import debug
from fileinput import filename
from flask import Flask, make_response, redirect, render_template, request, session, url_for
# from flask import *

UPLOAD_FOLDER = 'image'

app = Flask(__name__, template_folder='template', static_folder='css')
app.secret_key = "Yash"  
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def home():
    return "hello, this is our first flask website"


@app.route('/log')
def log():
    return render_template('login.html')


@app.route('/log1')
def log1():
    return render_template('login1.html')


@app.route('/home/<name>')
def de(name):
    return "hello,"+name


@app.route('/admin')
def admin():
    return 'admin'


@app.route('/librarion')
def librarion():
    return 'librarion'


@app.route('/student')
def student():
    return 'student'


@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    if name == 'librarion':
        return redirect(url_for('librarion'))
    if name == 'student':
        return redirect(url_for('student'))


# ----------------------------------------------------------------------------------------------------------------------
# request methode
@app.route('/login', methods=['POST'])
def login():
    uname = request.form['uname']
    passwrd = request.form['pass']
    if uname == "ayush" and passwrd == "google":
        return "Welcome %s" % uname

    return render_template('login.html')


@app.route('/login1', methods=['GET'])
def login1():
    uname = request.args.get('uname')
    passwrd = request.args.get('pass')
    if uname == "ayush" and passwrd == "google":
        return "Welcome %s" % uname

    return render_template('login1.html')


# ----------------------------------------------------------------------------------------------------------------------
# Template
@app.route('/temp')
def message():
    return "<html><body><h1>Hi, welcome to the website</h1></body></html>"


@app.route('/temp1')
def message1():
    return render_template('message.html')


@app.route('/users/<uname>')
def message2(uname):
    return render_template('admin.html', name=uname)


@app.route('/table/<int:num>')
def table(num):
    return render_template('print-table.html', n=num)


# ----------------------------------------------------------------------------------------------------------------------
# Data
@app.route('/data')
def customer():
    return render_template('customer.html')


@app.route('/success', methods=['POST', 'GET'])
def print_data():
    if request.method == 'POST':
        result = request.form
        return render_template("result_data.html", result=result)


# ----------------------------------------------------------------------------------------------------------------------
# cookie
@app.route('/cookie')
def cookie():
    res = make_response("<h1>cookie is set</h1>")
    res.set_cookie('name', 'Yash')
    return res


@app.route('/suclogin')
def suclogin():
    return render_template("suclogin.html")


@app.route('/suc', methods=['POST'])
def suc():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['pass']

    if password == "yash":
        resp = make_response(render_template('success.html'))
        resp.set_cookie('email', email)
        return resp
    else:
        return render_template("suclogin.html")
        # return redirect(url_for('error'))


@app.route('/viewprofile')
def profile():
    email = request.cookies.get('email')
    resp = make_response(render_template('profile.html', name=email))
    return resp


# -------------------------------------------------------------------------------------
# Session


@app.route('/ses')
def ses():
    return render_template("home.html")


@app.route('/lo')
def lo():
    return render_template("lo.html")


@app.route('/success2', methods=["POST"])
def success2():
        if request.method == "POST":
            session['email'] = request.form['email']
            print(session['email'])
        return render_template("s2.html")



@app.route('/logout2')
def logout2():
    if 'email' in session:
        session.pop('email', None)
        return render_template("logout2.html")
    else:
        return '<p>user already logged out</p>'


@app.route('/profile2')
def profile2():
    if 'email' in session:
        print("Yash", session['email'])
        email = session['email']
        return render_template("profile2.html", name=email)
    else:
        return '<p>Please login first</p>'

# --------------------------------------------------------------------------------------------
@app.route('/upload')  
def upload():  
    return render_template("file_upload_form.html")  
 
@app.route('/s', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))  
        return render_template("s.html", name = f.filename)  

if __name__ == "__main__":
    app.run(debug=True)
