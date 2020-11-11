console.log("entered script");

var hostUrl = "http://student04.cse.nd.edu";
var portNumber = 51047;
var requestType = "GET";

// Table 1: Test ('/tests/:ethnicity')
var testTableButton = document.getElementById('test-table-button');
testTableButton.onmouseup = function(){
    console.log('TABLE 1: button clicked');
    var endpoint = '/tests/' + document.getElementById('ethnicity-options').value;
    getInfo(endpoint, 1);
};

// Table 2: Ethnicity ('/ethnicities/:test')
var ethnicityTableButton = document.getElementById('ethnicity-table-button');
ethnicityTableButton.onmouseup = function(){
    console.log('TABLE 2: button clicked');
    var endpoint = '/ethnicities/' + document.getElementById('test-options').value;
    getInfo(endpoint, 2);
};

// Table 3: Tests
getInfo('/tests/', 3);

// Table 4: Ethnicities
getInfo('/ethnicities/', 4);

function getInfo(endpoint, tableNum) {
    console.log('getting info for endpoint: ' + endpoint);
    makeNetworkCalltoServer(hostUrl, portNumber, requestType, endpoint, tableNum);
}

function makeNetworkCalltoServer(hostUrl, portNumber, requestType, endpoint, tableNum) {
    console.log("made network call to server");
    handleRequest(hostUrl, portNumber, requestType, endpoint, tableNum);
}

function handleRequest(hostUrl, portNumber, requestType, endpoint, tableNum) {
    console.log("handling request");

    var xhr = new XMLHttpRequest();
    console.log("created XMLHttpRequest");
    
    xhr.open(requestType, hostUrl + ":" + portNumber + endpoint, true);
    console.log("opened xhr");

    xhr.onload = function(e){
        console.log("entered onload");
        console.log(xhr.responseText);
        if(requestType == 'GET'){
            console.log("update page for get");

            if (tableNum == 1){
                updateTable1(xhr.responseText);
            } else if (tableNum == 2){
                updateTable2(xhr.responseText);
            } else if (tableNum == 3){
                updateTable3(xhr.responseText);
            } else if (tableNum == 4){
                updateTable4(xhr.responseText);
            }
            
        }
    }

    xhr.onerror = function(e){
        console.log("enter onerror");
        document.getElementById('physical-passed').innerHTML = "An error occurred - revise your request.";
        console.error(xhr.statusText);
    }

    xhr.send(null);

}

function updateTable1(response_text){
    console.log('updating page for get');

    var response_json = JSON.parse(response_text);
    console.log('response: ' + response_json);

    document.getElementById('physical-passed').innerHTML = response_json['Passed_Physical_Test'];
    document.getElementById('written-passed').innerHTML = response_json['Passed_Written_Test'];
    document.getElementById('personal-passed').innerHTML = response_json['Passed_Personal'];
    document.getElementById('interview-passed').innerHTML = response_json['Passed_Interview'];
    document.getElementById('polygraph-passed').innerHTML = response_json['Passed_Polygraph__Medical__Psyc'];
}

function updateTable2(response_text){
    console.log('updating page for get');

    var response_json = JSON.parse(response_text);
    console.log('response: ' + response_json);

    document.getElementById('ai-passed').innerHTML = response_json['American-Indian'];
    document.getElementById('a-passed').innerHTML = response_json['Asian'];
    document.getElementById('b-passed').innerHTML = response_json['Black'];
    document.getElementById('hl-passed').innerHTML = response_json['Latino'];
    document.getElementById('nh-passed').innerHTML = response_json['Hawaiian'];
    document.getElementById('two-passed').innerHTML = response_json['Multiple'];
    document.getElementById('w-passed').innerHTML = response_json['White'];
}

function updateTable3(response_text){
    console.log('updating page for get');

    var response_json = JSON.parse(response_text);
    console.log('response: ' + response_json);

    document.getElementById('p-physical').innerHTML = response_json['Passed_Physical_Test'];
    document.getElementById('p-written').innerHTML = response_json['Passed_Written_Test'];
    document.getElementById('p-personal').innerHTML = response_json['Passed_Personal'];
    document.getElementById('p-interview').innerHTML = response_json['Passed_Interview'];
    document.getElementById('p-polygraph').innerHTML = response_json['Passed_Polygraph__Medical__Psyc'];
}

function updateTable4(response_text){
    console.log('updating page for get');

    var response_json = JSON.parse(response_text);
    console.log('response: ' + response_json);

    document.getElementById('ai-total-applicants').innerHTML = response_json['American-Indian'];
    document.getElementById('a-total-applicants').innerHTML = response_json['Asian'];
    document.getElementById('b-total-applicants').innerHTML = response_json['Black'];
    document.getElementById('hl-total-applicants').innerHTML = response_json['Latino'];
    document.getElementById('nh-total-applicants').innerHTML = response_json['Hawaiian'];
    document.getElementById('two-total-applicants').innerHTML = response_json['Multiple'];
    document.getElementById('w-total-applicants').innerHTML = response_json['White'];
}