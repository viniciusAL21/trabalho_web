let show = true;
const menuContent = document.querySelector('.content');
const menuToggle = menuContent.querySelector('.menu-toggle');


menuToggle.addEventListener('click', () => {

    document.body.style.overflow = show ? 'hidden' : 'initial'

    menuContent.classList.toggle('on', show);
    show = !show;
})

document.addEventListener("DOMContentLoaded", function () {
    const statusButtons = document.querySelectorAll(".status-button");
    
    statusButtons.forEach(function (button) {
      button.addEventListener("click", function () {
        toggleStatus(button);
      });
    });
  });
  
  function toggleStatus(button) {
    if (button.innerHTML === "Indisponível") {
      button.innerHTML = "Disponível";
      button.className = "status-disponivel";
    } else {
      button.innerHTML = "Indisponível";
      button.className = "status-indisponivel";
    }
  }