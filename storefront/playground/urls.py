from django.urls import path
from . import views

# URLconf
urlpatterns = [
    path('hello/', views.hello_world),
]