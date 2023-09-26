from django import forms
from .models import Article


# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)

# 단순한 modelform의 문법
# 파이썬 문법이 아니유
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                'class': 'article-title my-title',
                'placeholder': '제목을 입력하세요',
            }
        )
    )

    # model 등록
    class Meta:
        model = Article
        fields = '__all__'
        # fields = ('title',)
        # exclude = ('title',)