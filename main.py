from flask import Flask, render_template, redirect, request, url_for, abort
from datetime import datetime as dt
from notificationManager import NotificationManager

app = Flask(__name__)



@app.route("/")
def home():
    now = dt.now()
    year = now.year
    return render_template("index.html", current_year=year)

@app.route("/contact-me",methods=['GET','POST'])
def contactme():
    now = dt.now()
    year = now.year
    
    
    if request.method == 'POST':
        
        
        name = request.form['full-Name']
        email = request.form['email']
        message = request.form['message']
       
        notify = NotificationManager()
        try:
            notify.send_email(name=name, email=email, message=message)
        except:
            return abort(500)
        else:
            return redirect(url_for("success"))
        

    page_title = "Contact Me"

    return render_template("contact-me.html",page_title=page_title, current_year=year)

@app.route("/contact-success")
def success():
    page_title = "Message Successfully Sent!"
    return render_template("contact-me.html", page_title=page_title)



if __name__ == "__main__":
    app.run(debug=True)