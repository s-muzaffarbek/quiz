from django.urls import path

from .views import question, home, result_list, users_upload

urlpatterns = [
    path('', home, name='home'),
    path('quiz/<slug:slug>/', question, name='question'),
    path('result/', result_list, name='result_list'),
    path('users/', users_upload, name='users_upload'),
]