from crispy_forms.helper import FormHelper
from django.forms import ModelForm, Textarea, TextInput
from frontend.models import Order
from kite import settings

__author__ = 'niels-ole'

from django import forms

class OrderForm(ModelForm):
    class Meta:
        model = Order
        exclude = ['paid']
        widgets = {
            'email': TextInput(attrs={'class': 'form-control', 'placeholder': 'ricky@example.com'}),
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Jake Parker'}),
            'address': Textarea(attrs={'class': 'form-control', 'placeholder': 'Full address containing address, city and country'}),
        }

    def clean_image(self):
        image = self.cleaned_data['image']
        if image:
            from django.core.files.images import get_image_dimensions
            w, h = get_image_dimensions(image)
            if not image.content_type in settings.VALID_IMAGE_FORMATS:
                raise forms.ValidationError(u'Only *.gif, *.jpg and *.png images are allowed.')
            if w < settings.VALID_IMAGE_WIDTH or h < settings.VALID_IMAGE_HEIGHT:
                raise forms.ValidationError(u'That image is too small. The image needs to be ' +     str(settings.VALID_IMAGE_WIDTH) + 'px * ' + str(settings.VALID_IMAGE_HEIGHT) + 'px (or more).')
        return image