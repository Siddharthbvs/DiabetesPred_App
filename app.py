from flask import Flask, render_template
from models import init_db,add_user,check_user

app = Flask(__name__)
app.secret_key = "secret123"

#initialize the database
init_db()
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register',methods = ['POST'])
def register():
    usernamer = request.form['username']
    password = request.form['password']
    add_user(usernamer,password)
    return render_template('index.html',message="Registration Successful")

@app.route('/login',methods = ['POST'])
def login():
    usernamel = request.form['username']
    password = request.form['password']

    if check_user(usernamel,password):
        return render_template('login.html',message="Login Successful")
    else:
        return render_template('index.html',message="Invalid Credentials")
    
    @app.route('/login-page')
    def login_page():
        return render_template('login.html')    
    
if __name__ == '__main__':
    app.run(debug=True)
    