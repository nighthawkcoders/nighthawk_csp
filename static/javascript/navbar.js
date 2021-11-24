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
let clockElement = document.getElementById('clock');
// Clock update executes on each interval set by timer
function clock() {
    let date = new Date();
    clockElement.textContent = date.toLocaleString();
}
// Clock refresh timer, a reoccurring event
setInterval(clock, 1000);
// End Clock Control

