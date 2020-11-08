var firebaseConfig = {
    apiKey: "AIzaSyC66IKY6CUapUcoqr5DFIdfUjMtMFDbYYA",
    authDomain: "autozoom-a3a52.firebaseapp.com",
    databaseURL: "https://autozoom-a3a52.firebaseio.com",
    projectId: "autozoom-a3a52",
    storageBucket: "autozoom-a3a52.appspot.com",
    messagingSenderId: "393612684917",
    appId: "1:393612684917:web:696c8b059396d89022d23c",
    measurementId: "G-J1H6CTCHLH"
};
  // Initialize Firebase
firebase.initializeApp(firebaseConfig);

// Reference messages collection
var meetingRef = firebase.database().ref('meeting');

// Listen to form submit
document.getElementById('meetingForm').addEventListener('submit', submitForm);

// Submit Form
function submitForm(e){
    e.preventDefault();

    // Get values
    var name = getinput('mname');
    var link = getinput('mlink');
    var password = getinput('mpassword');
    var time = getinput('mtime');
    var label = getinput('mlabel');

    savemeeting(name, link, password, time, label);

}

// Function to get form values
function getinput(id){
    return document.getElementById(id).value;
}

// Save meeting to firebase
function savemeeting(name, link, password, time, label){
    var newMeetingRef = {
        name: name,
        link: link,
        password: password,
        time: time,
        label: label
    };

    meetingRef.push(newMeetingRef);
}

    