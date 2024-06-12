# from django.urls import path
# from . import views

# urlpatterns = [
#     path('home/',views.home,name='home'),

# ]
# app1/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
]
