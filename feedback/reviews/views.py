from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
from django.views import View

class ReviewView(View):
    pass

def review(request):
    if request.method == "POST":        
        form = ReviewForm(request.POST)        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thank-you')
    else:
        form = ReviewForm()
    return render(request, 'reviews/review.html', {
            'form' : form
        })


def thanks(request):
    return render(request, 'reviews/ty.html')