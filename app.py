from flask import Flask, render_template, request
from flask_mail import Mail, Message
import config
app = Flask(__name__, static_folder='static')


# Configure Flask-Mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = config.mail_user
app.config['MAIL_PASSWORD'] = config.mail_password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# Initialize Flask-Mail
mail = Mail(app)

# Define the routes for the different pages of your website
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Extract form data
    first_name = request.form['first-name']
    last_name = request.form['last-name']
    email = request.form['email']
    description = request.form['description']
    payment = request.form['payment']

    # Send email to your designated email address
    msg = Message('New Form Submission', sender=config.mail_user, recipients=[config.mail_user])
    msg.body = f"First Name: {first_name}\nLast Name: {last_name}\nEmail: {email}\nDescription: {description}\nPayment: ${payment}"
    mail.send(msg)

    return 'Form submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)