function onLoad() {
    if (navigator.geolocation){
        navigator.geolocation.getCurrentPosition(getPos);
    }
};

function getPos(position){
    document.getElementById('lat').value = position.coords.latitude;
    document.getElementById('long').value = position.coords.longitude;

    console.log("THisi great!")
};

function handleCredentialResponse(response){
    console.log("handeling");
    console.log(response);
};

function onSignIn(googleUser) {
  var profile = googleUser.getBasicProfile();
  console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
  console.log('Name: ' + profile.getName());
  console.log('Image URL: ' + profile.getImageUrl());
  console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
};

