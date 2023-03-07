from django.urls import path
from . import views

app_name = 'ckanAPI'
urlpatterns = [
    path('', views.IndexView.as_view(), name='avg_ecoli'),

]
