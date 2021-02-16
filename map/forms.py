from .models import VerifiedTag, UnverifiedTag
from django.forms import ModelForm, TextInput, Textarea


class VerifiedTagForm(ModelForm):
    class Meta:
        model = VerifiedTag
        fields = ['name', 'description', 'image', 'location', 'x_coord', 'y_coord', 'user']
        # fields = ['name', 'description', 'image', 'location', 'x_coord','y_coord']
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
