from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def login(request):
    # 만약 인증된 사용자의 요청이라면 index로 보내기
    if request.user.is_authenticated:
        return redirect('movies:index')
    
    # 만약 요청이 POST라면
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # 유효성 검사를 해서 유효하다면
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('movies:index')
    # 요청이 POST 외 다른 것이라면
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('movies:index')


def signup(requset):
    # 만약 인증된(로그인한, 가입한) 사용자라면 index로 보내버리기
    if requset.user.is_authenticated:
        return redirect('movies:index')
    
    # 요청이 POST면
    if requset.method == 'POST':
        form = CustomUserCreationForm(requset.POST)
        # 유효성 검사를 통과한다면
        if form.is_valid():
            form.save()
            return redirect('movies:index')
        
    # POST 외 다른 요청이라면
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(requset, 'accounts/signup.html', context)

@login_required
def delete(request):
    # 삭제할 User를 조회할 필요 없다. 바로 삭제하면 된다.
    request.user.delete()
    auth_logout(request)
    return redirect('movies:index')

@login_required
def update(request):
    # 만약 요청이 POST라면
    if request.method == 'POST':
        # 사용자 정보를 수정하기 위한 폼을 제공
        # isinstance는 현재 로그인한 사용자의 정보를 폼에 기본값으로 채워넣는 역할
        form = CustomUserChangeForm(request.POST, instance=request.user)
        # 유효성 검사를 통과하면
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    # 요청이 POST 외 다른 요청이라면
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)

@login_required
def change_password(request, user_pk):
    if request.method == 'POST':
        # 첫번째 인자 user가 필수, 두번째 인자가 데이터
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('movies:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)


