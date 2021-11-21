// Dark Mode Toggle
function darkFunction() {
    let element = document.body;
    element.classList.toggle("dark-mode");
}
// Clock controller
let clockElement = document.getElementById('clock');
function clock() {
    let date = new Date();
    clockElement.textContent = date.toLocaleString();
}
// Clock refresh frequency
setInterval(clock, 1000);
