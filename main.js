const os_button = document.getElementById('enter-os');
let entered_os = false;
document.querySelectorAll(".os").forEach(section => section.style.display = "none");
document.body.style.overflow = 'hidden';

os_button.addEventListener('click', () => {
    if (entered_os ){
        document.querySelectorAll(".welcome").forEach(section => section.style.display = "none");
        document.querySelectorAll(".os").forEach(section => section.style.display = "grid");
    }
    else{
        entered_os = true;
    }
});

const pupils = [
    { el: document.getElementById('pupil-left'), baseX: 90, baseY: 120},
    { el: document.getElementById('pupil-right'), baseX: 145, baseY: 120}
];
const maxDist = 3;

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
