from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
# Create your views here.
from django.views import generic
from .models import Post
from .forms import CommentForm
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

def Beforlogin(request):
    template = 'beforlogin.html'
    return render(request,template)

def Loadworkshop(request):
    template = 'workshop.html'
    return render(request,template)

def Loadchobit(request):
    template = 'chobit.html'
    return render(request,template)


def Loadmentormentee(request):
    template = 'mentormentee.html'
    return render(request,template)

def Loadprechobit(request):
    template = 'prechobit.html'
    return render(request,template)

def Loadtimmentor(request):
    template = 'timmentor.html'
    return render(request,template)

def Loadtimmentee(request):
    template = 'timmentee.html'
    return render(request,template)

def Loadtrangcanhan(request):
    template = 'trangcanhan.html'
    return render(request,template)

def Loadban(request):
    template = 'ban.html'
    return render(request,template)

def Loadtraodoi(request):
    template = 'traodoi.html'
    return render(request,template)

def Loadchiase(request):
    template = 'chiase.html'
    return render(request,template)
