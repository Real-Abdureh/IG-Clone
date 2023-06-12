from userauth.models import Profile
from django import forms

class EditProfileForm(forms.ModelForm):
    picture = forms.ImageField(required=True)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'First Name'}), required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Last Name'}), required=True)
    locaton = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Location'}), required=True)
    # locaton = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'fddfg '}), required=True)
    url = forms.URLField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'URL'}), required=True)
    bio = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Bio'}), required=True)

    class Meta:
        model = Profile
        fields = ['picture', 'first_name', 'last_name', 'location', 'url', 'bio']


