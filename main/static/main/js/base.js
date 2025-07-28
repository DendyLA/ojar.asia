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


//link for languages
function setLanguage(lang) {
    fetch('/set_language/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'), // Функция для получения CSRF
        },
        body: JSON.stringify({ lang: lang })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            window.location.reload();
        } else {
            console.error('Ошибка смены языка:', data.error);
        }
    })
    .catch(error => console.error('Ошибка сети:', error));
}

// Функция для получения CSRF-токена
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie) {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}