from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    user = request.user
    print (user.is_authenticated, user.username)
    return render(request, template_name="index.html", context={'user':user})
