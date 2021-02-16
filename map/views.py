from django.shortcuts import render, redirect

from .forms import TagForm, UnverifiedTagForm
from map.models import Tag



def index(request):

    if request.method == 'POST' and 'btnform1' in request.POST:
        form = TagForm(request.POST, request.FILES)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.image = request.FILES['image']
            # tag.UserID = request.user !!!!!!!!!!!!
            tag.save()
            return render(request, 'include/tag_added.html')
        else:
            return render(request, 'include/error.html')

    if request.method == 'POST' and 'btnform2' in request.POST:
        form = UnverifiedTagForm(request.POST, request.FILES)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.image = request.FILES['image']
            # tag.UserID = request.user !!!!!!!!!!!!
            tag.save()
            return render(request, 'include/tag_added.html')
        else:
            return render(request, 'include/error.html')

    form = TagForm()
    form2 = UnverifiedTagForm()
    context = {
        'form': form,
        'form2': form2
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
    tags = Tag.objects.filter(user=request.user)

    return render(request, 'my_tags.html', {'tags': tags})
