from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to='%Y/%m/%d')
    # image는 기존 필드 사이에 작성해도 테이블에서 가장 우측에 생성
    # blank=True 쓰는 이유 : 이게 없으면 이미지 없이 게시글 쓸 때도 있기 때문
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    