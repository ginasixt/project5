from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path("group_detail/<int:id>/", views.group_detail, name="group_detail"),
    path('create_group/', views.create_group, name='create_group'),
    path('create_activity/', views.create_activity, name='create_activity'),

]