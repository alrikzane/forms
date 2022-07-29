from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
from .models import Review

def review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            review = Review(user_name=data['user_name'], rating=data['rating'], review_text=data['review_text'])
            review.save()
            return HttpResponseRedirect('/thank-you')
    else:
        form = ReviewForm()
    return render(request, 'reviews/review.html', {
            'form' : form
        })


def thanks(request):
    return render(request, 'reviews/ty.html')