var start = document.getElementById('start_timer');
var stop = document.getElementById('stop_timer');
var inuse;

//Checks if Timer is inuse.
if (localStorage.getItem('inuse') == undefined || localStorage.getItem('inuse') == false){
    document.getElementById('start_timer').style.visibility = 'visible';
    document.getElementById('stop_timer').style.visibility = 'hidden';
}
if(localStorage.getItem('inuse')){
    document.getElementById('start_timer').style.visibility = 'hidden';
    document.getElementById('stop_timer').style.visibility = 'visible';
}
/**
*   Start Timer Function
*
*   Parameters
*   addEventListener('click') function activates on click
*/
start.addEventListener('click', function(){
    localStorage.setItem('startTime', new Date().getTime());
    alert("You have started a study session.");
    inuse = true;
    localStorage.setItem('inuse', inuse);
    document.getElementById('start_timer').style.visibility = 'hidden';
    document.getElementById('stop_timer').style.visibility = 'visible';
})

/**
*   Stop Timer Function
*
*   Parameters
*   addEventListener('click') function activates on click
*
*   Returns
*   Sends JSON data to '/posts' route.
*/
stop.addEventListener('click', function(){
    var time = (new Date().getTime() - localStorage.getItem('startTime'));
    alert("You have studied for " + Math.round(time/1000) + " seconds.");
    document.getElementById('start_timer').style.visibility = 'visible';
    document.getElementById('stop_timer').style.visibility = 'hidden';
    var xml = new XMLHttpRequest();
    xml.open("POST", "/posts", true);
    xml.setRequestHeader("Content-type","application/json");
    var data = JSON.stringify({
        "time": time
    });
    xml.send(data);

    inuse = false;

    localStorage.setItem('inuse', inuse);
    localStorage.clear();
})
