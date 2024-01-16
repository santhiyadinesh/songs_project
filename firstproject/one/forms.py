from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Review 
from .models import UserProfile


class Meta:
        model=User
        fields=['username','first_name','last_name','email']



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['username', 'stars', 'reviews']

class profileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
