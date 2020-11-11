console.log("Page loaded");

var submitButton = document.getElementById('submit-button')
submitButton.onmouseup = getFormInfo;

function getFormInfo(){
    console.log("get form info");
    var ethnicity;

    // get ethnicity
    if (document.getElementById('american-indian').checked){
        ethnicity = document.getElementById("american-indian").value;
    }

    if (document.getElementById('asian').checked){
        ethnicity = document.getElementById("asian").value;
    }

    if (document.getElementById('black').checked){
        ethnicity = document.getElementById("black").value;
    }

    if (document.getElementById('hispanic-latino').checked){
        ethnicity = document.getElementById("hispanic-latino").value;
    }

    if (document.getElementById('native-hawaiian').checked){
        ethnicity = document.getElementById("native-hawaiian").value;
    }

    if (document.getElementById('white').checked){
        ethnicity = document.getElementById("white").value;
    }

    if (document.getElementById('other').checked){
        ethnicity = document.getElementById("other").value;
    }

    console.log("Ethnicity: " + ethnicity);

    // get whether or not user submitted application
    var submitted;
    if (document.getElementById('yes').checked){
        submitted = document.getElementById("yes").value;
    }

    if (document.getElementById('no').checked){
        submitted = document.getElementById("no").value;
    }

    console.log("Application Submitted: " + submitted);

    // get tests passed
    var tests = [];
    if (document.getElementById('physical').checked){
        tests.push(document.getElementById("physical").value);
    }

    if (document.getElementById('written').checked){
        tests.push(document.getElementById("written").value);
    }

    if (document.getElementById('personal').checked){
        tests.push(document.getElementById("personal").value);
    }

    if (document.getElementById('interview').checked){
        tests.push(document.getElementById("interview").value);
    }

    if (document.getElementById('polygraph').checked){
        tests.push(document.getElementById("polygraph").value);
    }

    console.log("Tests passed: " + tests);

    // make dictionary
    data = {};
    data['ethnicity'] = ethnicity;
    data['submitted'] = submitted;
    data['tests'] = tests;

    console.log("DATA TO BE ADDED:" + data)
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

    console.log(the_data;
    var story_body = document.getElementById('story-body');
    story_body.innerHTML = the_data;
}