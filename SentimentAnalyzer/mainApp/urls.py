
from django.urls import path
from mainApp import views
urlpatterns = [
    path('', views.DetailView.as_view()),
    path('classification/',views.CreateView.as_view()),
    path('check/',views.PolarityCheckView.as_view()),
    path('users/', views.UserView.as_view())


]
