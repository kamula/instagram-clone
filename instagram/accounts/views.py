from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from .forms import registrationform,AccountAuthenticationForm,Accountupdateform

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
            #redirect to login page after registration
            return redirect("login")
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
        #redirect to home page after login
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
    else:
        form = AccountAuthenticationForm()
    context['login_form'] = form
    return render(request,'account/login.html',context)


def logout_view(request):
    logout(request)
    #redirect to login view after logging out
    return redirect('login')

def account_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    context = {}

    if request.POST:
        form = Accountupdateform(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = Accountupdateform(
                initial={
                    "email":request.user.email,
                    "username":request.user.username
                }
            )
    context['account_form'] = form
    return render(request,'account/account.html',context)

def must_authenticate_view(request):
    return render(request,'account/must_authenticate.html',{})
