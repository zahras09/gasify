import json
# I don't think I need this:
import urllib2
import requests

url = 'api.mygasfeed.com'
api_key = "c2pmuvu4mv"


def gas_stations(lat,lng):
	gas_stations_info = []

	# access the MyGasFeed API
	r = requests.get("http://api.mygasfeed.com/stations/radius/" + lat + "/" + lng + "/10/reg/price/c2pmuvu4mv.json")
	gas_stations_info = r.json()

	return gas_stations_info['stations']


# Tested query : http://api.mygasfeed.com/stations/radius/37.7749/-122.4194/2/reg/distance/c2pmuvu4mv.json

# parameter: stations
# - stations is a list of dictionaries.
# - each dictionary represents one gas station
# - each dictionary looks like this:
#          {
#             "country": "Canada",
#             "reg_price": "3.65",
#             "mid_price": "3.65",
#             "pre_price": "3.65",
#             "diesel_price": "3.65",
#             "address": "3885, Boulevard Saint-Rose",
#             "diesel": "0",
#             "id": "33862",
#             "lat": "45.492367",
#             "lng": "-73.710915",
#             "station": "Shell",
#             "region": "Quebec",
#             "city": "Saint-Laurent",
#             "reg_date": "3 hours agp",
#             "mid_date": "3 hours agp",
#             "pre_date": "3 hours agp",
#             "diesel_date": "3 hours agp",
#             "distance": "1.9km"
#         }
def cheapest_gas_stations(stations):

    ####### find the cheapest stations and put them into `cheapest_stations`

	# return cheapest_stations


	# # create an empty list:
	prices_list = []

	# # iterate over every station in the whole list of stations:
	for station in stations:
		# add the price and and index of every station in stations list to the
	    # price_list.
		prices_list.append( (station['reg_price'],stations.index(station)) )

	# sort the list by price (having a tuple with the price first then the index)
	prices_list.sort()
	
	print "This is the price list!!!", prices_list

	cheapest_station_tuple = prices_list[0]

	cheapest_station_index = cheapest_station_tuple[1]
	cheapest_station = stations[cheapest_station_index]

	return cheapest_station


		# # this returns a tuple of price and index:
		# print cheapest_10_stations

		# ####### NEXT STEPS ##############
		# # Iterate over the cheapest_10_stations
		# # for each station tuple
		#     # we need to get index of that station from the tuple : tuple[1]
		#     # use the index to get the full station information from stations list
		# 	# then you get a dictionary that represent info about that station
		# 	# get data from that dictionary as needed


		# ####This iteration iterates over every station in cheapest_10_stations
		#  which only contains a price and an index as a tuple and passes those values
		#  into the variable index_of_station.
		#  stations_list[] return a list of 10 stations



	# stations_list = []
	# for cheap_station in cheapest_station:
	# 	# 	#cheap station[1] return the index of the station
	# 	index_of_station = cheap_station[0]
	# 	# 	# print "index_of_station:"
	# 	# 	# print index_of_station
	# 	station = stations[index_of_station]
	# 	# 	# station is the dictionary
	# 	stations_list.append(station)
	# 	# 	# print "-----------------"
			# print station

	# all_gas_stations = gas_stations("37.7749","-122.4194")
# print cheapest_gas_stations(all_gas_stations)

	# for test_station in stations_list:
	# 	print "lat:"
	# 	print test_station['lat']
	# 	print "long:"
	# 	print test_station['lng']
	# 	print "regular price:"
	# 	print test_station['reg_price']

# 	for key in stations_list:
# 		station.get(key)
# 		# print key
# 		return stations_list


# cheapest_gas_stations()



# # do i need to covert this into a string?

# def get_gas_info():

#     gas_info =
# {
#     "status": {
#         "error": "NO",
#         "code": 200,
#         "description": "none",
#         "message": "Request ok"
#     },
#     "geoLocation": {
#         "city_id": "147",
#         "city_long": "Saint-Laurent",
#         "region_short": "QC",
#         "region_long": "Quebec",
#         "country_long": "Canada",
#         "country_id": "43",
#         "region_id": "35"
#     },
#     "stations": [
#         {
#             "country": "Canada",
#             "reg_price": "3.65",
#             "mid_price": "3.65",
#             "pre_price": "3.65",
#             "diesel_price": "3.65",
#             "address": "3885, Boulevard Saint-Rose",
#             "diesel": "0",
#             "id": "33862",
#             "lat": "45.492367",
#             "lng": "-73.710915",
#             "station": "Shell",
#             "region": "Quebec",
#             "city": "Saint-Laurent",
#             "reg_date": "3 hours agp",
#             "mid_date": "3 hours agp",
#             "pre_date": "3 hours agp",
#             "diesel_date": "3 hours agp",
#             "distance": "1.9km"
#         }
#     ]
# }
    
