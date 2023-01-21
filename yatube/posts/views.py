from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from .models import Group, Post


@login_required
def index(request):
    posts = Post.objects.select_related(
        'author', 'group')[:settings.NUMBER_OF_POSTS]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


@login_required
def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:settings.NUMBER_OF_POSTS]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
