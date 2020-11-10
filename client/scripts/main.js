console.log("entered script");

var hostUrl = "http://student13.cse.nd.edu";
var portNumber = 8080;
var requestType = 'GET';
var ethnicity = "White"; //document.getElementById('ethnicity-options').value;
makeNetworkCalltoServer(hostUrl, portNumber, requestType, ethnicity);

function makeNetworkCalltoServer(hostUrl, portNumber, requestType, ethnicity) {
    console.log("make network call to server");
    handleRequest(hostUrl, portNumber, requestType, ethnicity);
}

function handleRequest(hostUrl, portNumber, requestType, ethnicity) {
    console.log("handling request");

    var xhr = new XMLHttpRequest();
    
    xhr.open(requestType, hostUrl + ":" + portNumber + "/tests/" + ethnicity, true);

    xhr.onload = function(e){
        console.log(xhr.responseText);
        if(requestType == 'GET'){
            console.log("update page for get")
            updatePageForGet(xhr.responseText);
        }
    }
}

function updatePageForGet(response_text){
    console.log('updating page for get');

    var response_json = JSON.parse(response_text);
    console.log(response_json);

    document.getElementById('physical-passed').innerHTML = "Result: " + response_json['result'] + "\n Ethnicity: " + response_json['ethnicity'] + "\n Test: " + response_json['test'];
}

