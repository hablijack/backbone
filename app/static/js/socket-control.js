$(document).ready( function() {
    var socket = io();
    socket.on('connect', function() {
        console.log("connected");
    });

    socket.on('change', function(topic) {
        if(topic == "news"){
            $(".backgroundvideo").hide();
            $(".clock").hide();
            $(".newsimage").show();
        } else if(topic == "waiting"){
            $(".newsimage").hide();
            $(".backgroundvideo").show();
            $(".clock").show();
        }
    });
});
