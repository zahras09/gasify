
// use the id's from maps display to access the start and end values.
// use the ajax to call the python route

$('#map').onload(getGasstations);

function getGasstations(){
	var start = $('#start').val();
	var end = $('#end').val();
	var data = {
		'start': start,
		'end': end
	};
	$.get('/getgasstations', data, addMarkers);
// python route return json to this function
}

// console.log the information
// parse the json and 
		