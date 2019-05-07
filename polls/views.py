from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import Polls
from .forms import PollsForm

# Create your views here.


def polls_new(request):
    return render(request, 'polls/polls_new.html')


def polls_create(request):
    if request.method == 'POST':
        form = PollsForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/polls')
        else:
            return HttpResponseRedirect('/')
    else:
        form = PollsForm()
        return render(request, 'polls_new.html', {'form': form})
        

def ranking(request):
    scores = Polls.objects
    return render(request, 'polls.html', {'scores' : scores})


def rank_detail(request, score_id):
    score_detail = get_object_or_404(Polls, pk = score_id)
    return render(request, 'polls_detail.html', {'score': score_detail})