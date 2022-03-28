from django.forms import ModelForm
from .models import ShortenedURL


class CreateShortenedURLForm(ModelForm):
    class Meta:
        model = ShortenedURL
        fields = ['url']