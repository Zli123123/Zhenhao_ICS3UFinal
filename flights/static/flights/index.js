// clock code copied from a website. I tried to make a clock using datetime + setInterval in 3 different ways but I gave up after repeated errors. There's an easier method via javascript modules
let clock = () => {
    let date = new Date();
    let hrs = date.getHours();
    let mins = date.getMinutes();
    let secs = date.getSeconds();
    let period = "AM";
    if (hrs == 0) {
        hrs = 12;
  } else if (hrs >= 12) {
    hrs = hrs - 12;
    period = "PM";
  }
  hrs = hrs < 10 ? "0" + hrs : hrs;
  mins = mins < 10 ? "0" + mins : mins;
  secs = secs < 10 ? "0" + secs : secs;

  let time = `${hrs}:${mins}:${secs} ${period}`;
  document.querySelector("#clock").innerHTML = time;
  setTimeout(clock, 1000);
};

document.addEventListener('DOMContentLoaded', function() {
  clock();
})

