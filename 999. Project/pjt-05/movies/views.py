from django.shortcuts import render, redirect
from .models import Movie, Comment
from .forms import MovieForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:index')
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)
    

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    comment_form = CommentForm()
    
    
    comments = Comment.objects.filter(movie_id = pk)
    # print('ttttt: ',comments.query)
    # 위에 꺼나, 아래꺼 중에서 하나만 써도 나오긴한다.
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # comment_set을 사용하면 movie를 하나만 받아와도 되서 더 짧아진다.
    # 밑에꺼는 Comment를 import 하지 않아도 작동한다.
    movie_set = movie.comment_set.all()
    # print('movie_set: ', movie_set.query)
    
    
    
    context = {
        'movie': movie,
        'comment_form': comment_form,
        'comments': comments,
        'movie_set': movie_set,
    }
    return render(request, 'movies/detail.html', context)

@login_required
def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.user == movie.user:
        if request.method == 'POST':
            form = MovieForm(request.POST, instance=movie)
            if form.is_valid():
                form.save()
                return redirect('movies:detail', movie.pk)
        else:
            form = MovieForm(instance=movie)
    else:
        form = MovieForm(instance=movie)
    context = {
        'form': form,
        'movie': movie,
    }
    return render(request, 'movies/update.html', context)

@login_required
def delete(request, pk):
    movie = Movie.objects.get(pk=pk)

    if request.user == movie.user:
        movie.delete()
        return redirect('movies:index')

@login_required
def comment_create(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    comments = movie.comment_set.all()
    comment_form = CommentForm(request.POST)
    
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.movie = movie
        comment.user = request.user
        comment.save()
        return redirect('movies:detail', movie.pk)
    context = {
        'comment_form': comment_form,
        'movie': movie,
        'comments': comments,
    }
    return render(request, 'movies/detail.html', context)

@login_required
def comment_delete(request, movie_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    
    if request.user == comment.user:
        comment.delete()
    return redirect('movies:detail', movie_pk)
