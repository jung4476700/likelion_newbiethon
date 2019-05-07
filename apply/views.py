from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import Apply
from .forms import PostForm

# Create your views here.
def apply_new(request):
    return render(request, 'apply_new.html')

def apply_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/apply')
        else:
            return HttpResponseRedirect('/')
        
    else:
        form = PostForm()
        return render(request, 'apply_new.html', {'form': form})
        
def applying(request):
    applies = Apply.objects
    return render(request, 'apply.html', {'applies' : applies})

def apply_detail(request, apply_id):
    apply_detail = get_object_or_404(Apply, pk = apply_id)
    return render(request, 'apply_detail.html', {'apply_detail': apply_detail})