from django import forms
from .models import Post, Categories
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

choices=Categories.objects.all().values_list('name','name')
choices_list = []

for c in choices:
    choices_list.append(c)

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={"class":"form-control"}),
            "content": forms.Textarea(attrs={"class":"form-control"}),
            "author" : forms.Select(attrs={"class":"form-control"}),
            "category" : forms.Select(choices=choices_list,attrs={"class":"form-control"}),
            
            
        }
class SignUpForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Password')
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Password')
    class Meta:
        model = User
        fields = fields=["username","first_name","last_name",'email']
        labels={"email":"Email"}
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            }
        
        
class LogInForm(AuthenticationForm):
    class Meta:
        model = User
        username=forms.CharField(widget=forms.TextInput(attrs={'autofocus':True,'class':"form-control"}))
        password=forms.CharField(widget=forms.PasswordInput(attrs={'autofocus':True,'class':"form-control"}))