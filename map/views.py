from django.shortcuts import render, redirect

from .forms import VerifiedTagForm


def index(request):
    return render(request, 'base.html')

def contacts(request):
    return render(request, 'contacts.html')

def faq(request):
    return render(request, 'FAQ.html')

def info(request):
    return render(request, 'info.html')

def ternms_of_use(request):
    return render(request, 'termsofuse.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = VerifiedTagForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма неверная'

    form = VerifiedTagForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'include/forms/add_verified_tag.html', context)