from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(
            label = '',
            widget= forms.TextInput(attrs={"placeholder": 'Your Title'}))
    email = forms.EmailField()
    description = forms.CharField(
                    required = False, 
                    widget = forms.Textarea(
                        attrs={
                            "placeholder": 'Your Description',
                            'class': 'new-class-name two',
                            'id' : 'my-id-for-textarea',
                             'columns' : 20,
                             'rows':10
                        }
                    
                    ))
    price = forms.DecimalField(initial = 0.00)
    class Meta: 
        model = Product
        #fields = '__all__'
        fields = [
            'title',
            'description',
            'price'
        ]
    def clean_title(self,*args,**kwargs):
        title = self.cleaned_data.get('title')
        if 'hassnain' in title:
            return title
        else:
            raise forms.ValidationError("This is not a valid title")
    
    def clean_email(self,*args,**kwargs):
        email = self.cleaned_data.get('email')
        if not email.endswith('edu'):
            raise forms.ValidationError("This is not a valid email ")

class RawProductForm(forms.Form):
    title = forms.CharField(label = '',widget= forms.TextInput(attrs={"placeholder": 'Your Title'}))
    description = forms.CharField(
                    required = False, 
                    widget = forms.Textarea(
                        attrs={
                            "placeholder": 'Your Description',
                            'class': 'new-class-name two',
                            'id' : 'my-id-for-textarea',
                             'columns' : 20,
                             'rows':10
                        }
                    
                    ))
    price = forms.DecimalField(initial = 0.00)

# class RawProductForm(forms.Form):
#     title = forms.CharField()
#     description = forms.CharField()
#     price = forms.DecimalField()