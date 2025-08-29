from flask import Flask, render_template, request, redirect, url_for
import os
from datetime import datetime

app = Flask(__name__)

# Routes
@app.route("/")
def home():
    return render_template("index.html", active_page='home')

@app.route("/about")
def about():
    return render_template("about.html", active_page='about')

@app.route("/skills")
def skills():
    return render_template("skills.html", active_page='skills')

@app.route("/projects")
def projects():
    return render_template("projects.html", active_page='projects')

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Process form data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Here you would typically save to database or send email
        print(f"New message from {name} ({email}): {message}")
        
        # Redirect to thank you page
        return redirect(url_for('contact_success'))
    
    return render_template("contact.html", active_page='contact')

@app.route("/contact/success")
def contact_success():
    return render_template("contact_success.html")

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)