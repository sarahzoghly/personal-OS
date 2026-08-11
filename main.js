const os_button = document.getElementById('enter-os');
const logout_button = document.getElementById('logout');
const btn1 = document.getElementById('warning-bt1');
const btn2 = document.getElementById('warning-bt2');
const close_btn = document.querySelectorAll('.close');
const info_app = document.querySelectorAll('#welcome-app');
let entered_os = false;
let btn1_clicked = false;
let btn2_clicked = false;
let warning = "";
document.querySelectorAll(".os").forEach(section => section.style.display = "none");
document.querySelectorAll("#warning").forEach(section => section.style.display = "none");
document.querySelectorAll(".app").forEach(section => section.style.display = "none");
document.body.style.overflow = 'hidden';

os_button.addEventListener('click', () => {
    entered_os = true;
    os();
});

close_btn.forEach(btn => {
    btn.addEventListener('click', () => {
        document.querySelectorAll(".app").forEach(section => section.style.display = "none");
    });
});

info_app.forEach(app => {
    app.addEventListener('click', () => {
        document.querySelectorAll(".app").forEach(section => section.style.display = "flex");
        document.querySelector("#app-content").innerHTML = `<p id="app-title"> Hi! That is the first version of my OS. I will still work more on it. Have fun around! </p> <br> <img src = "images/cat.gif" alt = "image" height="250px", width="250px">`;
    });
});

const pupils = [
    { el: document.getElementById('pupil-left'), baseX: 90, baseY: 120},
    { el: document.getElementById('pupil-right'), baseX: 145, baseY: 120}
];
const maxDist = 10;

document.addEventListener('mousemove', (e) => {
    const catRect = document.getElementById('cat-with-eyes').getBoundingClientRect();
    pupils.forEach(p => {
        const eyeX = catRect.left + p.baseX;
        const eyeY = catRect.top + p.baseY;
        const angle = Math.atan2(e.clientY - eyeY, e.clientX - eyeX);
        const dx = Math.cos(angle) * maxDist;
        const dy = Math.sin(angle) * maxDist;
        p.el.style.left = (p.baseX + dx) + 'px';
        p.el.style.top = (p.baseY + dy) + 'px';
    });
});

logout_button.addEventListener('click', () => {
    document.querySelector("#warning-text").innerHTML = `ARE YOU SURE?`;
    document.querySelector("#warning-bt1").innerHTML = `Yes, logout`;
    document.querySelector("#warning-bt2").innerHTML = `No`;
    document.querySelectorAll("#warning").forEach(section => section.style.display = "block");
    warning = "logout";
});



btn1.addEventListener('click', () => {
    btn1_clicked = true;
    if (warning == "logout"){
        if (btn1_clicked){
            welcome();
            entered_os = false;
            document.querySelectorAll("#warning").forEach(section => section.style.display = "none");
        }
    }
});

btn2.addEventListener('click', () => {
    btn2_clicked = true;
    if (warning == "logout"){
        if (btn2_clicked){
            document.querySelectorAll("#warning").forEach(section => section.style.display = "none");
        }
    }
});

setInterval(updatetime, 1000);

dragElement(document.getElementById("warning"));
dragElement(document.getElementById("app"));

function welcome(){
    document.querySelectorAll(".os").forEach(section => section.style.display = "none");
    document.querySelectorAll(".welcome").forEach(section => section.style.display = "grid"); 
}

function os(){
    document.querySelectorAll(".welcome").forEach(section => section.style.display = "none");
    document.querySelectorAll(".os").forEach(section => section.style.display = "grid");  
}

function updatetime(){
    var currentTime = new Date().toLocaleString();
    var timeText = document.querySelector("#time");
    timeText.innerHTML = currentTime;
}

function dragElement(elmnt) {
  var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
  if (document.getElementById(elmnt.id + "header")) {
    document.getElementById(elmnt.id + "header").onmousedown = dragMouseDown;
  } else {
    elmnt.onmousedown = dragMouseDown;
  }

  function dragMouseDown(e) {
    e = e || window.event;
    e.preventDefault();
    pos3 = e.clientX;
    pos4 = e.clientY;
    document.onmouseup = closeDragElement;
    document.onmousemove = elementDrag;
  }

  function elementDrag(e) {
    e = e || window.event;
    e.preventDefault();
    pos1 = pos3 - e.clientX;
    pos2 = pos4 - e.clientY;
    pos3 = e.clientX;
    pos4 = e.clientY;
    elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
    elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
  }

  function closeDragElement() {
    document.onmouseup = null;
    document.onmousemove = null;
  }
}