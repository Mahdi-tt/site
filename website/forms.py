from django import forms
from .models import contact
from django.forms import ModelForm
from django_recaptcha.fields import ReCaptchaField
# from captcha.fields import ReCaptchaField 

# create forms 

class contactForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta():
        model = contact
        fields = '__all__'