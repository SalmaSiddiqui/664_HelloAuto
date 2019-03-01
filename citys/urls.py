from django.urls import path
from . import views
from django.views.generic import TemplateView

# https://docs.djangoproject.com/en/2.1/topics/http/urls/
urlpatterns = [
    path('', views.MainView.as_view(), name='citys'),
    path('main/create/', views.CityCreate.as_view(), name='city_create'),
    path('main/<int:pk>/update/', views.CityUpdate.as_view(), name='city_update'),
    path('main/<int:pk>/delete/', views.CityDelete.as_view(), name='city_delete'),
    path('lookup/', views.StateView.as_view(), name='state_list'),
    path('lookup/create/', views.StateCreate.as_view(), name='state_create'),
    path('lookup/<int:pk>/update/', views.StateUpdate.as_view(), name='state_update'),
    path('lookup/<int:pk>/delete/', views.StateDelete.as_view(), name='state_delete'),
]
