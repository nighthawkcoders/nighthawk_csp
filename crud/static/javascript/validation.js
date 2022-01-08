<!-- Password verification and error message -->

'use strict' //ensures best environment to prevent JS programmer error and tells browser to use most modern version of JS interpreter it has.
function verifyPassword(event) {
    /*
    because this is being called by an event, the event object is automatically
    passed and captured as seen above. We are capturing it with the 'event' parameter in this function.
    This is frequently represented in the following ways in JS: e, evt and event.
    As a variable, it could be called anything - but it makes more sense to call it event rather than banana... etc.
    Name your variables well, my friends.
    */

    const psw =  document.getElementById("password").value;

    if (psw.length < 6 || psw.length > 20) {
        document.getElementById("pswError").innerHTML = "Password must be between 6 and 20 characters";
        event.preventDefault();
        //prevents submission of form when password length is not valid.
    }

}




