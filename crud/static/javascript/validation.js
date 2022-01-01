<!-- Password verification and error message -->
//adding dom event listener to allow the verifyPassword funtion to be attached to the form. This is so we can keep our JS separate from our html and not have onsubmit in the form.

'use strict' //ensures best environment to prevent JS programmer error and tells browser to use most modern version of JS interpreter it has.

document.addEventListener("DOMContentLoaded", function(){
    // event listener fires when the DOM is fully loaded. This way you can write scripts that are before the elements are loaded into the dom, but waits to be added to the page until the dom is fully loaded.

    document.querySelector('#create').addEventListener('submit', verifyPassword );
    //querySelector selects elements with CSS selectors. id="create" gets selected with the code above.

    // pulled this function in here to keep it private from the window object/global scope. This is one way to protect your variables and functions from being hijacked by xss. Declared function names do act like variables in a way.

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

    } //this function could be expanded upon, where we use JS to completely validate the form and have HTML5 as a fallback. Let me know if you want to have me expand this. - T

    //additional listeners and functions could/should be put in here.

}); //end DOMContentLoaded listener