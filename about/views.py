from django.shortcuts import render

from about.models import AboutMain, Info, Comment

def about(request):
	main = AboutMain.objects.all()
	info = Info.objects.all()
	comments = Comment.objects.all()

	context = {
		'main' : main,
		'info' : info,
		'comments' : comments
	}

	return render( request, 'about/about.html', context )