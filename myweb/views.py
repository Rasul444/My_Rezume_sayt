from django.shortcuts import render
from django.http import HttpResponse
from .models import SendMessage


# Create your views here.

# class HomepageView(TemplateView):
#     template_name = 'index.html'

def HomePage(request):
    if request.method == "POST":
        username = request.POST['name']
        email = request.POST['email']
        description = request.POST["text"]


        if len(username) < 3:
            return HttpResponse("This is parol short from 3, >>>")
        else:

            new_user = SendMessage(name = username, email = email, description = description)
            new_user.save()
    return render(request, 'index.html')
