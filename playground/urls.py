from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('hello/', views.say_hello),
    path('quer/', views.queries),
    path('orop/', views.or_operator)
]
