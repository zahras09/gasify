"""Utility file to seed ratings database from MovieLens data in seed_data/"""

# import datetime
from sqlalchemy import func

from model import User, connect_to_db, db
from server import app


def load_user():
    """Load users from u.user into database."""

    print "User"
    
    email = 'zahra@gmail.com'
    password = 'hackbright'


    user = User(email=email,
                password=password)

    # We need to add to the session or it won't ever be stored
    db.session.add(user)

    
    # Once we're done, we should commit our work
    db.session.commit()


# def load_start():
#     """Load start location into database."""

#     print "Start"


#         start = Start(user_id=user_id)

#         # We need to add to the session or it won't ever be stored
#         db.session.add(movie)


#     # Once done,commit work
#     db.session.commit()


# def load_end():
#     """Load end location into database."""

#     print "End"

        

#         start_id = int(start_id)
#         user_id = int(user_id)

#         end = End(start_id=start_id,
#                   user_id=user_id)

#         # We need to add to the session or it won't ever be stored
#         db.session.add(rating)

#     # Once we're done, we should commit our work
#     db.session.commit()


# def load_trip():
#     """Load trip id into database."""

#     print "Trip"
#         user_id = user_id
#         start_id = start_id
#         end_id = end_id

#         trip = Trip(user_id=user_id,
#                     start_id=start_id,
#                     end_id=end_id)


#         db.session.add()
#     db.session.commit()



# def load_gas_station():
#     """Load gas station id into database."""

#     print "GasStation"

#     user_id = user_id
#     trip_id = trip_id

#     gas_station = gasstation(user_id=user_id,
#                              trip_id=trip_id)

#         db.session.add()
#     db.session.commit()


# def set_val_user_id():
#     """Set value for the next user_id after seeding database"""

#     # Get the Max user_id in the database
#     result = db.session.query(func.max(User.user_id)).one()
#     max_id = int(result[0])

#     # Set the value for the next user_id to be max_id + 1
#     query = "SELECT setval('users_user_id_seq', :new_id)"
#     db.session.execute(query, {'new_id': max_id + 1})
#     db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

    load_user()
    # load_start()
    # load_end()
    # load_trip()
    # load_gas_station()
    # set_val_user_id()





