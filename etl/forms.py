# form creation by class not with HTML

from django import forms

from .models import CsvData

class CsvDataForm(forms.ModelForm):

    class Meta:
        model = CsvData
        fields = ['name', 'ipv4', 'mac_address']
