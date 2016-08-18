// displaying the gas stations along the route
function fetchAndDisplayGasStations(directions, map) {
  var locations = pickLocationsToSearchForGas(directions);
  // this url is talking to my server.py. for each location in locations give me the lat. and lng.
  // locations is set equal to pickLocationsToSearchForGas funct.(below)coming from google api.
  locations.forEach(function(location) {
    var url = '/getgasstations.json?lat=' + location.lat + '&lng=' + location.lng;

    




    // I THINK THIS PART IS INCOMPLETE!!!!it is incomplete add the successhandler function
    // and loop over the dictionary and get the add a marker for every lat.,lng of the dict.
    // result.
    $.get(url, function(result){

      console.log(result);


      
    });

  });




  //     .load(function(cheapestStations) {
  //     console.log("something is printing from my gasfeed js");
  //     console.log(cheapestStations);
  //   });




  // });
}

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

  // [{lat:..., lng:...}, {}, {}, {}, ...]
  return locations;
}
