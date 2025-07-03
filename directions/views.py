from django.shortcuts import render

from directions.models import Companies

def directions(request):
	companies = Companies.objects.all()

	content = {
		'companies' : companies,
	}


	return render(request, 'directions/directions.html', content)