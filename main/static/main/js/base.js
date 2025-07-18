// Обработчик клика ТОЛЬКО для ссылок с классом activeNav
document.querySelectorAll('.activeNav').forEach(link => {
	link.addEventListener('click', function(e) {
		e.preventDefault();
		const navItem = this.closest('.nav__item');
		const subNav = navItem.querySelector('.sub-nav');

		// Закрываем все другие подменю
		document.querySelectorAll('.sub-nav.active').forEach(menu => {
		if (menu !== subNav) menu.classList.remove('active');
		});

		// Открываем/закрываем текущее подменю
		subNav.classList.toggle('active');
	});
});

// Закрытие при клике вне меню
document.addEventListener('click', function(e) {
	if (!e.target.closest('.nav__item')) {
		document.querySelectorAll('.sub-nav.active').forEach(menu => {
		menu.classList.remove('active');
		});
	}
	});


	//СКРОЛЛ

	// Получаем элементы
	const header = document.querySelector('header');
	const headerHeight = header.offsetHeight;
	document.documentElement.style.setProperty('--header-height', `${headerHeight}px`);

	// Создаем placeholder
	const placeholder = document.createElement('div');
	placeholder.className = 'header-placeholder';
	header.insertAdjacentElement('afterend', placeholder);

	// Обработчик скролла
	window.addEventListener('scroll', function() {
	const scrollPosition = window.scrollY || window.pageYOffset;

	if (scrollPosition > headerHeight) {
		header.classList.add('fixed');
	} else {
		header.classList.remove('fixed');
	}
});


function toogleBurger( burger, header ){
	burger.addEventListener('click', () => {
		burger.classList.toggle('is-active');
		header.classList.toggle('header__active');
	})
	
}

const burger = document.querySelector('.hamburger');
const headerRight = document.querySelector('.header__right')

toogleBurger(burger, headerRight)

