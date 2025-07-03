from django.shortcuts import render, get_object_or_404

from .models import Slider, Videos, Awards
from projects.models import Projects
from news.models import News

# Create your views here.
def home(request):
	slides = Slider.objects.all()
	news = News.objects.all()[:10]
	projects = Projects.objects.filter(is_featured=True).order_by('-created_at')[:3]
	videos = get_object_or_404(Videos, id=1)
	awards = Awards.objects.all()

	context = {
		'slides' : slides,
		'news' : news,
		'projects' : projects,
		'videos' : videos,
		'awards' : awards
	}
	return render(request, 'home/home.html', context)

def contacts(request):
	

	return render(request, 'home/contacts.html')