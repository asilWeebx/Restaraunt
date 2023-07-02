from django import forms
from main.models import Bron, Menyu


class MenyuForms(forms.ModelForm):
    class Meta:
        model = Menyu()
        fields = '__all__'
class BronForms(forms.ModelForm):
    class Meta:
        model = Bron()
        fields = '__all__'
