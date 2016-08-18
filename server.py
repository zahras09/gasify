
# import secrets.sh
import gasfeed
import os
import json
from flask import Flask, render_template, request, redirect, jsonify
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# url = "https://maps.googleapis.com/maps/api/js?key=" + GOOGLE_API_KEY + "&callback=initMap"
# consumer_secret=os.environ

# display homepage
@app.route('/')
def index():
    """Homepage"""
    return render_template("homepage.html")



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


############################## GASFEED #############################
# 
@app.route('/getgasstations.json', methods=['GET'])
def current_location():
    """  """
    #request for lat.,lng. for the route that the user has entered.
      #google gives the lat.lng. for the location.

    # CALL API 
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

    # connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host='0.0.0.0', port=5000, debug=True)
