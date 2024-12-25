from.models import comment
from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Invisible

class commentforms(forms.ModelForm):  
    captcha = ReCaptchaField()#widget=ReCaptchaV2Invisible
    class Meta():
        model = comment
        exclude = ('approved',)