from .models import UnverifiedTag, Tag
from django.forms import ModelForm, TextInput, Textarea, EmailInput, ClearableFileInput, FileField


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'description', 'location', 'x_coord', 'y_coord', 'user']
        widgets = {
            'name': TextInput(attrs={
                'class': 'name_input',
                'placeholder': 'Название',
                'style': 'border-radius: 5px; border: 2px solid #696969'
            }),
            'description': Textarea(attrs={
                'class': 'description_input',
                'placeholder': 'Введите описание',
                'style': 'border-radius: 5px; border: 2px solid #696969'
            }),
            'location': TextInput(attrs={
                'class': 'location_input',
                'placeholder': 'Местоположение',
                'style': 'border-radius: 5px; border: 2px solid #696969'
            }),
            'x_coord': TextInput(attrs={
                'id': 'id_point_x',
                'style': 'visibility: hidden'
            }),
            'y_coord': TextInput(attrs={
                'id': 'id_point_y',
                'style': 'visibility: hidden'
            }),
        }


class UnverifiedTagForm(ModelForm):
    class Meta:
        model = UnverifiedTag
        fields = ['name', 'description', 'location', 'x_coord', 'y_coord', 'username', 'email']
        widgets = {
            'name': TextInput(attrs={
                'class': 'name_input',
                'placeholder': 'Название',
                'style': 'border-radius: 5px; border: 2px solid #696969'
            }),
            'description': Textarea(attrs={
                'class': 'description_input',
                'placeholder': 'Введите описание',
                'style': 'border-radius: 5px; border: 2px solid #696969'
            }),
            'location': TextInput(attrs={
                'class': 'location_input',
                'placeholder': 'Местоположение',
                'style': 'border-radius: 5px; border: 2px solid #696969'
            }),
            'x_coord': TextInput(attrs={
                'id': 'id_point_x',
                'style': 'visibility: hidden'
            }),
            'y_coord': TextInput(attrs={
                'id': 'id_point_y',
                'style': 'visibility: hidden'
            }),
            'username': TextInput(attrs={
                'class': 'username_input',
                'placeholder': 'Юзернейм',
                'style': 'border-radius: 5px; border: 2px solid #696969'
            }),
            'email': EmailInput(attrs={
                'class': 'email_input',
                'placeholder': 'Email',
                'style': 'border-radius: 5px; border: 2px solid #696969'
            }),

        }

class ExtendedTagForm(TagForm):
    images = FileField(widget=ClearableFileInput(attrs={'multiple': True}))

    class Meta(TagForm.Meta):
        fields = TagForm.Meta.fields + ['images',]


class ExtendedUnverifiedTagForm(UnverifiedTagForm):
    images = FileField(widget=ClearableFileInput(attrs={'multiple': True}))

    class Meta(UnverifiedTagForm.Meta):
        fields = UnverifiedTagForm.Meta.fields + ['images',]