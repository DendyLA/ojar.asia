from django.shortcuts import render

from .models import Gallery

def gallery(request):
	gallery = Gallery.objects.all()

	content = {
		'gallery' : gallery
	}

	return render(request, 'gallery/gallery.html', content)