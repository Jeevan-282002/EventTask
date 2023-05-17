from django.urls import path
from . import views



urlpatterns = [
    
    path('',views.Home_view,name='home'),
    path("userlogin", views.userlogin_view, name = "userlogin"),
    path('register/', views.register, name='register'),
    path('signout/',views.signout_view , name = 'signout'),
    path("addevent/", views.addevent, name = "addevent" ),
    
]