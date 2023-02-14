from django.forms import ModelForm
from django import forms
from childmissingapp. models import complainant, user, Police
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



# class RegisterForm(UserCreationForm):
#     username = forms.CharField(max_length=15)
#     password1 = forms.CharField(widget=forms.PasswordInput)
#     password2 = forms.CharField(widget=forms.PasswordInput)
#     is_police = forms.BooleanField(initial=False, required=False)
#     badge_number = forms.CharField(max_length=10, required=False)

#     class Meta:
#         model = Registerd_users
#         fields = ['username', 'password1', 'password2', 'is_police', 'badge_number']
    
#     def clean_username(self):
#         username = self.cleaned_data['username']
#         if Registerd_users.objects.filter(username=username).exists():
#             raise forms.ValidationError('Username is already taken')
#         return username


class LoginForm(forms.Form):
    username = forms.CharField(max_length=15)
    password = forms.CharField(widget=forms.PasswordInput)
    is_police = forms.BooleanField(initial=False, required=False)
    badge_number = forms.CharField(max_length=10, required=False)

    class Meta:
        model = Police, User
        fields = ['username', 'password', 'is_police', 'badge_number']


class complainantForm(ModelForm):
    name = forms.CharField()
    place = forms.CharField()
    phone_number = forms.IntegerField()
    child_name = forms.CharField()
    age = forms.IntegerField()
    gender = forms.CharField()
    identification = forms.CharField()
    Details = forms.CharField()
    img = forms.ImageField()

    class Meta:
        model = complainant
        fields = ['name','place','phone_number','child_name','age','gender','identification','Details','img']
        widget = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'place' : forms.TextInput(attrs={'class':'form-control'}),
            'phone_number' : forms.NumberInput(attrs={'class':'form-control'}),
            'child_name' : forms.TextInput(attrs={'class':'form-control'}),
            'age' : forms.NumberInput(attrs={'class':'form-control'}),
            'gender' : forms.TextInput(attrs={'class':'form-control'}),
            'identification' : forms.TextInput(attrs={'class':'form-control'}),
            'img' : forms.FileInput(attrs={'class':'form-control'}),
        }

class userForm(ModelForm):
    name = forms.CharField()
    place = forms.CharField()
    phone_number = forms.IntegerField()
    child_name = forms.CharField()
    age = forms.IntegerField()
    gender = forms.CharField()
    identification = forms.CharField()
    Details = forms.CharField()
    image = forms.ImageField()

    class Meta:
        model = user
        fields = ['name','place','phone_number','child_name','age','gender','identification','Details','image']
        widget = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'place' : forms.TextInput(attrs={'class':'form-control'}),
            'phone_number' : forms.NumberInput(attrs={'class':'form-control'}),
            'child_name' : forms.TextInput(attrs={'class':'form-control'}),
            'age' : forms.NumberInput(attrs={'class':'form-control'}),
            'gender' : forms.TextInput(attrs={'class':'form-control'}),
            'identification' : forms.TextInput(attrs={'class':'form-control'}),
            'image' : forms.FileInput(attrs={'class':'form-control'}),
         }
