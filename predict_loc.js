var loc = document.getElementById("loc");
var predictHQUrl=https://api.predicthq.com;


var client_id = 'phq.pBkARGtqZsf0wljA7nfkqvw2PuTTpxYRvgg9Vq4e';
var client_secret = 'yzkIsZHtUfGubzFppws22P0FxGG2mQhmhFiKZD0C';
var api_token;

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(getAllDisasterDetails);
    } else {
        loc.innerHTML = "Geolocation is not supported by this browser.";
    }
}

function getAllDisasterDetails(position){
	
	
if(api_token == ''){
api_token = oauth2Login();
}
if(api_token == ''){
	return;
}

$.ajax({
	url: predictHQUrl + '/v1/events/?within=10km@'+position.coords.latitude+','
	+ position.coords.longitude + '&country=US' + '&q=disasters',
    headers: {
        'Authorization':'Bearer ' + api_token,
    },
    method: 'GET',
    dataType: 'json',
	async:false,
    success: function(data){
      console.log('succes: '+data);
    }
	
	
});

}

function oauth2Login(){
	$.ajax({
	url: predictHQUrl + '/oauth2/',
    headers: {
        'Authorization':'Basic ' + $.base64.encode(client_id + ':' + client_secret),
    },
    method: 'GET',
    dataType: 'json',
	async: false,
    success: function(data){
      return data.get('access_token');
    }
	
	
	
});
	return '';
	
	
}