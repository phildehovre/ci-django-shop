from django import forms
from django.contrib.auth.models import User
from .models import Product, ProductTag, Feature, ProductImage

class UpdateProductForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 5}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    tags = forms.ModelMultipleChoiceField(queryset=ProductTag.objects.all(), widget=forms.CheckboxSelectMultiple)
    stock = forms.IntegerField(min_value=0)
    price = forms.FloatField(min_value=0.01)
    

    class Meta:
        model = Product
        fields = ['name', 'image', 'description', 'price', 'tags', 'stock']

class ProductSpecsForm(forms.Form):
    key = forms.CharField(max_length=100)
    value = forms.CharField(max_length=100)

class ProductImageForm(forms.Form):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    alt=forms.CharField(max_length=150)


    class Meta:
        model = ProductImage
        fields = ['image']



class UpdateFeatureForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    title = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}))
    subtitle = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}))
    active = forms.BooleanField(required=False)
    tags = forms.ModelMultipleChoiceField(queryset=ProductTag.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Feature
        fields = ['title', 'subtitle', 'active', 'image']