import json
# I don't think I need this:
import urllib2
import requests

url = 'api.mygasfeed.com'
api_key = "c2pmuvu4mv"


# Tested query : http://api.mygasfeed.com/stations/radius/37.7749/-122.4194/2/reg/distance/c2pmuvu4mv.json

# gas_station_info = json.load
r = requests.get("http://api.mygasfeed.com/stations/radius/37.7749/-122.4194/10/reg/price/c2pmuvu4mv.json")
results = r.json()
# return the results as a list
stations = results['stations']

# create an empty list:
prices_list = []
# iterate over every station in the whole list of stations:
for station in stations:
	# add the price and and index of every station in stations list to the
		# price_list.
    prices_list.append( (station['reg_price'],stations.index(station)) )

# to print result as dictionary:
	# prices_list.append( {stations.index(station): station['reg_price']} )

# sorts through the list by having the price first then the index.
prices_list.sort()

# passes the value of the last 10 cheapest gas stations to the variable.
cheapest_10_stations = prices_list[:10]

# this returns a tuple of price and index:
# print cheapest_10_stations

####### NEXT STEPS ##############
# Iterate over the cheapest_10_stations
# for each station tuple
	# we need to get index of that station from the tuple : tuple[1]
	# use the index to get the full station information from stations list
	# then you get a dictionary that represent info about that station
	# get data from that dictionary as needed



# for price in cheapest_10_stations:
	# print price[0]

for station in stations:
	print (station['address'], station.index(station))








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
    
# Gas Prices History (NEW!!!)
# Retrieves a list of gas price histroy for a particular gas station. 

# Request Url example: /locations/pricehistory/(station id)/apikey.json?callback=?

# Method: GET 

# Arguments:
# station id - The id of the gas station. 
# Api Key 
# Callback - Only needed for JSONP requests 

# Example of JSON Response:
# {
#     "status": {
#         "error": "NO",
#         "code": 200,
#         "description": "none",
#         "message": "Request ok"
#     },
#     "histroy": [
#         {
#             "type": "Pre",
#             "price": "3.33",
#             "date": "1 day ago",
#             "via": "myGasFeed Dev"
#         },
#         {
#             "type": "Regular",
#             "price": "6.66",
#             "date": "1 day ago",
#             "via": "myGasFeed Dev"
#         },
#         {
#             "type": "Regular",
#             "price": "3.33",
#             "date": "1 day ago",
#             "via": "myGasFeed Dev"
#         },...
#     ]
# }
    
# Gas Station Details
# Retrieves gas station details by providing the station id. The station id can be retrieved when making a request for a list of stations. 

# Request Url example: /stations/details/(Stattion Id)/apikey.json?callback=?

# Method: GET 

# Arguments:
# Station id - The number id of station
# Api Key
# Callback - Only needed for JSONP requests 

# Example of JSON Response:
# {
#     "status": {
#         "error": "NO",
#         "code": 200,
#         "description": "none",
#         "message": "Request ok"
#     },
#     "details": {
#         "address": "3885, Boulevard de la Cavendish",
#         "id": "33862",
#         "city": "Saint-Laurent",
#         "region": "Quebec",
#         "country": "Canada",
#         "lat": "45.492367",
#         "lng": "-73.710915",
#         "station_name": "Shell",
#         "reg_price": "3.45",
#         "reg_date": "6 min ago",
#         "mid_price": "3.69",
#         "mid_date": "4 hours ago",
#         "pre_price": "3.89",
#         "pre_date": "5 mins ago",
#         "diesel_date": "4.09",
#         "diesel": "0" //0 contains no diesel pump, 1 contains a diesel pump
#     },
#     "previousPrices": [
#         {
#             "type": "Pre",
#             "price": "3.74",
#             "date": "11 hours ago",
#             "via": "myGasFeed"
#         },
#         {
#             "type": "Regular",
#             "price": "3.67",
#             "date": "11 hours ago",
#             "via": "myGasFeed"
#         }
#     ]
# }
        
# Gas Station Brands
# Retrieves a list of all gas station brands. 

# Request Url example: /stations/brands/apikey.json?callback=?

# Method: GET 

# Arguments:
# Api key
# Callback - Only needed for JSONP requests 

# Example of JSON Response:
# {
#     "status": {
#         "error": "NO",
#         "code": 200,
#         "description": "none",
#         "message": "Request ok"
#     },
#     "stations": [
#         {
#             "name": "7-Eleven",
#             "id": "42"
#         }...(more)
#     ]
# }
        
# Updating Gas Prices
# Updating gas prices for a particular gas station. All fields must be supplied with the exact name as described below. You will not be able to use JSONP or a straight POST from javascript ajax. Must be done all on the server side using cURL for PHP developers. 

# Request Url example: /locations/price/apikey.json

# Method: POST 

# Note: Once price is updated successfully you will receive json data response with the station details.

# Form Field Names:
# price - Actual gas price. Format (3.64)
# fueltype - Type of fuel. Arguments to be passed: reg,mid,pre,diesel
# stationid - The current location id of the station that will be updated. Add the integer to a hidden field. 

# Example of JSON Response:
# {
#     "status": {
#         "error": "NO",
#         "code": 200,
#         "description": "none",
#         "message": "Request ok"
#     },
#     "details": {
#         "country": "Canada",
#         "city": "Saint-Laurent",
#         "region": "Quebec",
#         "reg_price": "1.18 \u00a2\/Litre",
#         "mid_price": "N\/A",
#         "pre_price": "1.26 \u00a2\/Litre",
#         "diesel_price": "N\/A",
#         "address": "8300-8500, Rte Transcanadienne",
#         "diesel": "0",
#         "id": "33863",
#         "lat": "45.488991",
#         "lng": "-73.725204",
#         "station": "Ultramar",
#         "reg_date": "0 seconds ago",
#         "mid_date": "N\/A",
#         "pre_date": "23 hours ago",
#         "diesel_date": "N\/A"
#     },
#     "previousPrices": [
#         {
#             "type": "Regular",
#             "price": "1.18 \u00a2\/Litre",
#             "date": "0 seconds ago",
#             "via": "myGasFeed"
#         },...

#     ]
# }
        
# Address Location By Lat & Lng
# Providing the latitude & longitude of the current location, you will retrieve the full address. An example how to use this request when adding a gas station by picking up the address information at a specific gas station without having the user to enter the info. 

# Request Url example: /locations/geoaddress/(Latitude)/(Longitude)/apikey.json

# Method: GET 

# Arguments:
# Latitude
# Longitude 
# API Key. 

# Example of JSON Response:
# {
#     "status": {
#         "error": "NO",
#         "code": 200,
#         "description": "none",
#         "message": "Request ok"
#     },
#     "location": {
#         "country_short": "CA",
#         "lat": "45.5092499",
#         "lng": "-73.7167247",
#         "country_long": "Canada",
#         "region_short": "QC",
#         "region_long": "Quebec",
#         "city_long": "Saint-Laurent",
#         "city_short": "Saint-Laurent",
#         "address": "14073, Boulevard Cavendish",
#         "result": "OK"
#     }
# }
        
# Close By Gas Stations (New!!!)
# Retrieve a list of other gas stations that are close by to a particular station by just suppling the station id. 

# Request Url example: /locations/otherclosebystations/(Station Id)/(Limit)/apikey.json

# Method: GET 

# Station Id - The id of the gas station. 
# Limit - Number of gas stations needed to be returned.
# Api Key 
# Callback - Only needed for JSONP requests 

# Example of JSON Response:
# {
#     "status": {
#         "error": "NO",
#         "code": 200,
#         "description": "none",
#         "message": "Request ok"
#     },
#     "stations": [
#         {
#             "country": "United States",
#             "reg_price": "3.49",
#             "address": "330 N Federal Hwy",
#             "id": "36076",
#             "station": "Mobil",
#             "region": "Florida",
#             "city": "fort lauderdale",
#             "reg_date": "2 weeks ago",
#             "distance": "0.3 miles"
#         },
#         {
#             "country": "United States",
#             "reg_price": "3.57",
#             "address": "1420 E Sunrise Blvd",
#             "id": "36080",
#             "station": "Sunoco",
#             "region": "Florida",
#             "city": "fort lauderdale",
#             "reg_date": "2 weeks ago",
#             "distance": "0.7 miles"
#         },
#         {
#             "country": "United States",
#             "reg_price": "3.45",
#             "address": "460 W Broward Blvd",
#             "id": "36111",
#             "station": "Shell",
#             "region": "Florida",
#             "city": "fort lauderdale",
#             "reg_date": "2 weeks ago",
#             "distance": "0.9 miles"
#         }
#     ]
# }
        
