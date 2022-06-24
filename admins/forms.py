from django import forms
from .models import *

class TrainForm(forms.ModelForm):
    class Meta:
        model = Train
        fields = '__all__'
        widgets = {
            'train_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = '__all__'
        widgets = {
            'source': forms.TextInput(attrs={'class': 'form-control'}),
            'destination': forms.TextInput(attrs={'class': 'form-control'}),
            'From': forms.TimeInput(attrs={'class': 'form-control'}),
            'To': forms.TimeInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'number_of_seats': forms.NumberInput(attrs={'class': 'form-control'}),
            'ticket_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'trip_id': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class SearchTripForm (forms.ModelForm):
    class Meta:
        model =Trip
        fields=['source',
                 'destination',
                 'date',
                 'number_of_seats',
                 'ticket_price',

        ]
        widgets={
            'date':forms.DateInput(attrs={'type':'date'}),
            'number_of_seats':forms.NumberInput(attrs={'type':'number'}),
            'ticket_price':forms.NumberInput(attrs={'type':'number'})
        }
    