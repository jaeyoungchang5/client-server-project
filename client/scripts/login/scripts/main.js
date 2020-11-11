console.log("entered script");

var hostUrl = "http://student04.cse.nd.edu";
var portNumber = 51047;

var loginButton = document.getElementById("login-button");
loginButton.onmouseup = function(){
    getFormInfo("GET");
};

var signupButton = document.getElementById("signup-button");
signupButton.onmouseup = function(){
    getFormInfo("POST");
};

var deleteButton = document.getElementById("delete-button");
deleteButton.onmouseup = function(){
    getFormInfo("DELETE");
};

function getFormInfo(requestType) {
    console.log("get form info");
    var endpoint = "/user/";

    var data = {}
    if (requestType == "GET"){
        var username = document.getElementById("login-username").value;
        var password = document.getElementById("login-password").value;
        data = {'username': username, 'password': password};
        makeNetworkCalltoServer(hostUrl, portNumber, requestType, endpoint + 'all/', data);
    } else if (requestType == "POST"){
        var fname = document.getElementById("signup-fname").value;
        var lname = document.getElementById("signup-lname").value;
        var password = document.getElementById("signup-password").value;
        var email = document.getElementById("signup-email").value;
        var username = document.getElementById("signup-username").value;
        data = {'fname': fname, 'lname': lname, 'password': password, 'email': email}
        makeNetworkCalltoServer(hostUrl, portNumber, requestType, endpoint+username, data);
    } else if (requestType == "DELETE"){
        var username = document.getElementById("head-username").innerHTML;
        data = {}
        makeNetworkCalltoServer(hostUrl, portNumber, requestType, endpoint+username, data);
    }
}

function makeNetworkCalltoServer(hostUrl, portNumber, requestType, endpoint, data) {
    console.log("made network call to server");
    console.log("endpoint: " + endpoint);
    handleRequest(hostUrl, portNumber, requestType, endpoint, data);
}

function handleRequest(hostUrl, portNumber, requestType, endpoint, data) {
    console.log("handling request");

    var xhr = new XMLHttpRequest();
    console.log("created XMLHttpRequest");
    
    xhr.open(requestType, hostUrl + ":" + portNumber + endpoint, true);
    console.log("opened xhr");

    xhr.onload = function(e){
        console.log("entered onload");
        console.log(xhr.responseText);

        if (requestType == "GET"){
            updateGET(xhr.responseText, data);
        } else if (requestType == "POST"){
            updatePOST(xhr.responseText);
        }else if (requestType == "DELETE"){
            updateDELETE(xhr.responseText);
        }
    }

    xhr.onerror = function(e){
        console.log("enter onerror");
        console.error(xhr.statusText);
    }

    if (requestType == "GET"){
        xhr.send(null);
    } else if (requestType == "POST" || requestType == "DELETE"){
        xhr.send(JSON.stringify(data));
    }
}

function updateGET(response_text, data){
    var response_json = JSON.parse(response_text);

    if (response_json[data['username']]){
        console.log("match")
        // user exists
        if (response_json[data['username']]['password'] == data['password']){
            document.getElementById("head-username").innerHTML = data['username'];
            document.getElementById("login").style.display = "none";
            document.getElementById("signup").style.display = "none";
            document.getElementById("delete").style.display = "inline";
            document.getElementById("greeting").innerHTML = "Hello, " + data['username'] + ".";
        } else {
            alert("Incorrect password")
        }
    } else {
        // no user exists
        console.log("no match")
        document.getElementById("head-username").innerHTML = "";
        document.getElementById("login").style.display = "none";
        document.getElementById("signup").style.display = "inline";
        document.getElementById("delete").style.display = "none";
    }

}

function updatePOST(response_text){
    document.getElementById("login").style.display = "inline";
    document.getElementById("signup").style.display = "none";
    document.getElementById("delete").style.display = "none";
}

function updateDELETE(response_text){
    document.getElementById("login").style.display = "inline";
    document.getElementById("signup").style.display = "none";
    document.getElementById("delete").style.display = "none";
}