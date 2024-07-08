from django.urls import path
from aayush import views

app_name="aayush"

urlpatterns = [
    path("",views.home,name='home'),
    path("index",views.home,name='home'),
    path("blog",views.blog,name='blog'),
    path("about",views.about,name='about'),
    path("contact",views.contact,name='contact'),
]