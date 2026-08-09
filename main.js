const os_button = document.getElementById('enter-os');
let entered_os = false;
document.querySelectorAll(".os").forEach(section => section.style.display = "none");

os_button.addEventListener('click', () => {
    if (entered_os ){
        document.querySelectorAll(".welcome").forEach(section => section.style.display = "none");
        document.querySelectorAll(".os").forEach(section => section.style.display = "grid");
    }
    else{
        entered_os = true;
    }
});
