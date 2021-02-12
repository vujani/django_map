from .models import VerifiedTag, UnverifiedTag
from django.forms import ModelForm, TextInput, Textarea, FileField, FloatField, CharField


class VerifiedTagForm(ModelForm):
    class Meta:
        model = VerifiedTag
        fields = ['name', 'description', 'image', 'location', 'x_coord', 'y_coord', 'user']
        widgets = {
            'name': TextInput(attrs={
                'class': 'name-input',
                'placeholder': 'Название'
            }),
            'description': Textarea(attrs={
                'class': 'description-input',
                'placeholder': 'Введите описание'
            }),
            'location': TextInput(attrs={
                'class': 'location-input',
                'placeholder': 'Мустоположение'
            }),
        }