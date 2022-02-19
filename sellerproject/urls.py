"""sellerproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from taskapp import views as task_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', task_views.login_user, name="login"),
    path('logout/', task_views.logout_user, name="logoutuser"),
    path('signup/', task_views.signupuser, name="signupuser"),
    path('', task_views.home, name="home"),
    path('home/', task_views.home, name="home"),
    path('details/<int:client_id>',
         task_views.client_details, name="client_details"),
    path('create_task/', task_views.newtask, name="newtask"),
    path('complete_task/<int:task_id>',
         task_views.complete_task, name="complete_task"),
    path('edit_task/<int:task_id>', task_views.edit_task, name="edit_task"),
    path('delete_task/<int:task_id>', task_views.delete_task, name="delete_task"),
    path('all_pending/', task_views.all_pending_tasks, name="all_pending_tasks"),
    path('all_completed/', task_views.all_completed_tasks,
         name="all_completed_tasks"),
    path('clients/', task_views.view_clients, name="view_clients"),
    path('client_details/<int:client_id>',
         task_views.edit_client, name="edit_client"),
    path('delete_client/<int:client_id>',
         task_views.delete_client, name="delete_client"),


]
