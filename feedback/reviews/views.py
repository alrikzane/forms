from django.http import HttpResponseRedirect
from django.shortcuts import render

def review(request):
    if request.method == "POST":
        entered_username = request.POST['name']
        if entered_username == "":
            return render(request, 'reviews/review.html', {
                'error' : True
            })
        print(entered_username)
        return HttpResponseRedirect('/thank-you')
    else:
        
        return render(request, 'reviews/review.html', {
                'error' : False
            })


def thanks(request):
    return render(request, 'reviews/ty.html')