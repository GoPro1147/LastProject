from django.urls import path
from . import views

app_name="movie_review"

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/<int:id>/', views.movie_select, name="movie_select"),
    path('movie/<int:id>/', views.movie_detail, name="movie_detail"),
    path('actor/<int:id>/', views.actor_detail, name="actor_detail"),
    path('<int:id>/create_review/', views.create_review, name="create_review"),
    path('<int:movie_id>/<int:review_id>/delete_review/', views.delete_review, name="delete_review"),
    path('<int:movie_id>/<int:review_id>/update_review/', views.update_review, name="update_review"),
    path('like/<int:id>/', views.like, name="like"),
    path('<int:id>/movie_update/', views.movie_update, name="movie_update"),
    path('<int:id>/movie_delete/', views.movie_delete, name="movie_delete"),
    path('movies/search/', views.search, name="search"),
    path('movies/show/<int:id>/', views.show, name="show"),
]