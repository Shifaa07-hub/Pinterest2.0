from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name = 'home'),
    path('create/', views.createpin, name = 'create'),
    path('<int:pin_id>/edit/', views.editpin, name = 'edit'),
    path('<int:pin_id>/delete/', views.deletepin, name = 'delete'),
    path('profile/', views.profile, name = 'profile'),
    path('search/', views.search, name = 'search'),
    path('register/', views.register, name = 'register'),
]