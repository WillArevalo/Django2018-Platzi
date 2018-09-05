from django.http import HttpResponse
from datetime import datetime
import json

def hello_world(request):
	"Return a Gretting."
	now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
	return HttpResponse(
		'Oh, hi! Current server time is {}'.format(now)
	)

def sorted(request):
	"sorted."
	#import pdb; pdb.set_trace()   Debugger
	numbers = request.GET['numbers'].split(',')
	numbers = [int(i) for i in numbers]
	numbers = sorted(numbers)
	data = {
		'status':'ok',
		'numbers':numbers,
		'message':'Integers sorted successfully.'
	}
	return HttpResponse(
		json.dumps(data, indent=4), 
		content_type='application/json'
	)
def say_hi(request, name, age):
	"Say Hi."
	if age < 12:
		message = 'Sorry {name}, you aren\'t allowed here'.format(
			name = name
		)
	else:
		message = 'Hello {name}, Welcome to Platzigram!'.format(
			name = name
		)
	return HttpResponse(message)

