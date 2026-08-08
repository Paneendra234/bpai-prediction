from django.urls import path
from . import views

app_name = 'diet'
urlpatterns = [
    path('', views.diet_list, name='list'),
    path('<int:pk>/', views.diet_detail, name='detail'),
]
