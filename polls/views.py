from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Choice, Question

# Create your views here.

# def index(request):
# #    return HttpResponse("こんにちは, world! You're at the poll index.😆")
#     context = {
#         'latest_question_list': Question.objects.order_by('-pub_date')[:5],
#     }
#     return render(request, 'polls/index.html', context)


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # don't retrun future date.
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


# def detail(request, question_id):
#     q = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {
#         'question': q
#     })

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


# def results(request, question_id):
#     q = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': q})

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    try:
        # TODO: requestを直接処理してよい?
        selected_choice = q.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # TODO: Don't show error_message. or this code is guard?
        # that must check at client side.
        return render(request, 'polls/detail.html', {
            'question': q,
            'error_message': "You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        # prevent to handle double click by redirect.
        path_from_viewname = reverse('polls:results', args=(question_id,))
        return HttpResponseRedirect(path_from_viewname)


def get404(request, question_id):
    try:
        q = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request, 'polls/detail.html', {
        'question': q
    })


def get404_shortcut(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    # これはよく使われるので省略APIのget_object_or_404がある
    # try:
    #     q = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {
        'question': q
    })
