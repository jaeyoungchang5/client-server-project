console.log("Page loaded");

var hostUrl = "http://student04.cse.nd.edu";
var portNumber = 51047;
var requestType = "PUT";

var submitButton = document.getElementById('add-data-button')
submitButton.onmouseup = getFormInfo;

function getFormInfo(){
    console.log("get form info");
    var ethnicity;

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
    var submitted;
    if (document.getElementById('yes').checked){
        submitted = document.getElementById("yes").value;
    } else if (document.getElementById('no').checked){
        submitted = document.getElementById("no").value;
    }

    // get tests taken
    var taken = [];
    if (document.getElementById('physical-take').checked){
        taken.push(document.getElementById("physical-take").value);
    }

    if (document.getElementById('written-take').checked){
        taken.push(document.getElementById("written-take").value);
    }

    if (document.getElementById('personal-take').checked){
        taken.push(document.getElementById("personal-take").value);
    }

    if (document.getElementById('interview-take').checked){
        taken.push(document.getElementById("interview-take").value);
    }

    console.log("Tests taken: " + taken);

    // get tests passed
    var passed = [];
    if (document.getElementById('physical-pass').checked){
        console.log("HERE")
        console.log(document.getElementById("physical-pass").value)
        passed.push(document.getElementById("physical-pass").value);
    }

    if (document.getElementById('written-pass').checked){
        passed.push(document.getElementById("written-pass").value);
    }

    if (document.getElementById('personal-pass').checked){
        passed.push(document.getElementById("personal-pass").value);
    }

    if (document.getElementById('interview-pass').checked){
        passed.push(document.getElementById("interview-pass").value);
    }

    console.log("Tests passed: " + passed);

    // make dictionary
    data = {};
    data['ethnicity'] = ethnicity;
    data['submitted'] = submitted;
    data['taken'] = taken;
    data['passed'] = passed;

    console.log(data)
    displayData(data);
}

function displayData(data){
    console.log('entered data!');
    console.log(data);

    // get fields from story and display in label.
    var page_top = document.getElementById('story-top-line');
    page_top.innerHTML = 'Data to be Added';
    
    var the_data = "";

    the_data += "Ethnicity: " + data['ethnicity'] + "<br>";

    the_data += "<br>Submitted Application: " + data['submitted'];
    
    the_data += "<br>Tests Passed: ";
    for (test in data['tests']) {
        the_data += data['tests'][test] + " ";
    }

    var story_body = document.getElementById('story-body');
    story_body.innerHTML = the_data;
}
