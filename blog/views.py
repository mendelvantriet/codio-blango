import logging

from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect

from blog.forms import CommentForm
from blog.models import Post


logger = logging.getLogger(__name__)


#@csrf_protect # We need this because we disabled CsrfViewMiddleware, but we use a csrf_token in the view
def index(request):
    logger.critical('CRIT!')
    posts = Post.objects.filter(published_at__lte=timezone.now()).select_related("author")
    logger.debug("Got %d posts", len(posts))
    return render(request, "blog/index.html", {"posts": posts})

def post_detail(request, slug):

    post = get_object_or_404(Post, slug=slug)
    if request.user.is_active:
        if request.method == "POST":
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.content_object = post
                comment.creator = request.user
                comment.save()
                logger.info("Created comment on Post %d for user %s", post.pk, request.user)
                return redirect(request.path_info)
        else:
            comment_form = CommentForm()
    else:
        comment_form = None

    return render(request, "blog/post-detail.html", {"post": post, "comment_form": comment_form})

def post_table(request):
    return render(
        request,
        "blog/post-table.html",
        {"post_list_url": reverse("post-list")},
    )

def get_ip(request):
    from django.http import HttpResponse
    return HttpResponse(request.META['REMOTE_ADDR'])

def bootstrap(request):
    return render(request, "blog/bootstrap.html")
