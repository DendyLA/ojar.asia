const map = L.map('map').setView([37.959358, 58.421845], 13); 

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a>',
}).addTo(map);


const pinUrl = document.querySelector('.map').dataset.pinUrl;

let myIcon = L.icon({
    iconUrl: pinUrl,
    iconSize: [28, 25],
	iconAnchor: [22, 0],
});

// Добавим маркер
L.marker([37.959358, 58.421845], {icon: myIcon}).addTo(map)
  .bindPopup('Ojar Aziya')
  .openPopup();


//phone

const input = document.querySelector("#id_phone");
const iti = window.intlTelInput(input, {
	initialCountry: "tm",
	preferredCountries: ["tm", "ua", "ru", "cn"],
	separateDialCode: true,
	utilsScript: "https://cdn.jsdelivr.net/npm/intl-tel-input@17/build/js/utils.js"
});


const form  = document.querySelector(".contact-form");
const code = document.querySelector('.iti__selected-dial-code')



form.addEventListener("submit", (e) => {
	e.preventDefault();

	const fullNumber = code.innerText + input.value.trim();

	input.value = fullNumber;
	form.submit();
});


document.addEventListener("DOMContentLoaded", () => {
  const popup = document.querySelector(".popup");

  if (popup.classList.contains("active")) {
    setTimeout(() => {
      popup.classList.remove("active");

      // Убираем параметр ?sent=1 из URL без перезагрузки страницы
      const url = new URL(window.location);
      url.searchParams.delete('sent');
      window.history.replaceState({}, document.title, url.pathname + url.search);
    }, 3000);
  }
});


const popup = document.querySelector(".popup");
const popupWrapper = popup.querySelector(".popup__wrapper");
const popupClose = popup.querySelector(".popup__close");

popupClose.addEventListener("click", () => {
  popup.classList.remove("active");
});

popup.addEventListener("click", (e) => {
  if (!popupWrapper.contains(e.target)) {
    popup.classList.remove("active");
  }
});