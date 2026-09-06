const IMG = "cactus_game/Images/";
const ITCH_LINK = "https://sarahzoghly.itch.io/cactus"; 

const gameconsole_btn = document.querySelectorAll('#gameconsole');

gameconsole_btn.forEach(app => {
    app.addEventListener('click', () => {
        document.querySelectorAll(".app").forEach(section => section.style.display = "flex");
        document.querySelectorAll("#cat_bg").forEach(section => section.style.display = "none");
        document.querySelector("#headertext").innerHTML = `Cactus (Demo)`;

        document.querySelector("#app-content").innerHTML = `
            <div class="vn-app">
                <img class="vn-bg" id="vn-bg" src="${IMG}bg1.jpg" alt="scene background">
                <div class="vn-score" id="vn-score">Score: 0</div>
                <img class="vn-character" id="vn-character" src="" alt="" style="display:none;">
                <div class="vn-dialogue-box" id="vn-dialogue-box">
                    <div class="vn-speaker-row" id="vn-speaker-row" style="display:none;">
                        <img class="vn-speaker-icon" id="vn-speaker-icon" src="" alt="">
                    </div>
                    <p class="vn-text" id="vn-text"></p>
                    <span class="vn-continue-hint" id="vn-continue-hint">click to continue</span>
                </div>
            </div>
        `;

        VN.start();
    });
});

const VN = (() => {
    let score = 0;
    let queue = [];
    let onQueueDone = null;
    let awaitingClick = false;

    const bg = () => document.getElementById('vn-bg');
    const character = () => document.getElementById('vn-character');
    const speakerRow = () => document.getElementById('vn-speaker-row');
    const speakerIcon = () => document.getElementById('vn-speaker-icon');
    const textEl = () => document.getElementById('vn-text');
    const scoreEl = () => document.getElementById('vn-score');
    const dialogueBox = () => document.getElementById('vn-dialogue-box');
    const appContent = () => document.getElementById('app-content');

    function setBg(file) {
        bg().src = IMG + file;
    }

    function setSpeaker(speaker) {
        
        if (!speaker) {
            character().style.display = "none";
            speakerRow().style.display = "none";
            return;
        }
        speakerRow().style.display = "flex";
        character().style.display = "block";
        if (speaker === "cactus") {
            character().src = IMG + "cactus_character.png";
            speakerIcon().src = IMG + "dialogue_cactus_symbol.png";
        } else if (speaker === "cactus_happy") {
            character().src = IMG + "cactus_happy.png";
            speakerIcon().src = IMG + "dialogue_cactus_symbol.png";
        } else if (speaker === "cactus_evil") {
            character().src = IMG + "cactus_angry.png";
            speakerIcon().src = IMG + "dialogue_cactus_symbol.png";
        }
          else if (speaker === "cactus_sad") {
            character().src = IMG + "cactus_dissappointed.png";
            speakerIcon().src = IMG + "dialogue_cactus_symbol.png";
        }
          else if (speaker === "cactus_shocked") {
            character().src = IMG + "cactus_shocked.png";
            speakerIcon().src = IMG + "dialogue_cactus_symbol.png";
        } else if (speaker === "jeepman") {
            character().src = IMG + "jeep_man_normal.png";
            speakerIcon().src = IMG + "dialogue_man_symbol.png";
        } else if (speaker === "jeepman_angry") {
            character().src = IMG + "jeep_man_angry.png";
            speakerIcon().src = IMG + "dialogue_man_symbol.png";
        }
    }

    function playQueue(lines, done) {
        queue = lines.slice();
        onQueueDone = done;
        advance();
    }

    function advance() {
        if (queue.length === 0) {
            awaitingClick = false;
            if (onQueueDone) onQueueDone();
            return;
        }
        const line = queue.shift();
        const isObj = typeof line === "object";
        const text = isObj ? line.text : line;
        if (isObj && line.bg) setBg(line.bg);
        if (isObj && "speaker" in line) setSpeaker(line.speaker);
        textEl().textContent = text;
        awaitingClick = true;
    }

    document.addEventListener('click', (e) => {
        if (!awaitingClick) return;
        const box = dialogueBox();
        if (!box || !box.contains(e.target)) return;
        advance();
    });

    function showChoices(options) {
        
        awaitingClick = false;
        const container = document.createElement('div');
        container.className = 'vn-choices';
        container.id = 'vn-choices';
        options.forEach(opt => {
            const btn = document.createElement('button');
            btn.className = 'vn-choice-btn';
            btn.textContent = opt.label;
            btn.addEventListener('click', (e) => {
                e.stopPropagation();
                container.remove();
                opt.onSelect();
            });
            container.appendChild(btn);
        });
        document.querySelector('.vn-app').appendChild(container);
    }

    function showTrivia(questions, done) {
        let i = 0;

        function next() {
            if (i >= questions.length) {
                done();
                return;
            }
            const q = questions[i];
            const allOptions = shuffle([q.answer, ...q.wrong]);

            const box = document.createElement('div');
            box.className = 'vn-trivia-question';
            box.id = 'vn-trivia-question';

            const p = document.createElement('p');
            p.textContent = q.question;
            box.appendChild(p);

            const optWrap = document.createElement('div');
            optWrap.className = 'vn-trivia-options';

            allOptions.forEach(optText => {
                const btn = document.createElement('button');
                btn.className = 'vn-trivia-btn';
                btn.textContent = optText;
                btn.addEventListener('click', (e) => {
                    e.stopPropagation();
                    const correct = optText === q.answer;
                    score += correct ? 5 : -5;
                    scoreEl().textContent = `Score: ${score}`;
                    btn.classList.add(correct ? 'correct' : 'wrong');
                    Array.from(optWrap.children).forEach(b => b.disabled = true);
                    setTimeout(() => {
                        box.remove();
                        i++;
                        next();
                    }, 800);
                });
                optWrap.appendChild(btn);
            });

            box.appendChild(optWrap);
            document.querySelector('.vn-app').appendChild(box);
        }
        next();
    }

    function shuffle(arr) {
        const a = arr.slice();
        for (let i = a.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [a[i], a[j]] = [a[j], a[i]];
        }
        return a;
    }

    function closeConsole() {
        document.querySelectorAll(".app").forEach(section => section.style.display = "none");
        document.querySelectorAll("#cat_bg").forEach(section => section.style.display = "block");
    }

    const TRIVIA = [
        { question: "What do you use to write on a blackboard?", answer: "chalk", wrong: ["marker pen", "crayons", "pencil"] },
        { question: "What's the name of the organ that helps you breathe?", answer: "lungs", wrong: ["kidney", "langs", "toes"] },
        { question: "What's the colored part of your eye called?", answer: "iris", wrong: ["cornea", "pupil", "retina"] },
    ];

    function start() {
        score = 0;
        scoreEl().textContent = `Score: ${score}`;
        setBg("bg1.jpg");
        setSpeaker(null);

        playQueue(intro(), () => {
            playQueue(cactusIntro(), () => {
                playQueue(cactus1stDialogue(), () => {
                    showChoices([
                        { label: "Let's play", onSelect: () => playQueue(cactusHappy(), () => showTrivia(TRIVIA, afterTrivia)) },
                        { label: "No thanks", onSelect: () => playQueue(cactusSad(), afterTrivia) },
                    ]);
                });
            });
        });
    }

    function afterTrivia() {
        setSpeaker(null);
        playQueue(jeepVsPond(), () => {
            showChoices([
                { label: "Walk to the pond", onSelect: pondPath },
                { label: "Walk to the jeep", onSelect: jeepPath },
            ]);
        });
    }

    function pondPath() {
        playQueue(pondDialogue(), () => {
            playQueue(mirageDialogue(), () => {
                textEl().textContent = "You black out.";
                awaitingClick = false;
                setTimeout(() => start(), 2200);
            });
        });
    }

    function jeepPath() {
        playQueue(jeepDialogue(), () => {
            playQueue(jeepManTalk(), () => {
                showChoices([
                    { label: "Give him the bucket", onSelect: () => playQueue(bucketGiven(), showFinalOffer) },
                    { label: "Throw the bucket at his head", onSelect: () => playQueue(bucketThrown(), showFinalOffer) },
                ]);
            });
        });
    }

    function showFinalOffer() {
        playQueue(finalOffer(), () => {
            showChoices([
                { label: "Yes, let's go!", onSelect: acceptFullGame },
                { label: "No, I'm good", onSelect: declineFullGame },
            ]);
        });
    }

    function acceptFullGame() {
        playQueue([{ text: "See you there then!", speaker: "cactus_happy" }], () => {
            window.open(ITCH_LINK, "_blank");
            closeConsole();
        });
    }

    function declineFullGame() {
        playQueue([{ text: "Fine! You are no fun anyway!", speaker: "cactus_evil" }], () => {
            closeConsole();
        });
    }

    function intro() {
        return [
            "You find yourself in the middle of the desert.",
            "You don't remember how you got here. Your head is foggy, and the weather is unbearable.",
            "You're thirsty.",
            "Hungry.",
            "Dizzy.",
            "The sand stretches endlessly in every direction.",
            { text: "You hear a strange sound, you look and spot a grinning floating cactus."},
            { text: "Yes, it has a face." },
            { text: "You don't know whether it is just dehydration or if you have lost your mind"},
        ];
    }

    function cactusIntro() {
        return [
            {text: "Hi there! You are new here, aren't you?", speaker: "cactus_happy" },
            {text: "I'm The Floating Cactus! Your new best friend here!", speaker: "cactus"},
            {text: "You look confused..", speaker: "cactus_sad"},
            {text: "Well, I will help you settle in!", speaker: "cactus_happy"},
            {text: "First, the game is simple, just choose whatever you feel is right. But remember, your choices matter!", speaker: "cactus"},
            "For controls: just click anywhere to continue talking to me, and click a choice when I give you one. That's it!",
            "Also, a tip: never ignore me. We are friends and I really hate being ignored.",
            {text: "Now for the fun part!", speaker: "cactus_happy"}
        ];
    }

    function cactus1stDialogue() {
        return [
            {text: "Do you want to play a little trivia game? :D", speaker: "cactus"},
            "3 trivia questions, if you get 1 right you will earn 5 points! That is a great way to increase your total score!",
            "fun right? :D",
        ];
    }

    function cactusHappy() {
        return ["Amazong! First question:"]
    }

    function cactusSad() {
        return [
            {text: "[A dramatic gasp]", speaker: "cactus_shocked"},
            {text: "Fine! I will be back!", speaker: "cactus_evil"},
            {text:"That was weird.", speaker: null}
        ];
    }

    function jeepVsPond() {
        return [
            "In the distance, you spot two things:",
            {text: "-A shimmering water pond far to your left.", bg: "bg_pond.jpg"},
            {text: "-A black jeep, strange and unmoving, off to the right.", bg: "bg_jeep.jpg"},
            {text: "You have to choose. You can't just sit here and wait for the sun to finish you off.", bg: "bg2.jpg" },
        ];
    }

    function pondDialogue() {
        return [
            { text: "You start walking towards the water pond.", bg: "bg_pond.jpg" },
            "But with every step, the distance seems to stretch further away.",
            "You keep walking... and walking...",
        ];
    }

    function mirageDialogue() {
        return [
            "The pond never gets any closer.",
            "It was a mirage.",
            "You're more lost than before, the heat pressing down on you like a weight.",
            "Exhausted, dizzy, and drained from the endless walk",
            "You collapse in the sand.",
        ];
    }

    function jeepDialogue() {
        return [
            { text: "You walk towards the jeep.", bg: "bg_jeep_man_inspecting.jpg" },
            "After reaching it, you see a man inspecting the engine.",
            "It looks like the jeep is broken."
        ];
    }

    function jeepManTalk() {
        return [
            "You call for him",
            {text: "He walks towards you with a questioning look", bg: "bg_jeep.jpg" },
            "You explain that you're lost and don't remember how you got here.",
            {text: "I was headed to a nearby village, but the jeep broke down.", speaker: "jeepman"},
            "The jeep needs water to start again",
            "There is a well nearby, but I have nothing to fetch water with.",
            "If you help me, I might help you in return.",
        ];
    }

    function bucketGiven() {
        return [
            { text: "Thank you the bucket", speaker: "jeepman" },
            {text: "He takes it, walks off towards the well.", speaker: null},
            { text: "As you wait you hear a strange sound. Looking up, you spot it again.", speaker: null },
            { text: "Hehehehe", speaker: "cactus_happy" },
            "Hey there again!",
        ];
    }

    function bucketThrown() {
        return [
            { text: "OW!", speaker: "jeepman_angry" },
            "What is wrong with you!?",
            "Ughhh.. if you just weren't so.. pathetic",
            "Fine. Come make yourself useful",
            { text: "You were just going after him but a strange sound stopped you.", speaker: null },
            "You look up.",
            { text: "Hehehe!", speaker: "cactus_happy" },
            "Hey there again!",
        ];
    }

    function finalOffer() {
        return [
            { text: "Sooo... actually, forget trivia for a second.", speaker: "cactus" },
            "I've got something way better than another quiz.",
            {text: "There's a WHOLE game out there. My full desert. My full nonsense. Way more of me, if that isn't scary enough already.", speaker: "cactus_happy"},
            "Wanna go play the real thing?",
        ];
    }

    return { start };
})();
