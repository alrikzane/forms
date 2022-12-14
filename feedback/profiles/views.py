from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView
from .models import UserProfile

# Create your views here.


class CreateProfileView(CreateView):
    template_name = 'profiles/create_profile.html'
    model = UserProfile
    fields = '__all__'
    success_url = '/profiles'


def profiles(request):
    return render(request, 'profiles/watch_profiles.html', {
        'profiles' : UserProfile.objects.all()
    })