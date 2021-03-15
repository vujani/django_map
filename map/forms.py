from .models import UnverifiedTag, Tag
from django.forms import ModelForm, TextInput, Textarea, EmailInput, FileInput
from django import forms

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = [
            'name',
            'description',
            'image',
            'location',
            'x_coord',
            'y_coord',
            'user'
        ]

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
            'image': FileInput(attrs={
                'required': False
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
        fields = [
            'name',
            'description',
            'image',
            'location',
            'x_coord',
            'y_coord',
            'username',
            'email'
        ]

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
            'image': FileInput(attrs={
                'required': False
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

class Contactform(forms.Form):
    subject = forms.CharField(
        label="Имя",
        widget=forms.TextInput
    )
    from_email = forms.EmailField(
        label='Почта',
        widget=forms.EmailInput
    )
    message = forms.CharField(
        label="Сообщение",
        widget=forms.Textarea
    )