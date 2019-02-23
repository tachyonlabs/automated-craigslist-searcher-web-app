from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_results, name='search_results'),
    path(r'edit_search_settings', views.edit_search_settings, name='edit_search_settings'),
]
