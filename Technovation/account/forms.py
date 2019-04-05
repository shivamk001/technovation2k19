from django import forms
from django.contrib.auth.models import User
from .models import Profile, Participation, Event, Event_Type,Event_Choice


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

## THIS ALLOWS USERS TO EDIT THEIR first name, last name, and email, WHICH ARE ATTRIBUTES OF THE BUILT-IN DJANGO MODEL
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


## THIS ALLOWS USERS TO EDIT THE PROFILE DATA WE SAVE IN THE CUSTOM Profile Model
## USER WILL BE ABLE TO EDIT THEIR YEAR AND PHONE
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('year', 'phone', 'college')

class ParticipationForm(forms.ModelForm):
    class Meta:
        model=Event_Choice
        fields=('event',)
