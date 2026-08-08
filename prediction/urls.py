from django.urls import path
from . import views

app_name = 'prediction'
urlpatterns = [
    path('', views.predict_view, name='predict'),
    path('result/<int:pk>/', views.result_view, name='result'),
    path('history/', views.history_view, name='history'),
]
