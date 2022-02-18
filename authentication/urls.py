from django.urls import path
from . import views
urlpatterns = [
    path('logowanie/', views.loginUser, name='login'),
    path('rejestracja/', views.registerUser, name='register'),
    path('wylogowanie/', views.logoutUser, name='logout'),

]
