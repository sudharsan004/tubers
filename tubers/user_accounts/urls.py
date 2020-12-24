from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    # Django already has a build in logout method so give some other name to logout function
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
