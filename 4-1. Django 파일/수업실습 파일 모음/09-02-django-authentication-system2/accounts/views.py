from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required



# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:index')


def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@login_required
def delete(request):
    # 삭제하고자하는 User를 조회 할 필요 없다.
    request.user.delete()
    auth_logout(request)    # 탈퇴 후 로그아웃까지해서 session까지 없애는 것. 단 순서 중요
    return redirect('articles:index')


@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
def change_password(request, user_pk):
    if request.method == 'POST':
        # PasswordChangeForm은 첫번째 인자 user가 필수이다 !!!!중요!!!!
        # 두번째 인자가 데이터다.
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # 아래 함수에서 받는 user 인자는 위에서 저장한 비밀번호가 변경된 user이다.
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        # PasswordChangeForm은 첫번째 인자 user가 필수이다 !!!!중요!!!!
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)
