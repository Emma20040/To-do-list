from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.todo_list, name='home'),
    path('create/', views.todo_create, name="create"),
    path('<str:pk>/details/', views.todo_details, name="details" ),
    path('<str:pk>/update/', views.todo_update, name='update'),
    path('<str:pk>/delete/', views.delete_todo, name='delete'),
    path('login/', views.login_view, name='login'),
    path('singup/', views.singup_view, name='singup'),
    path('logout/', views.logout_view, name='logout')
]
