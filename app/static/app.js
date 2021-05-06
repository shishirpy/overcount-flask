function onLoad() {
    if (navigator.geolocation){
        navigator.geolocation.getCurrentPosition(getPos);
    }
};

function getPos(position){
    document.getElementById('lat').value = position.coords.latitude;
    document.getElementById('long').value = position.coords.longitude;
};