from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
from django.views import View

class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, 'reviews/review.html', {
            'form' : form
        })
    def post(self, request):
        form=ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thank-you')
        return render(request, 'reviews/review.html', {
            'form' : form
        })




def thanks(request):
    return render(request, 'reviews/ty.html')