from django.db import models
from django.conf import settings

# Create your models here.

class Movie(models.Model):
    GENRE_CHOICES = [
        ('Action', '액션'),
        ('Comedy', '코미디'),
        ('Drama', '드라마'),
        ('Romance', '로맨스'),
        ('Thriller', '스릴러'),
        ('Horror', '공포'),
        ('Sci-fi', '과학 소설'),
        ('민수형', '멋진 근육맨'),
        # 원하는 장르를 추가할 수 있습니다.
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    # image = models.ImageField(blank=True, upload_to='movies/')
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    # score = models.FloatField()
    score = models.DecimalField(max_digits=2, decimal_places=1, choices=[(x / 2, str(x / 2)) for x in range(11)])

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)



