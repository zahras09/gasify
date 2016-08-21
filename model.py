
# Google maps API key:
AIzaSyCKdnL2Tl4kXtLF7chKpyA-Z5_aJhEjbeM


# Gasfeed API:
Your Api Key: c2pmuvu4mv 

Once your app is complete and released you may submit your app to our 3rd party showcase section.
3rd Party Apps 

Please remember we have two different development environments which uses different domains. 

Development
Domain: devapi.mygasfeed.com
Api key: rfej9napna (All developers) 

Production
Domain: api.mygasfeed.com
Api key: c2pmuvu4mv 

#---------------------------------------------------------------------#


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class Traveler(db.Model):
	"""Traveler using the website."""

	 __tablename__ = "travelers"

    traveler_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    miles_per_gallon = db.Column(db.Integer, nullable=True)
    tank_capacity = db.Column(db.Integer, nullable=True)
    # tank_capacity = db.Column(db.String(64), nullable=True)

    # what happens if __repr__ is not here?
    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Traveler traveler_id=%s miles_per_gallon=%s tank_capacity%s>" % (self.traveler_id,
                                               self.miles_per_gallon, self.tank_capacity)




class Trip(db.Model):
	"""Saved trips info. including the start point and destination."""

	 __tablename__ = "trips"

    trip_id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    traveler_id = db.Column(db.Integer, foreign_key=True)
    # this would be a name in addition to lat.,lng.?
    latstart_point = db.Column(db.Integer, nullable=True)
    # this would be a name in addition to lat.,lng.?
    destination = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

    return "<Trip traveler_id=%s start_point=%s destination%s>" % (self.traveler_id,
                                               self.start_point, self.destination)



class GasStation(db.Model):
	"""Gas stations along the path of travel."""

	 __tablename__ = "stations"

    gas_station_id = db.Column(db.Integer, primary_key=True,nullable=True)
    traveler_id = db.Column(db.Integer, foreign_key=True)
    price = db.Column(db.Integer, nullable=True)
    # this will be lat.lng, do I also include a name?location?
    # favorite_gas_station = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        """Provide helpful representation when printed."""

    return "<Trip traveler_id=%s start_point=%s destination%s>" % (self.traveler_id,
                                               self.start_point, self.destination)



#---------------------------------------------------------------------#

def connect_to_db(app):
    """Connect the database to Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///bears'
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    print "Connected to DB."
