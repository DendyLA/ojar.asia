$('.slider').slick({
	dots: false,
	infinite: true,
	autoplay: true,
	autoplaySpeed: 3000,
	speed: 500,       // Уменьшено с 500 мс
	fade: true,
	cssEase: 'linear',
	waitForAnimate: false, // Важно для плавности
	pauseOnHover: false,   // Отключаем паузу при наведении
	pauseOnFocus: false    // Отключаем паузу при фокусе
});
//News
const swiperNews = new Swiper('.swiper', {
	slidesPerView: 4,
	centeredSlides: true,
	spaceBetween: 40,
	initialSlide: 0,
	
	// Эффект перехода
	slideToClickedSlide: true,
	
	// Навигация
	navigation: {
		nextEl: '.swiper-button-next',
		prevEl: '.swiper-button-prev',
	},
	
	// Пагинация
	pagination: {
		el: '.swiper-pagination',
		clickable: true,
		dynamicBullets: true,
		type: "progressbar"
	},
	// События
	breakpoints: {
    // when window width is <= 767px
    0: {
      slidesPerView: 2,
      centeredSlides: true,
      spaceBetween: 20
    },
    // планшеты
    768: {
      slidesPerView: 2,
      spaceBetween: 30
    },
    // десктоп
    992: {
      slidesPerView: 4,
      spaceBetween: 40
    }
  }
})


//Awards
new Glider(document.querySelector('.awards__wrapper'), {
	slidesToShow: 'auto',
	slidesToScroll: 'auto',
	draggable: true,
});