from django.shortcuts import render

# Create your views here.
def homescreen_view(request):
    return render(request,"post/home.html")
