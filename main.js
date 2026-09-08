const os_button = document.getElementById('enter-os');
const logout_button = document.getElementById('logout');
const btn1 = document.getElementById('warning-bt1');
const btn2 = document.getElementById('warning-bt2');
const close_btn = document.querySelectorAll('.close');
const info_app = document.querySelectorAll('#welcome-app');
const drawapp = document.querySelectorAll('#drawapp-button');
const catchat = document.querySelectorAll('#catchat');
const cat = document.querySelectorAll('#cat-with-eyes-app');
const searchBtn = document.getElementById('search-btn');
const searchInput = document.getElementById('search-input');
let entered_os = false;
let btn1_clicked = false;
let btn2_clicked = false;
let warning = "";
var hasDrawn = false;
var already_checked = false;
var eraseron = false;


document.querySelectorAll(".os").forEach(section => section.style.display = "none");
document.querySelectorAll("#warning").forEach(section => section.style.display = "none");
document.querySelectorAll(".app").forEach(section => section.style.display = "none");
document.querySelectorAll("#cat_bg").forEach(section => section.style.display = "block");
document.body.style.overflow = 'hidden';



os_button.addEventListener('click', () => {
    entered_os = true;
    os();
});

close_btn.forEach(btn => {
    btn.addEventListener('click', () => {
        document.querySelectorAll(".app").forEach(section => section.style.display = "none");
        document.querySelectorAll("#cat_bg").forEach(section => section.style.display = "block");
    });
});

info_app.forEach(app => {
    app.addEventListener('click', () => {
        document.querySelectorAll(".app").forEach(section => section.style.display = "flex");
        document.querySelector("#app-content").innerHTML = `
        <p id="app-texttitle">Hi! That is the first version of my OS!</p> 
        <p id="app-maintext">It is called Basb<u>OS</u>a after my cat's Basbousa name (which was named afer that Egyptian dessert)</p>
        <img src = "images/basbousa.png" alt = "basbousa-image" height="250px", width="250px">
        <p id="app-maintext">I will still work more on it. Have fun around! </p> <br> <img src = "images/cat.gif" alt = "image" height="250px", width="250px"> <a href="https://sarahzoghly.github.io/personal-website/" target="_blank">CLICK HERE TO KNOW MORE ABOUT ME!</a>`;
        document.querySelector("#headertext").innerHTML = `Info`
        document.querySelectorAll("#cat_bg").forEach(section => section.style.display = "none");
    });
});

catchat.forEach(app => {
    app.addEventListener('click', () => {
        document.querySelectorAll(".app").forEach(section => section.style.display = "flex");
        document.querySelector("#app-content").innerHTML = `
        <div class="chatapp">
            <div class="chat-container">
                <div id="messages" class="messages"></div>
                <div class="input-area">
                    <input type="text" id="user-input" placeholder="Type a message...">
                    <button id="send-btn">Send</button>
                </div>
            </div>
            <div id="right_side">
                <button id="cat-with-eyes-app"><img src="images/cat_happy.gif" alt="image" height="250px" width="250px"></button>
            </div>
        </div>
        `;
        document.querySelector("#headertext").innerHTML = `CatChat`
        document.querySelectorAll("#cat_bg").forEach(section => section.style.display = "none");
    
        const user_input = document.getElementById('user-input');
        const send_btn = document.getElementById('send-btn');
        const messages_container = document.getElementById('messages');
        const textList = ["...", "Meow~", "MEOW", "Meow Meow", "Meow", "meow?", "Mmmmeow!", "*sniff sniff*", "*ignores you*", "meow meow meow meow meow meow, mow meow; meow meow 'MEOW' m e o w. Meow meow meow, meow!"];
        const catBtn = document.getElementById('cat-with-eyes-app');

        send_btn.addEventListener('click', () => {
            send_message(user_input, messages_container, textList[Math.floor(Math.random() * textList.length)]);
            catBtn.innerHTML = `<img src="images/cf1-hppy.png" alt="image" height="250px" width="250px">`;
            setTimeout(() => {
                catBtn.innerHTML = `<img src="images/cat_happy.gif" alt="image" height="250px" width="250px">`;
            }, 1000);
        });
        user_input.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                send_message(user_input, messages_container, textList[Math.floor(Math.random() * textList.length)]);
                catBtn.innerHTML = `<img src="images/cf1-hppy.png" alt="image" height="250px" width="250px">`;
                setTimeout(() => {
                    catBtn.innerHTML = `<img src="images/cat_happy.gif" alt="image" height="250px" width="250px">`;
                }, 1000);
            }
        });
        catBtn.addEventListener('click', () => {
            catBtn.innerHTML = `<img src="images/cf1-hppy.png" alt="image" height="250px" width="250px">`;
            setTimeout(() => {
                catBtn.innerHTML = `<img src="images/cat_happy.gif" alt="image" height="250px" width="250px">`;
            }, 1000);
        });
    });
});


drawapp.forEach(app => {
    app.addEventListener('click', () => {
        document.querySelectorAll(".app").forEach(section => section.style.display = "flex");
        document.querySelector("#app-content").innerHTML = `
        <div class="drawapp">
            <div class="draw-column">
                <div class="canvas-container">
                    <canvas id="myCanvas">
                        Sorry, your browser doesn't support canvas technology.
                    </canvas>
                </div>
                <div class="drawing-buttons">
                    <button id="guess-btn" class="dr-btn">Ask Basobousa</button>
                    <button id="clear-btn" class="dr-btn">Clear</button>
                    <button id="eraser-btn" class="dr-btn">Eraser</button>

                    <p>Color picker: <select id="selectColor">
                    <option id="colBlack" value="black" selected="selected">Black</option>
                    <option id="colRed" value="red">Red</option>
                    <option id="colBlue" value="blue">Blue</option>
                    <option id="colGreen" value="green">Green</option>
                    <option id="colOrange" value="orange">Orange</option>
                    <option id="colYellow" value="yellow">Yellow</option>
                    </select>
                    </p>
                </div>
            </div>
            <div id="cat-draw">
                <div id="right_side">
                    <button id="cat-with-eyes-app"><img src="images/cat_happy.gif" alt="image" height="250px" width="250px"></button>
                </div>
                <p id="cat-comment">Draw something!</p>
            </div>
        </div>
        `;
        document.querySelector("#headertext").innerHTML = `CatDraw`;
        document.querySelectorAll("#cat_bg").forEach(section => section.style.display = "none");

        const canvas = document.getElementById('myCanvas');
        const container = document.querySelector('.canvas-container');
        const catGuesses = ["...", "Meow~", "MEOW", "Meow Meow", "Meow", "wow.. I dunno", "that a feet?", "*sniff sniff*", "*side-eyes the drawing*", "that looks bad... sry", "I dunno what that is but it looks awesome!", "that looks cute!", "you really drew this??", "I think art isn't your thing..", "haha.. what is that?", "you can pick other colors!", "can I eat that?", "that looks cute!"];


        function resizeCanvas() {
            var snapshot = canvas.toDataURL();

            canvas.width = container.clientWidth;
            canvas.height = container.clientHeight;

            var ctx = canvas.getContext("2d");
            ctx.lineWidth = 5;   

            var img = new Image();
            img.onload = function() {
                ctx.drawImage(img, 0, 0);
            };
            img.src = snapshot;
        }

        window.addEventListener('resize', resizeCanvas);
        resizeCanvas();
        drawing();
        document.getElementById('guess-btn').addEventListener('click', function() {
            if (!hasDrawn) {
                document.getElementById('cat-comment').innerHTML = "Draw something first, silly!";
                catBtn.innerHTML = `<img src="images/cf1-hppy.png" alt="image" height="250px" width="250px">`;
                setTimeout(() => {
                    catBtn.innerHTML = `<img src="images/cat_happy.gif" alt="image" height="250px" width="250px">`;
                }, 1000);
            }
            else if (hasDrawn && !already_checked) {
                const comment = catGuesses[Math.floor(Math.random() * catGuesses.length)];
                document.getElementById('cat-comment').innerHTML = comment;
                already_checked = true;
                catBtn.innerHTML = `<img src="images/cf1-hppy.png" alt="image" height="250px" width="250px">`;
                setTimeout(() => {
                    catBtn.innerHTML = `<img src="images/cat_happy.gif" alt="image" height="250px" width="250px">`;
                }, 1000);
            }
            else{
                document.getElementById('cat-comment').innerHTML = "I saw this drawing before!";
                catBtn.innerHTML = `<img src="images/cf1-hppy.png" alt="image" height="250px" width="250px">`;
                setTimeout(() => {
                    catBtn.innerHTML = `<img src="images/cat_happy.gif" alt="image" height="250px" width="250px">`;
                }, 1000);
            }
        });
        document.getElementById('clear-btn').addEventListener('click', function() {
            const ctx = canvas.getContext("2d");
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            hasDrawn = false;
            already_checked = false;
            document.getElementById('cat-comment').innerHTML = "Draw something!";
        });
        const eraserbtn = document.getElementById('eraser-btn');

        eraserbtn.addEventListener('click', function() {
            if (!eraseron) {
                eraseron = true;
                eraserbtn.textContent = 'Brush';
                eraserbtn.style.backgroundColor = 'rgb(173, 170, 170)';
            } else {
                eraseron = false;
                eraserbtn.textContent = 'Eraser';
                eraserbtn.style.backgroundColor = 'rgb(119, 118, 118)';
            }
        });
        const catBtn = document.getElementById('cat-with-eyes-app');
        catBtn.addEventListener('click', () => {
            catBtn.innerHTML = `<img src="images/cf1-hppy.png" alt="image" height="250px" width="250px">`;
            setTimeout(() => {
                catBtn.innerHTML = `<img src="images/cat_happy.gif" alt="image" height="250px" width="250px">`;
            }, 1000);
        });
    });
});



cat.forEach(catBtn => {
    catBtn.addEventListener('click', () => {
        catBtn.innerHTML = `<img src="images/cf1-hppy.png" alt="image" height="250px" width="250px">`;
        setTimeout(() => {
            catBtn.innerHTML = `<img src="images/cat_happy.gif" alt="image" height="250px" width="250px">`;
        }, 1000);
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

searchInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        const query = searchInput.value.trim();
        if (query === '') return;
        const url = `https://www.google.com/search?q=${encodeURIComponent(query)}`;
        window.open(url, '_blank');
    }
});

searchInput.addEventListener('focus', () => {
    document.body.classList.add('search-focused');
});

searchInput.addEventListener('blur', () => {
    document.body.classList.remove('search-focused');
});

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

function send_message(message, container, bot){
    const trimmed = message.value.trim();
    if (trimmed === '') return;   

    const message_el = document.createElement('p');
    message_el.textContent = trimmed;
    message_el.classList.add('user-message');

    container.appendChild(message_el);

    const botmessage_el = document.createElement('p');
    botmessage_el.innerHTML = `<img src="images/typing.gif" alt="typing..." height="6px" width="20px">`;
    botmessage_el.classList.add('bot-message');
    container.appendChild(botmessage_el);

    message.value = '';
    container.scrollTop = container.scrollHeight;

    setTimeout(() => {
        botmessage_el.textContent = bot;
        container.scrollTop = container.scrollHeight;
    }, 600);
}



function drawing() {
    var myCanvas = document.getElementById("myCanvas");
    var curColor = $('#selectColor option:selected').val();

    if(myCanvas){
        var isDown = false;


        var ctx = myCanvas.getContext("2d");
        var canvasX, canvasY;
        var rect;
        ctx.lineWidth = 5;

        $(myCanvas).mousedown(function(e){
            isDown = true;
            rect = myCanvas.getBoundingClientRect();
            ctx.beginPath();
            canvasX = e.clientX - rect.left;
            canvasY = e.clientY - rect.top;
            ctx.moveTo(canvasX, canvasY);
        }).mousemove(function(e){
            if(isDown != false) {
                canvasX = e.clientX - rect.left;
                canvasY = e.clientY - rect.top;
                ctx.strokeStyle = eraseron ? "white" : curColor;
                ctx.lineTo(canvasX, canvasY);
                ctx.stroke();
                hasDrawn = true;
                already_checked = false;
            }
        })
        .mouseup(function(e){
            isDown = false;
            ctx.closePath();
        });
    }

    $('#selectColor').change(function () {
        curColor = $('#selectColor option:selected').val();
    });

}

function loadWeather() {
    navigator.geolocation.getCurrentPosition(async (position) => {
        const lat = position.coords.latitude;
        const lon = position.coords.longitude;

        const response = await fetch(
            `https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current_weather=true`
        );

        const data = await response.json();

        const temp = data.current_weather.temperature;

        // Open-Meteo uses "weathercode" here
        const code = data.current_weather.weathercode;

        const weatherCodeMap = {
            0: 'Clear sky',
            1: 'Mainly clear',
            2: 'Partly cloudy',
            3: 'Overcast',
            45: 'Fog',
            48: 'Depositing rime fog',
            51: 'Light drizzle',
            53: 'Moderate drizzle',
            55: 'Dense drizzle',
            56: 'Light freezing drizzle',
            57: 'Dense freezing drizzle',
            61: 'Slight rain',
            63: 'Moderate rain',
            65: 'Heavy rain',
            66: 'Light freezing rain',
            67: 'Heavy freezing rain',
            71: 'Slight snow fall',
            73: 'Moderate snow fall',
            75: 'Heavy snow fall',
            77: 'Snow grains',
            80: 'Slight rain showers',
            81: 'Moderate rain showers',
            82: 'Violent rain showers',
            85: 'Slight snow showers',
            86: 'Heavy snow showers',
            95: 'Thunderstorm',
            96: 'Thunderstorm with slight hail',
            99: 'Thunderstorm with heavy hail'
        };

        const con = weatherCodeMap[code] || "Unknown";

        document.getElementById('temperature').textContent = `${temp}°C`;
        document.getElementById('condition').textContent = con;

        const weatherIcon = document.querySelector("#weather-icon img");

        if (code === 95 || code === 96 || code === 99) {

            weatherIcon.src = "images/lightning.gif";

        } else if (
            code === 71 || code === 73 || code === 75 ||
            code === 77 || code === 85 || code === 86
        ) {

            weatherIcon.src = "images/snowy.gif";

        } else if (
            code === 51 || code === 53 || code === 55 ||
            code === 56 || code === 57 ||
            code === 61 || code === 63 || code === 65 ||
            code === 66 || code === 67 ||
            code === 80 || code === 81 || code === 82
        ) {

            weatherIcon.src = "images/raining.webp";

        } else if (code === 0) {

            weatherIcon.src = "images/sunny.gif";

        } else if (code === 1 || code === 2 || code === 3) {

            weatherIcon.src = "images/cloudy.gif";

        } else if (code === 45 || code === 48) {

            weatherIcon.src = "images/foggy.gif";

        } else {

            weatherIcon.src = "images/cloudy.gif";
        }

    }, (error) => {
        document.getElementById('temperature').textContent = "something°C";
        document.getElementById('condition').textContent = "Couldn't get weather";
    });
}




loadWeather();