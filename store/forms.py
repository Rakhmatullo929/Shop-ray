from django import forms
from .models import *


class OrderForm(forms.Form):
    address = forms.ChoiceField(choices=DISTRICTS, widget=forms.Select(attrs={
        'class': 'input',
        'placeholder': 'Your address'
    }), label='Write your address')

    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input',
        'placeholder': 'Your phone number',
        'value': '998'
    }), label='Write your phone')

    class Meta:
        model = Order
        fields = ['address', 'phone']


class ReviewForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea'}),
                           label='Напишите отзыв')
    rating = forms.ChoiceField(choices=RATE_CHOICES, required=True,
                               label='Оценице от 1 до 5', )

    class Meta:
        model = Review
        fields = ['text', 'rating']
