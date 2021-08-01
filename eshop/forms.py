from django import forms
from django.forms import ModelForm, NumberInput
import datetime
from .models import *


class AddCategory(forms.ModelForm):
    model = Category
    fields = '__all__'


class AddClient(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'phone', 'address')
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
            'description': forms.Textarea(attrs={'cols': 30, 'rows': 3, 'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'link': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PriceFilter(forms.Form):
    min_price = forms.IntegerField(label='От', required=False)
    max_price = forms.IntegerField(label='До', required=False)
    widgets = {
        'field_name': "Фильтр стоимости",
        'max_price': forms.NumberInput(attrs={'class': 'form_control'}),
        'min_price': forms.NumberInput(attrs={'class': 'form_control'})
    }


class CategoryFilter():
    pass

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('customer', 'first_name', 'last_name',
                  'phone', 'products', 'price',
                  'total_products',
                  'address', 'status',
                  'buying_type', 'comment',
                  #'created_at',
                  'order_date'
                  )
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput({'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'products': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_products': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'cols': 10, 'rows': 1, 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'buying_type': forms.Select(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'cols': 30, 'rows': 1, 'class': 'form-control'}),
            #'created_at': forms.DateTimeField(attrs={'class':'form-control'}),
            #'created_at': forms.DateTimeField(input_formats="%Y-%m-%d %H:%M:%S",),
            #'created_at': forms.DateTimeField(required=True,label="Дата оформления заказа",widget=Calendar),
            'order_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }
class OrderView(ModelForm):
    class Meta:
        model = Order
        fields = ('__all__')
