from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from polls.models import Question

# http://.../poll
def index(request):
	latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)


# http://.../poll/3
def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})

# http://.../poll/3/results
def results(request, question_id):
	return HttpResponse("You're looking at the results of poll %s." % question_id)

# http://.../poll/3/vote
def vote(request, question_id):
	return HttpResponse("You're voting on poll %s." % question_id)
