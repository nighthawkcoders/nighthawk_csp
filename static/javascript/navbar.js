// Search Bar Control
// open google search window
const search = document.getElementById('search');
const google = 'https://www.google.com/search?q=site%3A+';
const site = 'https://nighthawkcodingsociety.com';

function submitted(event) {
    if (event.key === 'Enter') {
        // calculations to determine new window size at 66% of existing
        const reduction = 0.66;  // reduce by 66%
        const w = Math.trunc(window.innerWidth*reduction);
        const h = Math.trunc(window.outerHeight*reduction);
        const l = Math.trunc(window.top.screenX + ((window.innerWidth - w)/2));
        const t = Math.trunc(window.top.screenY + ((window.outerHeight - h)/2));
        const left = "left=" + l;
        const top = "top=" + t;
        const width = "width=" + w;
        const height = "height=" + h;
        const location = left + ", " + top + ", " + width + ", " + height

        // setup and display window
        event.preventDefault();
        const url = google
            + site
            + '+'
            + search.value;
        const win = window.open(url, "CompSci Principles Search", location);
        win.focus();
    }
}
search.addEventListener('keypress', submitted);


// Dark Mode Control
// darkSwitch global element is set for convenience
const darkSwitch=document.getElementById("darkSwitch");
// establishes the initial state of darkSwitch on page load
if(darkSwitch) {
    // obtains the value of darkSwitch from localStorage
    const darkSwitchSelected =
        localStorage.getItem("darkSwitch") !== null &&
        localStorage.getItem("darkSwitch") === "dark";
    // sets the value of darkSwitch.checked to the global darkSwitch
    darkSwitch.checked=darkSwitchSelected;
    // if dark-mode, toggle the switch to dark-mode position
    if (darkSwitchSelected)
        document.body.classList.toggle("dark-mode");
}
// executes on each "dark mode" UI toggle
function darkFunction() {
    // toggles between off (standard CSS) and dark-mode (.dark-mode CSS)
    document.body.classList.toggle("dark-mode");
    // localStorage is used to manage darkSwitch status
    darkSwitch.checked
        ? localStorage.setItem("darkSwitch","dark")
        : localStorage.removeItem("darkSwitch");
}
// End Dark Mode Control


// Clock Control
// clockElement global element set for convenience
let clockElement = document.getElementById('clock')
// Execute clock function on load
clock();
// Clock update executes on each interval set by timer
function clock() {
    let date = new Date();
    clockElement.textContent = date.toLocaleString();
}
// Clock refresh timer, a reoccurring event
setInterval(clock, 1000);
// End Clock Control

