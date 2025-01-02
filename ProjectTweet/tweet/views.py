from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm , UserRegistationForm,UserCreationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.

def index(request):
    return render(request,'index.html')

def tweetList(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request,"tweetsList.html",{"tweets":tweets})
@login_required
def tweetCreate(request):
    if request.method=="POST":
        form = TweetForm(request.POST,request.FILES)
        if form.is_valid():
            tweet =form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("tweetList")
    else:
        form = TweetForm()
    return render(request,'tweetForm.html',{"form":form})
@login_required
def tweetEdit(request,tweetId):
    tweet = get_object_or_404(Tweet,pk=tweetId,user = request.user)
    if request.method == "POST":
        form = TweetForm(request.POST,request.FILES,instance=tweet)
        if form.is_valid():
            tweet =form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("tweetList")
    else:
        form = TweetForm(instance=tweet)
    return render(request,'tweetForm.html',{"form":form})
@login_required
def tweetDelete(request,tweetId):
    tweet = get_object_or_404(Tweet,pk=tweetId,user = request.user)
    
    if request.method =="POST":
        tweet.delete()
        return redirect("tweetList")
    return render(request,'tweetDelete.html',{"tweet":tweet})



def register(request):
    if request.method == "POST":
        form = UserRegistationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()
            login(request,user)
            return redirect("tweetList")
    else:
        form = UserRegistationForm()
        
    return render(request,'registration/register.html',{"form":form})