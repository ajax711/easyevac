from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__, template_folder='templates')
 
 
@app.route("/")
def index():
    return render_template(
        'index.html')
 
 
@app.route("/about-us")
def about_us():
        return render_template(
        'about_us.html')
 
@app.route("/evac-locations")
def evac_locations():
    return render_template(
        'evac_locations.html')
 

@app.route("/find-volunteers")
def find_volunteers():
    return render_template(
        'find_volunteers.html')
 
@app.route("/updates")
def updates():
    return render_template(
        'updates.html')
 

@app.route("/volunteers-near-you")
def volunteers_near_you():
    return render_template(
        'volunteers_near_you.html')
  

@app.route("/near-me")
def near_me():
    return render_template(
        'near_me.html')
		
		
@app.route("/sos")
def sos_automated_updated():
    return render_template(
        'sos.html') 
 
if __name__ == "__main__":
    app.run()