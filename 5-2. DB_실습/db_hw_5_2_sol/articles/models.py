# articles/models.py
from django.db import models
from django.conf import settings

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


##########################################################################
# 암기해야 하는것 : 모델에서만 settings.AUTH_USER_MODEL을 사용하고, 
# 그 외 .py(파일)에서는 get_user_model을 사용해야한다. (강력하게 이걸 사용해야 한다. 걍 이거 쓰기)
# get_user_model 은 아예 유저 모델을 반환하고 (함수여서 반환한다.)
# 어써유저모델은 문자열만 가지고 있다가, 필요할 때 그 문자열에 해당하는 앱의 모델을 찾아가서 그 때의 유저를 가지고 온다.
