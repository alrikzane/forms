from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewView.as_view()),
    path('thank-you', views.ThankYou.as_view()),
    path('reviews', views.ReviewsView.as_view()),
    path('reviews/<int:id>', views.DetailedReviewView.as_view(), name='review-detail')     
]
