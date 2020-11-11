console.log("entered script");

var hostUrl = "http://student04.cse.nd.edu";
var portNumber = 51047;
var requestType = "GET";
var ethnicity = document.getElementById('ethnicity-options').value;
var testTableButton = document.getElementById('test-table-button');
testTableButton.onmouseup = getFormInfo;
var ethnicityTableButton = document.getElementById('ethnicity-table-button');
ethnicityTableButton.onmouseup = getFormInfo;

function getFormInfo() {
    makeNetworkCalltoServer(hostUrl, portNumber, requestType, ethnicity);
}

function makeNetworkCalltoServer(hostUrl, portNumber, requestType, ethnicity) {
    console.log("make network call to server");
    handleRequest(hostUrl, portNumber, requestType, ethnicity);
}

function handleRequest(hostUrl, portNumber, requestType, ethnicity) {
    console.log("handling request");

    var xhr = new XMLHttpRequest();
    console.log("created XMLHttpRequest");
    
    xhr.open(requestType, hostUrl + ":" + portNumber + "/tests/" + ethnicity, true);
    console.log("opened xhr");

    xhr.onload = function(e){
        console.log("entered onload");
        console.log(xhr.responseText);
        if(requestType == 'GET'){
            console.log("update page for get")
            updatePageForGet(xhr.responseText);
        }
    }

    xhr.onerror = function(e){
        console.log("enter onerror");
        document.getElementById('physical-passed').innerHTML = "An error occurred - revise your request.";
        console.error(xhr.statusText);
    }

    xhr.send(null);

}

function updatePageForGet(response_text){
    console.log('updating page for get');

    var response_json = JSON.parse(response_text);
    console.log(response_json);

    document.getElementById('physical-passed').innerHTML = response_json['Passed_Physical_Test'];
}

