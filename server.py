
# import secrets.sh
import gasfeed
import os
import json
from flask import Flask, render_template, request, redirect, jsonify, flash, session
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"
from model import connect_to_db, db, User, Trip, GasStation


# url = "https://maps.googleapis.com/maps/api/js?key=" + GOOGLE_API_KEY + "&callback=initMap"
# consumer_secret=os.environ

# DISPLAY HOMEPAGE AND HAVE THE USER LOGIN:
@app.route('/', methods=['GET'])
def index():
    """Homepage"""
    return render_template("homepage.html")



# LOGIN PROCESS:
@app.route('/log_in', methods=['POST'])
def login_process():
    """Process login."""

    # Get form variables
    my_email = request.form.get("email")
    password = request.form.get("password")

    print "my email"
    print my_email

    user = User.query.filter_by(email=my_email).first()
    print "user"
    print user

    if not user:
        flash("User not found!")
        return redirect("/")

    if user.password != password:
        flash("Incorrect password")
        return redirect("/")
    else:
        # session is a dict. and you want to set the key user id to user.user_id.
        session['user_id'] = user.user_id
        return redirect('/destination-form')

# once user clicks submit route them to /destination-form page and display the form
@app.route('/destination-form', methods=['GET'])
def destination_form():
    """Shows form for user to enter route info."""

    return render_template('destination.html')


# when form is filled take user to /destination-process
@app.route('/destination-form')
def process_destination_form():
    return redirect("/destination-process")



# when user arrives at /destination-process display map_display.html
@app.route('/destination-process', methods=['POST'])
def destination_process():
    """Processes the user's input"""

    # user_entered_start_point = request.form['start-point'] # KeyError if not there
    user_entered_start_point = request.form.get("start") # None if not there.
    user_entered_destination = request.form.get("end")

    # map_display is my jinja, start" and end variables are from destination.html
    return render_template("map_display.html", start=user_entered_start_point,
                                               end=user_entered_destination)






# SHOW USER THE FORM IN ORDER TO REGISTER:
# @app.route('/log_in', methods=['POST'])
# def register_process():
#     """Process registration."""

#     # Get form variables
#     email = request.form["email"]
#     password = request.form["password"]

#     new_user = User(email=email, password=password)

#     db.session.add(new_user)
#     db.session.commit()

#     flash("User %s added." % email)
#     return redirect("/users/%s" % new_user.user_id)




@app.route('/logout')
def logout():
    """Log out."""

    del session["user_id"]
    flash("Logged Out.")
    return redirect("/")

# IS THIS ROUTE NECESSARY??????
# @app.route("/users/<int:user_id>")
# def user_detail(user_id):
#     """Show info about user."""

#     user = User.query.get(user_id)
#     return render_template("user.html", user=user)







############################## GASFEED #############################
# 
@app.route('/getgasstations.json', methods=['GET'])
def current_location():
    """  """
    #request for lat.,lng. for the route that the user has entered.
      #google gives the lat.lng. for the location.

    lat = request.args.get('lat') #If you want to retrieve GET (query string) data:
    lng = request.args.get('lng')

    # ITERATE OVER THE DICTIONARY TO ONLY GET WHAT IS NEEDED:
    # calling gas_stations funct. from gasfeed.py that takes in 2 params.lat,lng.
    stations = gasfeed.gas_stations(lat, lng)

    # calling the funct. (cheapest_gas_stations) from gasfeed.py and passing in the values(stations).cheap_stations
    #returns the cheapest stations' lat.,lng.
    cheap_stations = gasfeed.cheapest_gas_stations(stations)

    # RETURN JSONIFY DICT.
    # writting json data into python 
    return json.dumps(cheap_stations)





# @app.route('/googlemap', methods=['POST'])
# def map_image():
#     """Map user's route."""
#     # location = request.form.get("destination")
#     # print "test"
#     return render_template("googlemaps.html")





if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run(host='0.0.0.0', port=5000, debug=True)
