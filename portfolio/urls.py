from django.urls import path
from portfolio import views
from .views import IndexView


app_name = 'portfolio'

urlpatterns = [
    
    path('', views.IndexView.as_view(), name='index'),
    
]