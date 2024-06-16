from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('create_group_page/', views.create_group_page, name='create_group_page'),
    path("group_detail/<int:group_id>/", views.group_detail, name="group_detail"),
    path('create_group/', views.create_group, name='create_group'),
    path('create_activity/', views.create_activity, name='create_activity'),
    path('join_group/<int:group_id>/', views.join_group, name='join_group'),
    path('leave_group/<int:group_id>/', views.leave_group, name='leave_group'),
    path('calendar_view/', views.calendar_view, name='calendar_view'),

]