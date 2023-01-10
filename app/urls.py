from django.urls import path
from . import views

app_name = "app"
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('addtask', views.addtask, name='addtask'),
    path('taskdetails', views.taskdetails, name='taskdetails')
]