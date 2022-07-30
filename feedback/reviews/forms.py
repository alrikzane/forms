from django import forms
from .models import Review


# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your name", max_length=100, min_length=2)
#     rating = forms.IntegerField(label="Your rating", max_value=5, min_value=1)
#     review_text = forms.CharField(label='Your feedback', widget=forms.Textarea, max_length=300)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        error_messages = {
            'user_name' : {
                'required' : 'This field can not be empty!'
            }
        } 
    