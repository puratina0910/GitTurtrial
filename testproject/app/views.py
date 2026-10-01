from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
 
def index(request):
    username = "puratina"

    context = {"username": username}

    return render(request, "app/index.html", context =context)

    def mypage(request):
        return render(request,"app/mypage.html")