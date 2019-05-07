from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import Free
from .forms import FreeForm 

# Create your views here.
def free_new(request):
    return render(request, 'free_new.html')

def free_create(request):
    if request.method == 'POST':
        form = FreeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/free')
        else:
            return HttpResponseRedirect('/')
    else:
        form = FreeForm()
        return render(request, 'free_new.html', {'form': form})

def free(request):
    contents = Free.objects.all
    return render(request, 'free.html', {'contents' : contents})

def free_detail(request, content_id):
    content_detail = get_object_or_404(Free, pk = content_id)
    return render(request, 'free_detail.html', {'content': content_detail})
