
# from multiprocessing import context
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,DetailView,CreateView)
from django.shortcuts import render,HttpResponse
from .models import Post

# Create your views here.
# posts =[
#     {
#         'author':'CoreMs',
#         'title':'Blog post 1',
#         'content':'First post content',
#         'date_post':'August 27, 2018',
#     },
#     {
#         'author':'CoreMs',
#         'title':'Blog post 1',
#         'content':'First post content',
#         'date_post':'August 27, 2018',
#     }
# ]
def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)

##convert home view to class view
class PostListView(ListView):
    model= Post
    template_name='blog/home.html'
    context_object_name='posts'
    # ordering = ['-date_posted']
class PostDetailsView(DetailView):
    model= Post
    # ordering = ['-date_posted']

class PostCreateView(LoginRequiredMixin,CreateView):
    model= Post
    fields = ['title','content']

def about(request):
    # return HttpResponse('<h1>Hello I am about</h1>')
    return render(request,'blog/about.html',{'title':'about'})

def nothing(request):
    return render(request,'blog/nothing.html')
