from django import forms
from django.db.models import fields
from .models import Custmer,Message

class MessageForm(forms.ModelForm):
    class Meta:
        model=Message
        fields=['title','content','custmer']



class CustmerForm(forms.ModelForm):
    class Meta:
        model=Custmer
        fields=['name','mail','gender','company','visitday']

class FindForm(forms.Form):
    find=forms.CharField(label='Find',required=False)

class CheckForm(forms.Form):
    # empty=forms.CharField(label='Empty',empty_value=True)
    # min=forms.CharField(label='Min',min_length=10)
    # max=forms.CharField(label='Max',max_length=10)
    str=forms.CharField(label='String')
    def clean(self):
        cleaned_data=super().clean()
        str=cleaned_data['str']
        if(str.lower().startswith('no')):
            raise forms.ValidationError('You input "NO!"')

# class HelloForm(forms.Form):
#     name=forms.CharField(label='Name')
#     mail=forms.EmailField(label='Email')
#     gender=forms.BooleanField(label='Gender',required=False)
#     company=forms.IntegerField(label='company')
#     visitday=forms.DateField(label='Visit',required=False)