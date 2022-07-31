from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from .models import Review
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



class ThankYou(TemplateView):
    template_name = 'reviews/ty.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "This works"
        return context


class ReviewsView(TemplateView):
    template_name = 'reviews/reviews.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.all()
        return context