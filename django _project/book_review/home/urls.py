from django.urls import path
from . import views

urlpatterns = [
    path('', views.home  ),
    path('browse_books/', views.browse_books)
]
