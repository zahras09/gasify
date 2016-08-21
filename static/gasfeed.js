



// displaying the gas stations along the route
function fetchAndDisplayGasStations(directions, map) {
  var locations = pickLocationsToSearchForGas(directions);
  // this url is talking to my server.py. for each location in locations give me the lat. and lng.
  // locations is set equal to pickLocationsToSearchForGas funct.(below)coming from google api.
  locations.forEach(function(location) {
    var url = '/getgasstations.json?lat=' + location.lat + '&lng=' + location.lng;

    
    
    // result is the result from 
    $.get(url, fetchAndDisplayGasStations);


    console.log(fetchAndDisplayGasStations);{
      var marker = {lat: parseFloat(fetchAndDisplayGasStations['lat']) ,lng: parseFloat(fetchAndDisplayGasStations['lng']) };
      displayGasStation(marker, map);
    }
      // result is a dict. returning the cheapest station (every 30,000m) along the path with all
      // of the information assiciated with that specific staion but I want to only grab the lat.lng 
      // which are keys inside the result dictionary:
      // var lat = result['lat'];
      // var lng = result['lng'];

  });
}
// THIS FUNCTION IS TAKING THE LAT,LNG OF EVERY 30,000 LOCATION(A DICT) METERS 
// AND ADDING IT TO THE LIST LOCATIONS:

function pickLocationsToSearchForGas(directions) {
  // this is from google api
  var steps = directions.routes[0].legs[0].steps;

  // keep only the steps that are longer than 30,000 meters
  var longSteps = _.filter(steps, function(step) {
    return step.distance.value >= 30000;
  });
  
  var locations = [];
  // convert all the long steps into lat and lng
  longSteps.forEach(function(step) {

    // step is the dictionary name, start_location is key,inside the key you
    // have another dict. with key 'lat' that has a value that is a function
    var lat = step.start_location.lat();
    var lng = step.start_location.lng();

    var location = {
      lat: lat,
      lng: lng
    };

    locations.push(location);
  });
  return locations;
}
