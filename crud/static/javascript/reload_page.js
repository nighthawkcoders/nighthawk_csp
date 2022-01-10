<!-- Password verification and error message -->
//adding dom event listener to allow the verifyPassword function(defined in validation.js) to be attached to the form. This is so we can keep our JS separate from our html and not have onsubmit in the form.

'use strict' //ensures best environment to prevent JS programmer error and tells browser to use most modern version of JS interpreter it has.

document.addEventListener("DOMContentLoaded", function() {
    // event listener fires when the DOM is fully loaded. This way you can write scripts that are before the elements are loaded into the dom, but waits to be added to the page until the dom is fully loaded.

    document.querySelector('#create').addEventListener('submit', verifyPassword);
    //querySelector selects elements with CSS selectors. id="create" gets selected with the code above.

    // pulled this function in here to keep it private from the window object/global scope. This is one way to protect your variables and functions from being hijacked by xss. Declared function names do act like variables in a way.

});
