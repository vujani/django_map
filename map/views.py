from django.shortcuts import render, redirect

from .forms import VerifiedTagForm


def index(request):
    error = ''
    if request.method == 'POST':
        form = VerifiedTagForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма неверная'

    form = VerifiedTagForm()
    context = {
        'form': form
    }

    return render(request, 'base.html', context)