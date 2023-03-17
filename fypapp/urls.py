from django.urls import URLPattern, path
from xml.dom.minidom import Document
from django.urls import include, path

from . import views

 
urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.Signup, name='signup'),
    path('contact', views.Contact_Us, name='contact'),
    path('blog', views.blog, name='blog'),
    path('login', views.Login, name='Login'),
    path('logout', views.Logout, name='Logout'),
    path('blogs/<slug:slug>', views.singleBlog, name='singleBlog'),
    path('result',views.GetWeatherResult,name='Weather_Result')
]

