from django.shortcuts import render,redirect
from .forms import createPostForm
from accounts.models import useraccount

# Create your views here.
def homescreen_view(request):
    return render(request,"post/home.html")

def create_post_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    form = createPostForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        # author = useraccount.objects.filter(email=request.user.email).first()
        author = useraccount.objects.filter(email=request.user.email).first()
        obj.author = author
        # obj.save()
        form = createPostForm()
    context['form'] = form
    return render(request,"post/createPost.html",context)
