from django import forms
from .models import Article

# forms.라는 모듈의 Form이라는 클래스를 상속 받는다.
# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)


# forms모듈의 ModelForm이라는 부모 클래스를 상속 받는다.
# 자동으로 models.py의 Article 클래스의 데이터를 자동으로 받아오기
# 위해서 ModelForm으로 만들어서 사용한다.
class ArticleForm(forms.ModelForm):
    class Meta:
        # 어떤 모델과 연동할지 정하는 것
        model = Article 
        # 그 모델에서 어떤 필드를 쓸지를 정하는 것
        fields = '__all__'  # 전체 필드를 받아온다.


