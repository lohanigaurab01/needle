from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from home.models import Post
from django.contrib.auth.models import User


@login_required(login_url="login")
def index(request):
    posts = Post.objects.all()
    context = {
               'posts': posts,
    
               }
    return render(request, 'index.html', context)

class UserAboutView(LoginRequiredMixin, ListView ):
    model=Post
    template_name='about.html'
    context_object_name='posts'

    def get_queryset(self):
        user=get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-time')


class UserPostView(LoginRequiredMixin, ListView ):
    model=Post
    template_name='profile.html'
    context_object_name='posts'
    

    def get_queryset(self):
        user=get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-time')

class DetailView(LoginRequiredMixin, DetailView):
    model=Post
    template_name='detailpost.html'
    context_object_name='posts'

    
class CreatePostView(LoginRequiredMixin, CreateView):
    model=Post
    template_name='createpost.html'
    fields=['content', 'image']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    
class UpdatePostView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model=Post
    template_name='updatepost.html'
    fields=['content', 'image']
    success_url=''
    
    
    def test_func(self):
        post = self.get_object()
        if post.author==self.request.user:
            return True
        else:
            return False

class DeletePostView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model=Post
    template_name='deletepost.html' 
    success_url='/'


    def test_func(self):
        post=self.get_object()
        if post.author==self.request.user:
            return True
        else:
            return False
        



    
        