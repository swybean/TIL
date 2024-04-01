from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import User
# 2번 라인 User를 써도 결과는 똑같은데 아래 get_user_model을 사용하는 이유
# User 모델이 이름이 바뀌거나, 어떤 사유로 바뀌는 경우 User를 직접 참조하고 있는
# 위치마다 다 바꿔줘야 한다.
# 그런데 아래 get_user_modle을 사용하면 바꿔주지 않아도 알아서
# 활성화된 User 객체를 찾아서 반환해주기 때문에 => 직접 바꿔줄 수고를 없애준다.
# django에서도 위 방법을 지양하고 아래 방법을 사용하는 것을 권장하고 있다.
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # get_user_model: 현재 django 프로젝트에 활성화된 User 객체를 반환하는 함수
        model = get_user_model()

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email',)


