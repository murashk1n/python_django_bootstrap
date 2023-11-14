from django import forms

from cities.models import City
from trains.models import Train


class TrainForm(forms.ModelForm):
    name = forms.CharField(label='Train number', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter a train number'}))
    travel_time = forms.IntegerField(label='Duration', widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter a duration'}))
    from_city = forms.ModelChoiceField(label='From', queryset=City.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control'}))
    to_city = forms.ModelChoiceField(label='To', queryset=City.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control'}))

    class Meta:
        model = Train
        fields = '__all__'
