from django.urls import path
from .import views 
urlpatterns =[
    path('register/',views.register,name='register'),
    path('',views.login_user,name='signin'),
    path('home/',views.home,name='home'),
    path('logout/',views.logout_user,name='logout'),
    path('update/',views.userupdate,name='update_user'),
    path('ajax/register/',views.check_user_register,name='check_user_register'),
    path('ajax/login/',views.check_user_login,name='check_user_login'),

]