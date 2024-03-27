from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

# 과거 new 함수
# def new(request):
#     form = ArticleForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'articles/new.html', context)

# 과거 create 함수
# def create(request):
#     # title = request.POST.get('title')
#     # content = request.POST.get('content')
#     # article = Article(title=title, content=content)
#     # article.save()
#     form = ArticleForm(request.POST)
#     if form.is_valid(): # 유효성 검사 메서드
#         article = form.save()   # 저장하고 생성된 객체를 반환해야함
#         return redirect('articles:detail', article.pk)
    
#     # 유효성 검사를 통과하지 못한 경우도 처리해야 함
#     # (예를 들어 제목 10자제한인데, 100자를 넣은 경우)
#     context = {
#         'form': form,
#     }
#     return render(request, 'articles/new.html', context)
#     # render는 에러가 담긴 폼을 새로운 템플릿에 만들어서 응답을 하는 것
#     # 이유 : is_valid에 의해서 False로 평가되면 context문으로 내려가서
#     # 에러메시지를 포함된 form 객체를 넘겨주기 때문이다.

#     # return redirect('articles:new')
#     # redirect를 안쓰는 이유 : 이걸 쓰면 def new를 다시 하라고 시키기
#     # 때문에 에러메시지가 뜨지 않는다.
#     # 새로운 요청을 받아서 새로운 뷰함수(new)를 실행하는 것이기 때문이다.



# new + create한 함수 제작
def create(request):
    # 아래부분은 과거 create 함수 부분
    form = ArticleForm(request.POST)
    # 메서드가 POST면 이 부분을 실행
    if request.method == 'POST':
        # 만약 POST 통과했는데 유효성 불통과하면 73라인 context로 간다
        if form.is_valid():  
            article = form.save()   
            return redirect('articles:detail', article.pk)
    # 메서드가 "POST가 아닌 다른 모든 경우" 이 부분을 실행
    # 따라서 무조건 if문은 POST로 하기
    # 과거 new 함수 부분
    else:
        form = ArticleForm()
    
    context = {
        'form': form,   # 이 form은 is_valid를 통과 못했으니
                        # 에러메시지를 포함한 form이 된다.
    }
    return render(request, 'articles/create.html', context)




def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

# 과거 edit 함수
# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(instance=article)
#     context = {
#         'article': article,
#         'form': form,
#     }
#     return render(request, 'articles/edit.html', context)

# 과거 update 함수
# def update(request, pk):
#     # title = request.POST.get('title')
#     # content = request.POST.get('content')
#     # article.title = title
#     # article.content = content
#     # article.save()

#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(request.POST, instance=article)
#     # create와 update의 차이점!!!!!
#     # 위에 instance=article이 있어야 밑에 form.save()가 생성이 아닌
#     # 수정으로 인식하고 수정해준다. (없으면 생성해버림)
#     if form.is_valid():
#         form.save()
#         return redirect('articles:detail', article.pk)
#     context = {
#         'form': form,
#         'article': article,
#     }
#     return render(request, 'articles/edit.html', context)


# edit + updqte한 함수
# 이 함수가 나오는 구조를 이해하기!!!!!!!!!!!!!
# 한줄 한줄 왜 그런지 이유를 알고 사용해야한다!!!!!!!!!!!
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        # 아래 if부터 return까지는 과거 update 부분
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        # else문은 과거 edit 부분
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,       
    }
    return render(request, 'articles/edit.html', context)


'''
!!!!!!!!!!!!!!!!중요!!!!!!!!!!!!!!!!!!
복습할 때 CRUD 작성 순서

1번 : 메서드가 POST일때, 나머지 모든 경우를 나눠 쓰기
2번 : else문 코드부터 먼저 작성해야 한다!!!!!!!!
즉, else문 - if문 - 조건문 나오고 나서 context 등 순으로 작성하기

def creat(request):
    # 메서드가 POST인 경우
    if request.method == 'POST':
        pass
    # 메서드가 POST가 아닌 모든 경우 < 여기부터 작성해야 한다!!
    else:
        pass
'''