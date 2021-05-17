from django import forms


class ProductForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    min_price = forms.CharField()
    end_date = forms.CharField()
    image = forms.FileField()
