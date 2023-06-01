from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from django.urls import reverse
from tweet_app.forms import AddTweetForms

def index(request):
    return render(request, "tweet_app/first.html")

def addtweet(request):
    if request.POST:
        nickname = request.POST["nickname"]
        message = request.POST["message"]
        models.tweet.objects.create(nickname=nickname, message=message)
        return redirect(reverse('tweet_app:listtweet'))
    else:
        return render(request, "tweet_app/addtweet.html")


def listtweet(request):
    all_tweet = models.tweet.objects.all()
    tweet_dic = {"tweets":all_tweet}
    return render(request, "tweet_app/listtweet.html", context=tweet_dic)

def AddTweetByForm(request):

    if request.POST:
        form = AddTweetForms(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data["nickname_input"]
            message = form.cleaned_data["message_input"]
            models.tweet.objects.create(nickname=nickname, message=message)
            return redirect(reverse('tweet_app:listtweet'))
        else:
            print("error in form")
            return render (request, "tweet_app/addtweetbyform.html", context={"form":form})
    else:
        form = AddTweetForms()
        return render (request, "tweet_app/addtweetbyform.html", context={"form":form})