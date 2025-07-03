from django.shortcuts import render, get_object_or_404
from .models import News

def news(request):
	news = News.objects.all()

	content = {
		'news' : news
	}


	return render( request, 'news/news.html', content )


def newsDetail(request, slug):
	news = get_object_or_404(News, slug=slug)

	content = {
		'news' : news
	}

	return render(request, 'news/newsDetail.html', content)
