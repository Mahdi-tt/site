from django.urls import path 
from .views import *
from django.contrib.auth import views

app_name='account'

urlpatterns = [
    path('login/',login_user,name='login'),
    path('singup/',singup,name='singup'),
    path('logout/',logout_view,name='logout'),

    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
