from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search_items, name='search_items'),
    path('incremental_search/', views.incremental_search, name='incremental_search'),
    path('admin_dashboard/', views.contact, name='admin_dashboard'),
    path('user_dashboard/', views.contact, name='user_dashboard'),
]