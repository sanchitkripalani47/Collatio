from django import forms
from .models import Product

class BrandForm(forms.Form):
    brands = forms.ModelMultipleChoiceField(choices=Product.objects.values_list('brand'), 
    widget=forms.CheckboxSelectMultiple(), required=False)

    class Meta:
        model = Product
        fields = ['brand']