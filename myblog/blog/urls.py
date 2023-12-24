from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostView.as_view()),
    path('<int:pk>/', views.PostDetailView.as_view()),
    path('review/<int:pk>/', views.AddComment.as_view(), name = 'add_comment'),
]