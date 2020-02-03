from django.shortcuts import render
from .models import Post


def index(request):
    postAll = Post.objects.all()
    return render(request, 'main/index.html', {'postAll':postAll})

def postdetail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'main/postdetail.html', {'post':post})