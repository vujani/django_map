from django.shortcuts import render, redirect

from .forms import VerifiedTagForm


def index(request):

    if request.method == 'POST':
        form = VerifiedTagForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'include/tag_added.html')
        else:
            return render(request, 'include/error.html')


    form = VerifiedTagForm()
    context = {
        'form': form
    }

    return render(request, 'base.html', context)

def contacts(request):
    return render(request, 'contacts.html')

def faq(request):
    return render(request, 'FAQ.html')

def info(request):
    return render(request, 'info.html')

def ternms_of_use(request):
    return render(request, 'termsofuse.html')