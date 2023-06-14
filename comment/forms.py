from django import forms
from .models import Comment

class commentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter a comment'}), required=True)


    class Meta:
        model = Comment
        fields = ['body']


   

