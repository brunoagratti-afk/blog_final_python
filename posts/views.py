from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.shortcuts import render, get_object_or_404
from .models import Post


def lista_posts(request):
    posts = Post.objects.all().order_by("-fecha_creacion")

    return render(
        request,
        "posts/lista_posts.html",
        {
            "posts": posts
        }
    )

def lista_posts(request):
    posts = Post.objects.all().order_by("-fecha_creacion")

    return render(
        request,
        "posts/lista_posts.html",
        {
            "posts": posts
        }
    )


def detalle_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    return render(
        request,
        "posts/detalle_post.html",
        {
            "post": post
        }
    )
@login_required
def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()

            return redirect("lista_posts")
    else:
        form = PostForm()

    return render(
        request,
        "posts/crear_post.html",
        {
            "form": form
        }
    )

@login_required
def editar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.autor != request.user:
     return redirect("detalle_post", post_id=post.id)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return redirect("detalle_post", post_id=post.id)

    else:
        form = PostForm(instance=post)

    return render(
        request,
        "posts/editar_post.html",
        {
            "form": form,
            "post": post
        }
    )


@login_required
def eliminar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.autor != request.user:
     return redirect("detalle_post", post_id=post.id)

    if request.method == "POST":
        post.delete()
        return redirect("lista_posts")

    return render(
        request,
        "posts/eliminar_post.html",
        {
            "post": post
        }
    )