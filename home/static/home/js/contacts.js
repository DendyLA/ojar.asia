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