from django.shortcuts import render
from .forms import PersonForm


def index(request):
    form = PersonForm()

    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}

    return render(request, 'blog/index.html',context)