console.log("entered script");

var hostUrl = "http://student13.cse.nd.edu";
var portNumber = 8080;
var 
makeNetworkCalltoServer(hostUrl, portNumber, requestType, ethnicity);

function makeNetworkCalltoServer(hostUrl, portNumber, requestType, ethnicity) {
    console.log("make network call to server");
    handleRequest(hostUrl, portNumber, requestType, ethnicity);
}

function handleRequest(hostUrl, portNumber, requestType, ethnicity) {
    console.log("handling request");

    var xhr = new XMLHttpRequest();
    
    xhr.open(requestType, hostUrl + ":" + portNumber + "/tests/:" + ethnicity, true);

    xhr.onload = function(e){
        console.log(xhr.responseText);
        if(requestType == 'GET'){
            console.log("update page for get")
            updatePageForGet(xhr.responseText);
        }
    }

    xhr.onerror = function(e){
        document.getElementById('answer-label').innerHTML = "An error occurred - revise your request.";
        console.error(xhr.statusText);
    }
}

function updatePageForGet(response_text){
    console.log('updating page for get');

    var response_json = JSON.parse(response_text);
    console.log(response_json);

    document.getElementById('physical-').innerHTML = "Result: " + response_json['result'] + "\n Title: " + response_json['title'] + "\n Genres: " + response_json['genres'];
}

