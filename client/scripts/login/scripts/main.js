console.log("entered script");
var loginButton = document.getElementById("login-button");
loginButton.onmouseup = getFormInfo;

function getFormInfo() {
    console.log("get form info");

    var email = document.getElementById("input-email").value;
    var password = document.getElementById("input-password").value;
}
