from django.urls import path
from tracker.views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),

    path('profile/_add', profile_add, name='profile_add'),
    path('profile_list/', profile_list, name='profile_list'),
    path('profile_update/', profile_update, name='profile_update'),
    path('profile_delete/', profile_delete, name='profile_delete'),

    path('calorie_consume_list/', calorie_consume_list, name='calorie_consume_list'),
    path('calorie_consume_add/', calorie_consume_add, name='calorie_consume_add'),
    path('calorie_consume_update/', calorie_consume_update, name='calorie_consume_update'),
    path('calorie_consume_delete/', calorie_consume_delete, name='calorie_consume_delete'),
]