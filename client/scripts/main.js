console.log("entered script");

var hostUrl = "http://student04.cse.nd.edu";
var portNumber = 51047;
var requestType = "GET";

// Table 1: Test ('/tests/:ethnicity')
var testTableButton = document.getElementById('test-table-button');
testTableButton.onmouseup = function(){
    console.log('TABLE 1: button clicked');
    var endpoint = '/tests/' + document.getElementById('ethnicity-options').value;
    getTestInfo(endpoint)
};

// Table 2: Ethnicity ('/ethnicities/:test')
var ethnicityTableButton = document.getElementById('ethnicity-table-button');
ethnicityTableButton.onmouseup = getFormInfo;

function getTestInfo(endpoint) {
    console.log('getting info for endpoint: ' + endpoint);
    makeNetworkCalltoServer(hostUrl, portNumber, requestType, endpoint);
}

function makeNetworkCalltoServer(hostUrl, portNumber, requestType, endpoint) {
    console.log("made network call to server");
    handleRequest(hostUrl, portNumber, requestType, endpoint);
}

function handleRequest(hostUrl, portNumber, requestType, endpoint) {
    console.log("handling request");

    var xhr = new XMLHttpRequest();
    console.log("created XMLHttpRequest");
    
    xhr.open(requestType, hostUrl + ":" + portNumber + endpoint, true);
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
    document.getElementById('written-passed').innerHTML = response_json['Passed_Written_Test'];
    document.getElementById('personal-passed').innerHTML = response_json['Passed_Personal'];
    document.getElementById('interview-passed').innerHTML = response_json['Passed_Interview'];
    document.getElementById('polygraph-passed').innerHTML = response_json['Passed_Polygraph__Medical__Psyc'];

    console.log(response_json['Passed_Written_Test']);
    console.log(response_json['Passed_Interview']);
}

