from django.http import HttpResponse, Http404
from django.shortcuts import render

from polls.models import Question


def index(request):
	latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
	context = {'latest_poll_list': latest_poll_list}
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})

def results(request, poll_id):
	return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
	return HttpResponse("You're voting on poll %s." % poll_id)
