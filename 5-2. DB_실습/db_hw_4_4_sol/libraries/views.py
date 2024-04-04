from django.shortcuts import render, redirect
from .models import Book, Review
from .forms import ReviewForm

# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'libraries/index.html', context)

def detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    reviews = Review.objects.all()
    review_form = ReviewForm()
    context = {
        'book': book,
        'review_form': review_form,
        'reviews': reviews,
    }

    return render(request, 'libraries/detail.html', context)


def review_create(request, pk):
    book = Book.objects.get(pk=pk)
    reviews = book.review_set.all()
    review_form = ReviewForm(request.POST)

    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.book = book
        review.user = request.user
        review.save()
        return redirect('libraries:detail', book.pk)
    context = {
        'review_from': review_form,
        'book': book,
        'reviews': reviews,
    }
    return render(request, 'libraries/detail.html', context)


def review_delete(request, book_pk, review_pk):
    # review 변수에 = ORM   ==>   # SELECT * FROM reviews WHERE pk = 1
    review = Review.objects.get(pk=review_pk) 
    #  요청한 사용자와 리뷰 작성자가 동일하면 
    if request.user == review.user:
        review.delete()  # 해당 리뷰를 삭제한다.
    return redirect('libraries:detail', book_pk)




