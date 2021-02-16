from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import VerifiedTagForm
from map.models import VerifiedTag



def index(request):

    if request.method == 'POST':
        form = VerifiedTagForm(request.POST, request.FILES)
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

def my_tags(request):
    tags = VerifiedTag.objects.all()

    return render(request, 'my_tags.html', {'tags': tags})
