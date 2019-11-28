from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('user_info/<int:id>/', views.user_info, name="user_info"),
    path('user_info/<int:id>/del', views.user_delete, name="user_delete"),
]
