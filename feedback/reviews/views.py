from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from .models import Review
from django.views import View


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


class DetailedReviewView(DetailView):
    template_name = 'reviews/review-detail.html'
    model = Review
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        context["is_liked"] = request.session.get('liked_review') == loaded_review.id
        return context
    

class LikeView(View):
    def post(self, request):
        review_id = request.POST['review_id']
        request.session['liked_review'] = int(review_id)
        return HttpResponseRedirect('/reviews/'+review_id)

