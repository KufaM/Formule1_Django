from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('drivers/grouped/', views.driver_list_grouped, name='driver_list_grouped'),
    path('driver/<int:pk>/', views.driver_detail, name='driver_detail'),
    path('teams/', views.team_list, name='team_list'),
    path('tracks/', views.track_list, name='track_list'),
    path('track/new/', views.track_create, name='track_create'),
    path('track/edit/<int:pk>/', views.track_edit, name='track_edit'),
    path('track/delete/<int:pk>/', views.track_delete, name='track_delete'),
]
