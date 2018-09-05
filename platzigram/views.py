from django.http import HttpResponse
from datetime import datetime
from numpy import sort

def hello_world(request):
	"Return a Gretting."
	now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
	return HttpResponse('Oh, hi! Current server time is {}'.format(now))

def hi(request):
	"Hi."
	#import pdb; pdb.set_trace()   Debugger
	numbers = request.GET['numbers'].split(',')
	numbers = [int(i) for i in numbers]
	numbers = sort(numbers)
	return HttpResponse('{}\n'.format(x) for x in numbers)

