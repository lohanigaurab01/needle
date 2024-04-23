from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from home.models import Post,Like
from django.contrib.auth.models import User


@login_required(login_url="login")
def index(request):
    posts = Post.objects.all().order_by('-time')
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)


def like_post(request, username, post_id):
    post = get_object_or_404(Post, pk=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()
    else:
        like

    return redirect('detailpost', username=username, pk=post_id)



class UserAboutView(LoginRequiredMixin, ListView ):
    model=Post
    template_name='about.html'
    context_object_name='posts'

    def get_queryset(self):
        user=get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user)


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





