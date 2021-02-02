const map = document.querySelector('#redirection-url')
    
// simulates arriving at #Who-We-Are for the purpose of this example
window.location.hash = '#redirection-url';

addEventListener('DOMContentLoaded', event => {
if (window.location.hash === '#redirection-url') {
    map.scrollIntoView({behavior: "smooth", block: "start"});
}
});

document.getElementById("tags").selectedIndex = -1;
document.getElementById("category").selectedIndex = -1;