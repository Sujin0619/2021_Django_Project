from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse
from .models import Post
from .forms import PostForm


# Create your views here.
# html 파일 이름은 '소문자 모델명'_list,'소문자 모델명'_detail, '소문자 모델명'_form, '소문자 모델명'_confirm_delete로 설정할 것 
def index(request):
    return redirect('post-list')


class PostListView(ListView):
    model = Post
    ordering = ['-dt_created']
    paginate_by = 6


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.id})


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.id})


class PostDeleteView(DeleteView):
    model = Post

    def get_success_url(self):
        return reverse('post-list')
