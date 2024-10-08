from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from datetime import datetime
from .filters import PostFilter
from .forms import PostForm
from django.urls import reverse_lazy


class PostsList(ListView):
   model = Post
   ordering = 'post_autor'
   template_name = 'sapp/posts.html'
   context_object_name = 'posts'
   paginate_by = 2

   def get_queryset(self):
      queryset = super().get_queryset()
      self.filterset = PostFilter(self.request.GET, queryset)
      return self.filterset.qs

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['filterset'] = self.filterset
      return context


class PostDetail(DetailView):
   model = Post
   template_name = 'sapp/post.html'
   context_object_name = 'post'

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['time_no2w'] = datetime.utcnow()
      return context


class PostCreate(LoginRequiredMixin, CreateView):
   raise_exception = True
   form_class = PostForm
   model = Post
   template_name = 'sapp/post_create.html'


class PostUpdate(LoginRequiredMixin, UpdateView):
   raise_exception = True
   form_class = PostForm
   model = Post
   template_name = 'sapp/post_update.html'


class PostDelete(LoginRequiredMixin, DeleteView):
   raise_exception = True
   model = Post
   template_name = 'sapp/post_delete.html'
   success_url = reverse_lazy('posts')
