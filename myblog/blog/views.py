from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post
from .form import CommentsForm

# Create your views here.



class PostView(View):
    '''вывод записей'''
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog/index.html', {'post_list' : posts})
    
class PostDetailView(View):
    '''отдельная страница записи'''
    def get(self, request, pk):
        post = Post.objects.get(id = pk)
        return render(request, 'blog/blog_detail.html', {'post' : post})


class AddComment(View):
    '''добавление комментария'''
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.post_id = pk
            form.save()
        return redirect(f'/{pk}')    