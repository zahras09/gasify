function initMap() {
        
  var startLocation = {lat: 37.788668, lng: -122.411499}; // map is centered at Hackbright
  //constructing a new object (new google.maps)
  var directionsService = new google.maps.DirectionsService;
  var directionsDisplay = new google.maps.DirectionsRenderer;
  //constructing a new object and grabbing the id from html(the DOM)
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 7,
    center: startLocation,
    scrollwheel: false,
    zoomControl: true,
    panControl: false,
    streetViewControl: false,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  });

  directionsDisplay.setMap(map);

  var onChangeHandler = function() {
    calculateAndDisplayRoute(directionsService, directionsDisplay);
  };
  document.getElementById('start').addEventListener('change', onChangeHandler);
  document.getElementById('end').addEventListener('change', onChangeHandler);

  calculateAndDisplayRoute(directionsService, directionsDisplay, map);
}

function print_steps(response, map) {
  steps = response.routes[0].legs[0].steps;

  longSteps = _.filter(steps, function(step) {
    return step.distance.value >= 30000;
  });


  var markers = [];
  longSteps.forEach(function(step) {
    console.log(step.distance.value);
    console.log(  step.start_location.lat() + ", " + step.start_location.lng()  );

    var myLatLng = {
      lat: step.start_location.lat(),
      lng: step.start_location.lng()
    };

    var marker = {
      position: myLatLng,
      title: 'gas',
      animation: google.maps.Animation.DROP,
      map: map,
    };

    markers.push(marker);
  });

  console.log(markers);

  for (var i=0; i<markers.length; i++) {

    var marker = markers[i];
    
    var func = function(marker) {
      setTimeout(function() {
        new google.maps.Marker(marker);
      }, i * 200);
    }

    func(marker);
  }
}

function calculateAndDisplayRoute(directionsService, directionsDisplay, map) {
  directionsService.route({
    origin: document.getElementById('start').value,
    destination: document.getElementById('end').value,
    travelMode: 'DRIVING'
  }, function(response, status) {
    print_steps(response, map);
    if (status === 'OK') {
      directionsDisplay.setDirections(response);
    } else {
      window.alert('Directions request failed due to ' + status);
    }
  });
}

