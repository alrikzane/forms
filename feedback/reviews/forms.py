from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        labels = {
            'user_name' : 'Your name'
        }
        error_messages = {
            'user_name' : {
                'required' : 'This field can not be empty!'
            }
        } 
