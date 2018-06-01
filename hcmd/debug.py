def index(request):
	from django.http import HttpResponse
	import pprint
	vars = {'GET' : request.GET, 'POST' : request.POST, 'META' : request.META, 'FILES' : request.FILES}
	return HttpResponse(pprint.pformat(vars))
