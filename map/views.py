from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
import json
import io
from .models import Images, UImages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.mail import EmailMessage
<<<<<<< Updated upstream
from .forms import TagForm, UnverifiedTagForm, ExtendedUnverifiedTagForm, ExtendedTagForm
=======
from .forms import TagForm, UnverifiedTagForm, ExtendedUnverifiedTagForm, \
    ExtendedTagForm
>>>>>>> Stashed changes
from map.models import Tag, UnverifiedTag
from django_map.settings import MODERATOR_EMAIL
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# function to add to JSON
def write_json(data, filename='static/tags/tags.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def clear_tags(filename='static/tags/tags.json'):
    with io.open(filename, encoding='utf-8') as json_file:
        data = json.load(json_file)

        data['features'] = []

    write_json(data)


def add_tag(filename='static/tags/tags.json',
            coord_x=float,
            coord_y=float,
            tag_id=int,
            name='',
            description='',
            location='',
            user='',
            image='no_img'
            ):
    with io.open(filename, encoding='utf-8') as json_file:
        data = json.load(json_file)

        temp = data['features']

        # python object to be appended
        y = {"type": "Feature",
             "id": tag_id,
             "geometry":
                 {"type": "Point",
                  "coordinates": [coord_x, coord_y]},
             "properties": {
                 "balloonContentHeader":
                     "<font size=3><b><div id='output_name'>" + name + "</div></b></font>",
                 "balloonContentBody":
                     "<div>" + description + "</div>"
                                             "<img src='" + image + "' height='150' width='200'> <br/>"
                                                                    "<div>" + location + "</div>",

                 "balloonContentFooter":
                     "<div>" + user.username + "</div>"
             }}

        # appending data
        temp.append(y)
    write_json(data)


def index(request):
    tags = Tag.objects.all()
    clear_tags()
    for tag in tags:
        add_tag(coord_x=tag.x_coord,
                coord_y=tag.y_coord,
                tag_id=tag.id,
                name=tag.name,
                description=tag.description,
                location=tag.location,
                user=tag.user,
                image='')

    if request.method == 'POST' and 'btnform1' in request.POST:
        form = ExtendedTagForm(request.POST or None, request.FILES or None)
        files = request.FILES.getlist('images')
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            location = form.cleaned_data['location']
            x_coord = form.cleaned_data['x_coord']
            y_coord = form.cleaned_data['y_coord']
            user = request.user
<<<<<<< Updated upstream
            tag_obj = Note.objects.create(user=user, name=name, description=description,
                                           location=location, x_coord=x_coord, y_coord=y_coord)
            for f in files:
                Images.objects.create(tag_object=tag_obj, image=f)

=======
            tag_obj = Tag.objects.create(user=user, name=name, description=description, location=location, x_coord=x_coord,
                                          y_coord=y_coord)
            for f in files:
                Images.objects.create(tag_object=tag_obj, image=f)
>>>>>>> Stashed changes

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
            message = EmailMessage(
                'Запрос на создание метки',
                'Name:' + tag.name + ' Description:' + tag.description + '',
                to=[MODERATOR_EMAIL]
            )
            message.send()
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

<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
@login_required(login_url='/accounts/login/')
def my_tags(request):
    tag_list = Tag.objects.filter(user=request.user)
    paginator = Paginator(tag_list, 3)
    page = request.GET.get('page')
    try:
        tags = paginator.page(page)
    except PageNotAnInteger:
        tags = paginator.page(1)
    except EmptyPage:
        tags = paginator.page(paginator.num_pages)
    return render(request,
                  'my_tags.html',
                  {'page': page,
                   'tags': tags})


@login_required(login_url='/accounts/login/')
def admin_tags(request):
    tag_list = UnverifiedTag.objects.all()

    paginator = Paginator(tag_list, 3)
    page = request.GET.get('page')
    try:
        tags = paginator.page(page)
    except PageNotAnInteger:
        tags = paginator.page(1)
    except EmptyPage:
        tags = paginator.page(paginator.num_pages)
    return render(request,
                  'admin_tags.html',
                  {'page': page,
                   'tags': tags})