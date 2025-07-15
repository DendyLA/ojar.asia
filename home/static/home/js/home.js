
//Main
// $('.slider').slick({
// 	slidesToShow: 1,
// 	slidesToScroll: 1,
// 	autoplay: true,
// 	autoplaySpeed: 4000,
// 	infinite: true,
// 	draggable: false,
// })

const mainSlider = new Glider(document.querySelector('.slider'), {
	slidesToScroll: 1,
	slidesToShow: 1,
	draggable: false,

})

setInterval(() => {
  	mainSlider.scrollItem((mainSlider.page + 1) % mainSlider.slides.length);
}, 4000);


//News
new Glider(document.querySelector('.news__slider'), {
	slidesToScroll: 4,
	slidesToShow: 4,
	draggable: true,
	dots: '.news__dots',
	arrows: {
		prev: '.slider__prev',
		next: '.slider__next'
	},
	responsive: [
		{

			breakpoint: 1200,
			settings: {
				slidesToShow: 3,
				slidesToScroll: 3
			}
		},
		{

			breakpoint: 992,
			settings: {
				slidesToShow: 2,
				slidesToScroll: 2
			}
		},
		{

			breakpoint: 768,
			settings: {
				slidesToShow: 1,
				slidesToScroll: 1
			}
		}
	]
});

//Awards
new Glider(document.querySelector('.awards__wrapper'), {
	slidesToShow: 'auto',
	slidesToScroll: 'auto',
	draggable: true,
	itemWidth: 620,
	responsive: [
		{
			// при ширине экрана <= 1024px
			breakpoint: 1200,
			settings: {
				itemWidth: 420,
			}
		},
		{
			// при ширине <= 768px
			breakpoint: 992,
			settings: {
				itemWidth: 360,
			}
		},
		{
			// при ширине <= 480px
			breakpoint: 480,
			settings: {
				itemWidth: 620,
			}
		}
	]
});

//video
const container = document.getElementById("player");
    const videoUrl = container.dataset.videoUrl;
    const posterUrl = container.dataset.posterUrl;

    if (videoUrl) {
        const video = document.createElement("video");
        video.src = videoUrl;
        video.poster = posterUrl || "";
        video.controls = true;
        video.style.width = "100%";
        video.style.height = "auto";

        // необязательные параметры
        // video.autoplay = true;
        // video.muted = true;  // нужно для autoplay в Chrome
        // video.loop = true;

        container.appendChild(video);
    } else {
        container.innerText = "Видео не найдено.";
    }