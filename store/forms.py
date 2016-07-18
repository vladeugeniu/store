from django import forms

from .models import Sell, Buy

class SellForm(forms.ModelForm):

    class Meta:
        model = Sell
        fields = ('name', 'surrname', 'adress', 'mentions',)

class BuyForm(forms.ModelForm):

	class Meta:

		model = Buy
		fields = ('book_name', 'author', 'description', 'category', 'price', 'amount', 'first_name', 'last_name', 'phone_number', 'email')