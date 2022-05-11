const pannel = document.querySelector('#updProfile');
const btnPannel = document.querySelector('#openUpdProfile');

btnPannel.addEventListener('click', () => {
    pannel.classList.toggle('change-form--active')
})