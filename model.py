
# # Google maps API key:
# AIzaSyCKdnL2Tl4kXtLF7chKpyA-Z5_aJhEjbeM


# # Gasfeed API:
# Your Api Key: c2pmuvu4mv 

# Development
# Domain: devapi.mygasfeed.com
# Api key: rfej9napna (All developers) 

# Production
# Domain: api.mygasfeed.com
# Api key: c2pmuvu4mv 

#---------------------------------------------------------------------#

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """Traveler using the website."""
    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String)
    password = db.Column(db.String)


    # miles_per_gallon = db.Column(db.Integer, nullable=True)
    # tank_capacity = db.Column(db.Integer, nullable=True)
    # tank_capacity = db.Column(db.String(64), nullable=True)

    # what happens if __repr__ is not here?
    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User user_id=%s email=%s password%s>" % (self.user_id,
                                                                  self.email, 
                                                                  self.password)




class Trip(db.Model):
    """Saved trips info. including the start point and destination."""

    __tablename__ = "trips"

    trip_id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    # this would be a name in addition to lat.,lng.?
    start = db.Column(db.String, nullable=True)
    end = db.Column(db.String, nullable=True)


    user = db.relationship("User",
                            backref=db.backref("trips"))


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Trip trip_id=%s start=%s end%s>" % (self.user_id,
                                                           self.start, 
                                                           self.end)


class GasStation(db.Model):
    """Gas stations along the path of travel."""
    __tablename__ = "gasstations"

    gas_station_id = db.Column(db.Integer, primary_key=True,nullable=True)
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.trip_id'))
    location = db.Column(db.String)
    name = db.Column(db.String)

    trip = db.relationship("Trip",
                            backref=db.backref("gasstations"))



    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<GasStation gas_station_id=%s name=%s >" % (self.gas_station_id,
                                                                            self.name)



#---------------------------------------------------------------------#

def connect_to_db(app):
    """Connect the database to Flask app."""

    ####### WHAT IS THE PURPOSE OF APP.CONFIG???!!!!!!!!################
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///gasify'
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    print "Connected to DB."
