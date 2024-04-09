from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comments = article.comment_set.all()
    comment_form = CommentForm()
    context = {
        'article': article,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        article.delete()
    return redirect('articles:index')


@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else: 
        return redirect('articles:index')
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)


@login_required
def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comments = article.comment_set.all()
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
        return redirect('articles:detail', article.pk)
    context = {
        'comment_form': comment_form,
        'article': article,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


@login_required
def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('articles:detail', article_pk)


@login_required
def likes(request, article_pk):
    # 어떤 게시글에 좋아요가 눌리는건지 조회를 해야 함
    article = Article.objects.get(pk=article_pk)
    
    # 유저 정보는 이미 request 안에 들어있기에 조회할 필요 없다.
    # 직관적이기 위해 일단 작성해본다고 강의에서 말씀하심
    # 좋아요를 요청하는 유저
    user = request.user
    
    # 해당 게시글에 좋아요를 누른 유저 목록에 현재 요청하는 유저가 있을 경우
    if user in article.liek_users.all():
        # 좋아요 취소
        article.liek_users.remove(user)
    else:
        # 좋아요 진행
        article.liek_users.add(user)
    return redirect('articles:index')
    
    # # 요청하는 유저가 좋아요를 누른 게시글 목록에 지금 좋아요를 요청하는 게시글이 있을 경우
    # # 유저 입장에서 보는 것
    # # 그런데 위에가 더 자연스러우니 위에껄 쓰기 
    # if article in user.liek_articles.all():
    #     user.liek_articles.remove(user0)
    # else:
    #     user.liek_articles.add(user)  