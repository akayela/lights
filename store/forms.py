from django import forms
from .models import Stock

class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = [ 
                'category',
                'color',
                'condition',
                'unit',
                'size',
                'stock_code',
                'quantity',
                'location',
                'shelf_id',
                'container_id',
                ] 

        def clean_name(self):
            name = self.cleaned_data.get('category')
            if not category:
                raise forms.ValidationError('This field is required')
            return category


class StockUpdateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = [ 
               'category',
                'color',
                'condition',
                'unit',
                'size',
                'stock_code',
                'quantity',
                'location',
                'shelf_id',
                'container_id',
                ] 


class IssueForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = [
                'issue_quantity',
                ]


class ReceiveForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = [
                'receive_quantity',
                ]
