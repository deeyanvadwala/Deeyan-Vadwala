from flask import Flask,render_template,request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def homepg():
    return render_template('index.html')
@app.route('/submit-email', methods=['POST'])
def submit_email():
    # Print the form data for debugging
    print(request.form)

    # Use get() method to safely access form data
    email = request.form.get('email')

    if email:
        # Append the email to a text file
        with open('emails.txt', 'a') as f:
            f.write(f"{email}\n")
        # Redirect back to the homepage or a thank you page
        return redirect(url_for('homepg'))
    else:
        # Handle the case where the email is missing
        return "Email field is missing!", 400
if __name__ == "__main__":
    app.run(debug=True)