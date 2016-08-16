app.jinja_env.auto_reload = True



function loadDirectionsWithGasStations() {
  //constructing a new object (new google.maps)
  var directionsService = new google.maps.DirectionsService;
  var directionsDisplay = new google.maps.DirectionsRenderer;

  var map = initMap();

  directionsDisplay.setMap(map);

  var start = document.getElementById('start').value;
  var end   = document.getElementById('end').value;

  calculateRoute(start, end, directionsService, directionsDisplay, map);
}


// Initializes the Google Maps object with some settings and our defined lat/lng
// Returns the instance of the Google Maps object
function initMap() {
        
  var startLocation = {lat: 37.788668, lng: -122.411499}; // map is centered at Hackbright

  var htmlMap = document.getElementById('map');

  //constructing a new object and grabbing the id from html(the DOM)
  var map = new google.maps.Map(htmlMap, {
    zoom: 7,
    center: startLocation,
    scrollwheel: false,
    zoomControl: true,
    panControl: false,
    streetViewControl: false,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  });

  return map;
}



function calculateRoute(start, end, directionsService, directionsDisplay, map) {
  directionsService.route({
    origin: start,
    destination: end,
    travelMode: 'DRIVING'
  }, function(directions, status) {
    if (status === 'OK') {
      fetchAndDisplayGasStations(directions, map);
      directionsDisplay.setDirections(directions);
    } else {
      window.alert('Directions request failed due to ' + status);
    }
  });
}


function fetchAndDisplayGasStations(directions, map) {
  var steps = directions.routes[0].legs[0].steps;

  // pick which locations to look for gas stations
  longSteps = _.filter(steps, function(step) {
    return step.distance.value >= 30000;
  });

  // for each location, 
  // find cheapest gas stations, 
  // and put markers for them on the map
  longSteps.forEach(function(step) {
    console.log(step.distance.value);
    console.log(  step.start_location.lat() + ", " + step.start_location.lng()  );

    // location to search
    var searchLocation = {
      lat: step.start_location.lat(),
      lng: step.start_location.lng()
    };

    findAndDisplayLocalGasStations(searchLocation, map);
  });
}

function findAndDisplayLocalGasStations(searchLocation, map) {
  var lat = searchLocation.lat;
  var lng = searchLocation.lng;

  // STEP ONE: make call to mygasfeed to get stations
  var url = "http://api.mygasfeed.com/stations/radius/"+lat+"/"+lng+"/10/reg/price/c2pmuvu4mv.json";
  
  // hit the gas station api
  $.get(url, function(results) {
    // find the cheapest gas station

    // This is a list of station dictionary objects
    var stations = results.stations;

    // STEP TWO: given results (the json results from the API), you want to get the
    // 10 cheapest stations
    var cheapestStations = []; // <-- fill this up with dictionaries
    
    // @TODO -- what you are going to replace is here
    cheapestStations = stations.slice(0, 1); //- give me first five items
    console.log('cheapestStations:');
    console.log(cheapestStations);
    // @TODO


    // STEP THREE: Get the lat and lng of each cheap station and pass to the Google API
    // the code below loops through cheapestStations, looking at each currentStation
    // currentStation is a dictionary containing *all* the info for ONE station
    cheapestStations.forEach(function(currentStation) {

      // STEP FOUR: render the gas station on the map by retrieving its lat/lng from
      // the currentStation dictionary
      displayGasStation({
        lat: parseFloat(currentStation["lat"]),
        lng: parseFloat(currentStation["lng"])
      }, map);

    });

  });
}

// function that displays the gas station on the map
function displayGasStation(latLng, map) {
  new google.maps.Marker({
    position: latLng,
    title: 'gas',
    animation: google.maps.Animation.DROP,
    map: map,
  });
}