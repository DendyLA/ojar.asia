from django.shortcuts import get_object_or_404, render

from .models import Projects

def projectsCurrent(request):
	projects = Projects.objects.filter(is_finish=False)

	content = {
		'projects' : projects
	}

	return render(request, 'projects/projectsCurrent.html', content)


def projectsNotCurrent(request):
	projects = Projects.objects.filter(is_finish=True)

	content = {
		'projects' : projects
	}

	return render(request, 'projects/projectsNotCurrent.html', content)


def projectsDetail(request, slug):
	project = get_object_or_404(Projects, slug=slug)

	content = {
		'projects' : project
	}

	return render(request, 'projects/projectsDetail.html', content)