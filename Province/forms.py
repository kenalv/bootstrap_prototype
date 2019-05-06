from django import forms
from Province.models import Canton,Distric

class SearchForm(forms.Form):
    search_name = forms.CharField(widget=forms.TextInput,required=False)
    options =[("1", "Canton"), ("2", "Distric")]
    search_options = forms.ChoiceField(widget=forms.RadioSelect(),
                              required=True,choices = options)
    filters = [("1", "Province")]
    search_filter = forms.ChoiceField(widget=forms.CheckboxSelectMultiple(),
                              required=False,choices = filters)
    
class CantonForm(forms.ModelForm):
    class Meta:
        model = Canton
        fields = ['province', 'name', 'code']

class DistricForm(forms.ModelForm):
    class Meta:
        model = Distric
        fields = ['canton', 'name', 'code']
