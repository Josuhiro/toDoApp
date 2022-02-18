from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('edytuj/<str:pk>', views.update, name='update'),
    path('usun/<str:pk>', views.delete, name='delete'),

]
