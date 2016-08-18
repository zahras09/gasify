// app.jinja_env.auto_reload = True



function loadDirectionsWithGasStations() {
  //constructing a new object (new google.maps)
  var directionsService = new google.maps.DirectionsService;
  var directionsDisplay = new google.maps.DirectionsRenderer;

  var map = initMap();

  // makes the map appear
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
      directionsDisplay.setDirections(directions);
      fetchAndDisplayGasStations(directions, map);
    } else {
      window.alert('Directions request failed due to ' + status);
    }
  });
}



// function findAndDisplayLocalGasStations(searchLocation, map) {
//   var lat = searchLocation.lat;
//   var lng = searchLocation.lng;

//   // STEP ONE: make call to mygasfeed to get stations
//   var url = "http://api.mygasfeed.com/stations/radius/"+lat+"/"+lng+"/10/reg/price/c2pmuvu4mv.json";
  
//   // hit the gas station api
//   $.get(url, function(results) {
//     // find the cheapest gas station

//     // This is a list of station dictionary objects
//     var stations = results.stations;

//     // STEP TWO: given results (the json results from the API), you want to get the
//     // 10 cheapest stations
//     var cheapestStations = []; // <-- fill this up with dictionaries
    
//     // @TODO -- what you are going to replace is here
//     cheapestStations = stations.slice(0, 1); //- give me first five items
//     console.log('cheapestStations:');
//     console.log(cheapestStations);
//     // @TODO


//     // STEP THREE: Get the lat and lng of each cheap station and pass to the Google API
//     // the code below loops through cheapestStations, looking at each currentStation
//     // currentStation is a dictionary containing *all* the info for ONE station
//     cheapestStations.forEach(function(currentStation) {

//       // STEP FOUR: render the gas station on the map by retrieving its lat/lng from
//       // the currentStation dictionary
//       displayGasStation({
//         lat: parseFloat(currentStation["lat"]),
//         lng: parseFloat(currentStation["lng"])
//       }, map);

//     });

//   });
// }

// function addMarker() {
//   var myImageURL = 'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png';
//   var image = myImageURL;
//   var nearSydney = new google.maps.LatLng(-34.788666, 150.41146);
// }
 
// function that displays the gas station on the map\
var displayGasStation = function(latlng, map) {
  
  var marker = new google.maps.Marker({
          position: latlng,
          map: map,
          // title: 'Gas Station'
        });
 


  new google.maps.Marker({
    position: latLng,
    title: 'gas',
    animation: google.maps.Animation.DROP,
    map: map,
  });
};


var gasStation = new google.maps.latlng(37.7749, -122.4194);

displayGasStation(gasStation, map);


