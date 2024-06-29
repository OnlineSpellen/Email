from flask import Flask, render_template, request
import smtplib
import time

app = Flask(__name__)

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/send-emails', methods=['POST'])
def send_emails():
    try:
        # Email credentials (replace with your own)
        sender_email = "cf77d49527b6159@outlook.com"
        sender_password = "Outlook@2000"

        # Form inputs from the user
        num_emails = int(request.form['num_emails'])
        recipient_email = request.form['recipient_email']

        # SMTP setup
        with smtplib.SMTP('smtp.office365.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(sender_email, sender_password)

            # Sending emails
            for i in range(num_emails):
                smtp.sendmail(sender_email, recipient_email, "Testbericht")
                print(f"Email {i+1} sent to {recipient_email}")
                time.sleep(1)

        message = "All emails successfully sent!"
    except Exception as e:
        message = f"An error occurred: {str(e)}"

    return render_template('result.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
