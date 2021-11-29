var start = document.getElementById('start_timer');
var stop = document.getElementById('stop_timer');
var inuse;


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
*/
stop.addEventListener('click', function(){
    var time = (new Date().getTime() - localStorage.getItem('startTime'))/1000;
    alert("You have studied for " + time + "seconds.");
    document.getElementById('start_timer').style.visibility = 'visible';
    document.getElementById('stop_timer').style.visibility = 'hidden';
    inuse = false;
    localStorage.setItem('inuse', inuse);
    localStorage.clear();
})
