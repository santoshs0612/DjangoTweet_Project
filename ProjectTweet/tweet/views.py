from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404, redirect
# Create your views here.

def index(request):
    return render(request,'index.html')

def tweetList(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request,"tweetsList.html",{"tweets":tweets})

def tweetCreate(request):
    if request.method=="POST":
        form = TweetForm(request.POST,request.FILES)
        if form.is_vald():
            tweet =form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("tweetList")
    else:
        form = TweetForm()
    return render(request,'tweetForm.html',{"form":form})

def tweetEdit(request,tweetId):
    tweet = get_object_or_404(Tweet,pk=tweetId,user = request.user)
    if request.method == "POST":
        form = TweetForm(request.POST,request.FILES,instance=tweet)
        if form.is_vald():
            tweet =form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("tweetList")
    else:
        form = TweetForm(instance=tweet)
    return render(request,'tweetForm.html',{"form":form})
def tweetDelete(request,tweetId):
    tweet = get_object_or_404(Tweet,pk=tweetId,user = request.user)
    
    if request.method =="POST":
        tweet.delete()
        return redirect("tweetList")
    return render(request,'tweetDelete.html',{"tweet":tweet})