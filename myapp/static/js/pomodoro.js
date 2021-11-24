var start = document.getElementById('start');
var reset = document.getElementById('reset');
var pause = document.getElementById('pause');
var skip = document.getElementById('skip');

var wm = document.getElementById('workmins');
var ws = document.getElementById('worksecs');
var bm = document.getElementById('brkmins');
var bs = document.getElementById('brksecs');
var counter = document.getElementById('counter');

//Starting Timer Function
var startTimer;

start.addEventListener('click', function(){
    if(startTimer === undefined){
        startTimer = setInterval(timer, 1000);
    } else {
        alert("Timer is already running");
    }
})

//Reset Timer Function
reset.addEventListener('click', function(){
  wm.innerText = 25;
  ws.innerText = 0;
  bm.innerText = 5;
  bs.innerText = 0;
  counter.innerText = 0;
})

//Stop Timer Function
pause.addEventListener('click', function(){
  stopTimer()
  startTimer = undefined;
})

//Skip To Next Pomodoro Phase
skip.addEventListener('click', function(){
    if(wm.innerText == 0 && ws.innerText == 0){
        bm.innerText = 0;
        bs.innerText = 0;
    } else {
        wm.innerText = 0;
        ws.innerText = 0;
    }
})

//Timer Function
function timer(){
    //Work Timer
    if(ws.innerText != 0){
        ws.innerText--;
    } else if(wm.innerText != 0 && ws.innerText == 0){
        ws.innerText = 59;
        wm.innerText--;
    }

    //Break Timer
    if(wm.innerText == 0 && ws.innerText == 0){
        if(bs.innerText != 0){
            bs.innerText--;
        } else if(bm.innerText != 0 && bs.innerText == 0){
            bs.innerText = 59;
            bm.innerText--;
        }
    }

    //Increment Counter after a complete cycle. Every four cycle gives a 15 min break instead of the normal 5 min.
    if(wm.innerText == 0 && ws.innerText == 0 && bm.innerText == 0 && bs.innerText == 0){
        wm.innerText = 25;
        ws.innerText = 0;

        //Checks what type of break the user should recieve
        var breakTime = 0;
        var val = parseInt(counter.innerHTML);

        if ((val + 1) % 4 === 0 && val != 0){
          breakTime = 15;
        } else {
            breakTime = 5}
        bm.innerText = breakTime;
        bs.innerText = 0;
    	counter.innerText++;
    }
}
//Stopping Timer Function
function stopTimer(){
  clearInterval(startTimer);
}
