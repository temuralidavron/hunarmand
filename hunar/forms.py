from django import forms
from .models import Anketa, MarkAnketa, User


class Markanketaform(forms.ModelForm):


    class Meta:
        model = MarkAnketa

        fields = '__all__'



class Anketaform(forms.ModelForm):


    class Meta:
        model = Anketa
        exclude = ('fname',)





