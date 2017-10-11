from flask import Flask, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def display_form():
    return render_template('index.html', username='', username_error='', password='', password_error='', verpassword='', verpassword_error ='', email='', email_error='')

@app.route('/', methods=['POST'])
def validate_signup():

    username = request.form['username']
    password = request.form['password']
    verpassword = request.form['verpassword']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verpassword_error = ''
    email_error = ''

    if len(username) < 3 or len(username) > 20:
        username_error = 'Not a valid username.'
    if username.find(' ') >= 1:
        username_error = 'Not a valid username.' 

    if len(password) < 3 or len(password) > 20:
        password_error = 'Not a valid password.'
    if password.find(' ') >= 1:
        password_error = 'Not a valid password.'
    if len(verpassword) == 0:
        verpassword_error = 'Passwords do not match.'
    if verpassword != verpassword.replace(verpassword, password):
            verpassword_error = 'Passwords do not match.'
            password= 'Passwords do not match.'

    if len(email) != 0:
        if len(email) <3 or len(email) >20:
            email_error = 'Not a valid email.'
        if '@' not in email or ' ' in email or '.' not in email:
            email_error = 'Not a valid email.' 
        
    if not username_error and not password_error and not verpassword_error and not email_error:
        return render_template('welcomepage.html', username=username)

    else:
        return render_template('index.html', username=username, username_error=username_error, password='', 
        password_error=password_error, verpassword='', verpassword_error=verpassword_error, email='', email_error=email_error)       

app.run()