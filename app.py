
from flask import Flask, render_template, request,redirect
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
  host="localhost",
  user="student",
  password="123",
  database="laundry"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        mycursor = mydb.cursor()
        mycursor.execute(f"SELECT * FROM login_cred WHERE username = '{username}' and password = '{password}'")
       # myresult = mycursor.fetchall()
        student_details = mycursor.fetchall()
        if student_details:
            return render_template('home.html', student=student_details[0])
        return render_template('login.html')
    return render_template('login.html')



        # if myresult:
        #     return redirect('/home')
        # else:
        #     return render_template('login.html')
        # return f'Logged in as {username}'
    # return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        mycursor = mydb.cursor()
        sql = "INSERT INTO login_cred (username, email, password) VALUES (%s, %s, %s)"
        val = (username, email, password)
        mycursor.execute(sql, val)
        mydb.commit()

        return redirect('/home')

    return render_template('signup.html')

@app.route('/redirect_login', methods=['GET', 'POST'])
def redirect_login():
    return redirect('/login')

@app.route('/redirect_signup', methods=['GET', 'POST'])
def redirect_signup():
    return redirect('/signup')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/bag', methods=['GET', 'POST'])
def handle_bag():
    if request.method == 'POST':
        # Handle the 'Bag' button click
        # Add your logic here
        return render_template('bag.html')
    else:
        return render_template('home.html')  # Update to the appropriate template for 'bag'

@app.route('/history', methods=['GET', 'POST'])
def handle_history():
    if request.method == 'POST':
        # Handle the 'History' button click
        # Add your logic here
        return render_template('history.html')
    else:
        return render_template('home.html')  # Update to the appropriate template for 'history'

if __name__ == '__main__':
    app.run(debug=True)




if __name__ == '__main__':
    app.run(debug=True)

