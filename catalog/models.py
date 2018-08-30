from django.db import models
from django.utils import timezone
# Create your models here.


class Post(models.Model): # 글 작성 모델 제작 # db에 저장될 형태??
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) # auth.User 데이블의 user 목록을 참조한다.
    title = models.CharField(max_length=200) # 글 작성 공간 할당
    text = models.TextField()

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self): ## 글 배포 메소드 설정
        self.published_date = timezone.now()
        self.save()

    def __str__(self): # 타이틀 string 추출 메소드
        return self.title

class Person(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)