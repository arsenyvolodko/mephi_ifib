from django import forms
from .models import User


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    is_superuser = forms.BooleanField(label='Менеджер (Админ)', required=False)
