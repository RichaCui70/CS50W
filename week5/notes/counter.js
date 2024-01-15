let counter = 0;
function count() {
    document.querySelector('h1').innerHTML = ++counter
    if (counter % 10 === 0) {
        alert(`counter is now ${counter}!`)
    }
}
document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('button').onclick = count;
})