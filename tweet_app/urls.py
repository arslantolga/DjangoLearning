from django.urls import path, include
from . import views

app_name = "tweet_app"

urlpatterns = [
    path('', views.index, name="index"),
    path('listtweet', views.listtweet, name="listtweet"),
    path('addtweet', views.addtweet, name="addtweet"),
    path('addtweetbyform', views.AddTweetByForm, name="addtweetbyform"),
]