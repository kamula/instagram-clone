from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from .forms import registrationform,AccountAuthenticationForm

def registration_view(request):
    context = {}
    if request.POST:
        form = registrationform(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            account = authenticate(email=email,password=raw_password)
            login(request,account)
            return redirect("home")
        else:
            context['registrationform'] = form
    else:
        form = registrationform()
        context['registrationform'] = form
    return render(request,'account/register.html',context)

def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('home')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email,password = password)

            if user:
                login(request,user)
                return redirect('home')
def logout_view(request):
    logout(request)
    return redirect('home')
