from django.urls import path

from calculator.views import home, sobre

urlpatterns = [
    path('', home),
    path('sobre/', sobre),
]