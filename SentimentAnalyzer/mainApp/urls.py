
from django.urls import path
from mainApp import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', views.DetailView.as_view()),
    path('classification/',views.CreateView.as_view()),
    path('check/',views.PolarityCheckView.as_view()),
    path('users/', views.UserView.as_view()),
    path('login/',views.Usercheck.as_view()),
    path('api/',TokenObtainPairView.as_view()),
    path('getUser/',views.getUserView.as_view())
]
