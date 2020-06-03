from .models import destination
from django import forms


class destinationform(forms.ModelForm):
    img = forms.ImageField(label='Image')
    desc = forms.CharField(widget=forms.Textarea,label='Description')
    class Meta():
        model=destination
        fields = ['img','name','desc','price','offer']

        
class searchform(forms.Form):
    search = forms.CharField(required=False,max_length=25,widget=forms.TextInput(attrs={'class':'form-control search_input','placeholder':'Search here','required':'required'}))
        