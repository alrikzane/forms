from django.shortcuts import render
from .forms import ReviewForm
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .models import Review


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = '/thank-you'


class ThankYou(TemplateView):
    template_name = 'reviews/ty.html'


class ReviewsView(TemplateView):
    template_name = 'reviews/reviews.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.all()
        return context


class DetailedReviewView(TemplateView):
    template_name = 'reviews/review-detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review'] = Review.objects.get(id=kwargs['id'])
        return context