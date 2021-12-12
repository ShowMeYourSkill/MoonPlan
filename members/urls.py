from django.urls import path
from . import views


urlpatterns = [
    path('login2/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    #path('login/?next=add_activity')

]