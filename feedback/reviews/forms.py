from django import forms



class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your name", max_length=100, min_length=2)
    rating = forms.IntegerField(label="Your rating", max_value=5, min_value=1)
    review_text = forms.CharField(label='Your feedback', widget=forms.Textarea, max_length=300)

