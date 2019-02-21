# Cyber Attacks risks awareness project by Irdi Caushaj
# Ethical Hacking class COS 310a S2019
# Technologies used: Python, Flask, HTML, CSS

from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)
 

# Home routes
@app.route('/')
def hello():
    return render_template('home.html')
 

@app.route('/home')
def home():
    return render_template('home.html')



# Categories routes
@app.route('/ransomware')
def ransomware():
    return render_template('ransomware.html')

@app.route('/ddos')
def ddos():
    return render_template('ddos.html')

@app.route('/mitm')
def mitm():
    return render_template('mitm.html')


# Popular risks for 2019 routes
@app.route('/biodata')
def bio():
    return render_template('bio_data.html')

@app.route('/aidata')
def ai():
    return render_template('ai_data.html')

@app.route('/phishing')
def phishing():
    return render_template('phishing.html')