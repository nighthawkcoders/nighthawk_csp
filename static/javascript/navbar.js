// Dark Mode Toggle

const darkSwitch=document.getElementById("darkSwitch");
if(darkSwitch)
    initDarkSwitch();

function initDarkSwitch(){
    const darkSwitchSelected=localStorage.getItem("darkSwitch") !==null
        && localStorage.getItem("darkSwitch") === "dark";
    darkSwitch.checked=darkSwitchSelected;
    darkSwitchSelected
        ? document.body.setAttribute("data-theme","dark")
        : document.body.removeAttribute("data-theme")
    if(darkSwitchSelected){
        darkFunction();
    }
}

function darkFunction() {
    let element = document.body;
    element.classList.toggle("dark-mode");

    darkSwitch.checked
        ? localStorage.setItem("darkSwitch","dark")
        : localStorage.removeItem("darkSwitch");
}

// Clock controller
let clockElement = document.getElementById('clock');
function clock() {
    let date = new Date();
    clockElement.textContent = date.toLocaleString();
}
// Clock refresh frequency
setInterval(clock, 1000);
