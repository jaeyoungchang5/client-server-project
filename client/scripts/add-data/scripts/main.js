console.log("Page loaded");

var hostUrl = "http://student04.cse.nd.edu";
var portNumber = 51047;
var requestType = "PUT";

var submitButton = document.getElementById('add-data-button')
submitButton.onmouseup = getFormInfo;

function getFormInfo(){
    console.log("get form info");
    var ethnicity;
    var json_data = {}

    // get ethnicity
    if (document.getElementById('american-indian').checked){
        ethnicity = document.getElementById("american-indian").value;
    } else if (document.getElementById('asian').checked){
        ethnicity = document.getElementById("asian").value;
    } else if (document.getElementById('black').checked){
        ethnicity = document.getElementById("black").value;
    } else if (document.getElementById('hispanic-latino').checked){
        ethnicity = document.getElementById("hispanic-latino").value;
    } else if (document.getElementById('native-hawaiian').checked){
        ethnicity = document.getElementById("native-hawaiian").value;
    } else if (document.getElementById('white').checked){
        ethnicity = document.getElementById("white").value;
    } else if (document.getElementById('other').checked){
        ethnicity = document.getElementById("other").value;
    }

    // get whether or not user submitted application
    var hired;
    if (document.getElementById('yes').checked){
        hired = document.getElementById("yes").value;
        json_data['Passed_Polygraph__Medical__Psyc'] = true;
    } else if (document.getElementById('no').checked){
        hired = document.getElementById("no").value;
    }

    // get tests taken
    var taken = [];
    if (document.getElementById('physical-take').checked){
        taken.push("Physical");
        json_data[document.getElementById("physical-take").value] = true;
    }

    if (document.getElementById('written-take').checked){
        taken.push("Written");
        json_data[document.getElementById("written-take").value] = true;
    }

    if (document.getElementById('personal-take').checked){
        taken.push("Personal");
        json_data[document.getElementById("personal-take").value] = true;
    }

    if (document.getElementById('interview-take').checked){
        taken.push("Interview");
        json_data[document.getElementById("interview-take").value] = true;
    }

    console.log("Tests taken: " + taken);

    // get tests passed
    var passed = [];
    if (document.getElementById('physical-pass').checked){
        passed.push("Physical");
        json_data[document.getElementById("physical-pass").value] = true;
    }

    if (document.getElementById('written-pass').checked){
        passed.push("Written");
        json_data[document.getElementById("written-pass").value] = true;
    }

    if (document.getElementById('personal-pass').checked){
        passed.push("Personal");
        json_data[document.getElementById("personal-pass").value] = true;
    }

    if (document.getElementById('interview-pass').checked){
        passed.push("Interview");
        json_data[document.getElementById("interview-pass").value] = true;
    }

    console.log("Tests passed: " + passed);

    // make dictionary
    data = {};
    data['ethnicity'] = ethnicity;
    data['hired'] = hired;
    data['taken'] = taken;
    data['passed'] = passed;

    displayData(data);
    makeNetworkCalltoServer(hostUrl, portNumber, requestType, '/results/' + ethnicity, json_data);
}

function displayData(data){
    console.log('entered data!');

    // get fields from story and display in label.
    var page_top = document.getElementById('data-to-be-added');
    page_top.innerHTML = 'Data Added';
    
    var the_data = "";

    the_data += "Ethnicity: <br>" + data['ethnicity'] + "<br>";

    the_data += "<br>Hired: <br>" + data['hired'];
    
    the_data += "<br><br>Tests Taken: <br>";

    for (test in data['taken']) {
        the_data += data['taken'][test] + ", ";
    }

    the_data += "<br><br>Tests Passed: <br>";

    for (test in data['passed']) {
        the_data += data['passed'][test] + ", ";
    }

    var story_body = document.getElementById('story-body');
    story_body.innerHTML = the_data;
}

function makeNetworkCalltoServer(hostUrl, portNumber, requestType, endpoint, json_data) {
    console.log("made network call to server");
    handleRequest(hostUrl, portNumber, requestType, endpoint, json_data);
}

function handleRequest(hostUrl, portNumber, requestType, endpoint, json_data){
    console.log("handling request");
    console.log(json_data)

    var xhr = new XMLHttpRequest();
    console.log("created XMLHttpRequest");
    
    xhr.open(requestType, hostUrl + ":" + portNumber + endpoint, true);
    console.log("opened xhr");

    xhr.onload = function(e){
        console.log("entered onload");
        console.log(xhr.responseText);
        if(requestType == 'PUT'){
            console.log("put request -- here");
            
        }
    }

    xhr.onerror = function(e){
        console.log("enter onerror");
        console.error(xhr.statusText);
    }

    xhr.send(JSON.stringify(json_data));
}
