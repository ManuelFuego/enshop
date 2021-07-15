from .models import *
from django import forms

class AddCategory(forms.ModelForm):
    model = Category
    fields = '__all__'

class AddClient(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('first_name','last_name','phone','address')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AddProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'name', 'description', 'quantity', 'price', 'link')
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'cols':30, 'rows':3, 'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'link': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PriceFilter(forms.Form):
    min_price = forms.IntegerField(label= 'От', required= False)
    max_price = forms.IntegerField(label= 'До', required= False)
    widgets = {
        'field_name':"Фильтр стоимости",
        'max_price': forms.NumberInput(attrs={'class':'form_control'}),
        'min_price': forms.NumberInput(attrs={'class': 'form_control'})
    }

class CategoryFilter():
    pass

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"