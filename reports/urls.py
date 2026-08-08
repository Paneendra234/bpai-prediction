from django.urls import path
from . import views

app_name = 'reports'
urlpatterns = [
    path('generate/<int:pk>/', views.generate_report, name='generate'),
]
