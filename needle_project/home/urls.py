from django.urls import path
from home import views
from home.views import UserPostView,CreatePostView,DetailView,UserAboutView,DeletePostView,UpdatePostView

urlpatterns = [
    path('', views.index, name='home'),
    path('createpost/',CreatePostView.as_view(), name='createpost'),
    path('post/<int:pk>/update', UpdatePostView.as_view(), name='updatepost'),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name='deletepost'),
    path('<str:username>/about/', UserAboutView.as_view(), name='about'),
    path('<str:username>/post/<int:pk>/', DetailView.as_view(), name='detailpost'),
    path('<str:username>/', UserPostView.as_view(), name='userpost'),

]