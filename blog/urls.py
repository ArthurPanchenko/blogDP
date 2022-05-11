from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPageView.as_view(), name='home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('like/<int:pk>/', views.LikeView, name='like'),
    path('delete/<int:pk>/', views.DeletePostView.as_view(), name='delete'),
    path('post/<int:pk>/review', views.AddReviewView.as_view(), name='add-review'),
]