
// displaying the gas stations along the route
function fetchAndDisplayGasStations(directions, map) {
  var locations = pickLocationsToSearchForGas(directions);
  // added the infowindow variable(gets called in bindInfoWindow funct.)
  var infoWindow = new google.maps.InfoWindow({
      width: 150
  });
  // this url is talking to my server.py. for each location in locations give me the lat. and lng.
  // locations is set equal to pickLocationsToSearchForGas funct.(below)coming from google api.
  locations.forEach(function(location) {
    var url = '/getgasstations.json?lat=' + location.lat + '&lng=' + location.lng;

    // ask the server for the cheapest station,
    // the server returns that cheapest station into the anonymous function below
    $.get(url, function(cheapest_station_json) {
      // station_json is the json returned from python that represents a gas station
      var cheapest_station = JSON.parse(cheapest_station_json);


      // call displayGasStation with the station AND the map!!!
      displayGasStation(cheapest_station, map, infoWindow);
    });
  });
}




function displayGasStation(station, map, infoWindow) {
  // variable for the content of the Info.

  
  var latlng = {
    lat: parseFloat(station['lat']),
    lng: parseFloat(station['lng'])
  };
  
  var marker =  new google.maps.Marker({
    position: latlng,
    title: 'gas',
    animation: google.maps.Animation.DROP,
    map: map
  });
  html = ('Station: ' + station['station'] + ' Price: ' + station['reg_price']);

          // Inside the loop we call bindInfoWindow passing it the marker,
          // map, infoWindow and contentString
  bindInfoWindow(marker, map, infoWindow, html);
      
}


  function bindInfoWindow(marker, map, infoWindow, html) {

      google.maps.event.addListener(marker, 'click', function () {
          infoWindow.close();
          infoWindow.setContent(html);
          infoWindow.open(map, marker);
      });
  }

// THIS FUNCTION IS TAKING THE LAT,LNG OF EVERY 30,000 LOCATION(A DICT) METERS 
// AND ADDING IT TO THE LIST LOCATIONS:
function pickLocationsToSearchForGas(directions) {
  var locations = [];

  // TODO: directions.routes[0].overview_path
  // which is a large array of lots of lat/lng points
  // Use it to pick locations!  
  // - Maybe choose every 10th point? Maybe every 20th?
  // - Try things, see what looks nice!
  // *** remember, the lat and lng keys are functions
  // *** just like they are below!
  // - below is an example of using EVERY lat/lng from overview_path

  // directions.routes[0].overview_path.forEach(function(location) {
  //   var lat = location.lat();
  //   var lng = location.lng();

  //   var latlng = {
  //     lat: lat,
  //     lng: lng
  //   };

  //   location.push(latlng);
  // });

  // // this is from google api
  // var steps = directions.routes[0].legs[0].steps;

  // // keep only the steps that are longer than 30,000 meters
  // var longSteps = _.filter(steps, function(step) {
  //   return step.distance.value >= 30000;
  // });
  
  // // convert all the long steps into lat and lng
  // longSteps.forEach(function(step) {

  //   // step is the dictionary name, start_location is key,inside the key you
  //   // have another dict. with key 'lat' that has a value that is a function
  //   var lat = step.start_location.lat();
  //   var lng = step.start_location.lng();

  //   var location = {
  //     lat: lat,
  //     lng: lng
  //   };

  //   locations.push(location);
  // });

  // return locations;
  var numSteps = directions.routes[0].overview_path.length;
  // Math.floor returns a whole number vs. a float.
  var interval = Math.floor(numSteps / 10);
  // set a forloop and iterate over intervals
  for (var i = 0; i < numSteps; i = i + interval) {
    console.log(i);
    var location = {
      lat: directions.routes[0].overview_path[i].lat(),
      lng: directions.routes[0].overview_path[i].lng()
    };
    // add location to list of locations
    locations.push(location);
    
    console.log(location);

  } //end for
  return locations;


}