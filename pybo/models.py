from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    # User모델(회원가입 데이터 저장에 사용함)을 외래키로 적용해 선언.
    # + 계정이 삭제되면 이 계정이 작성한 질문 모두 삭제(CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_quesiton')
    #글자 수 길이 제한된 텍스트는 CharField 사용.
    subject = models.CharField(max_length=200)
    #길이 제한 없는 건 TextField
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null = True, blank = True)
    # blank=True: form.is_valid()를 통한 입력 데이터 검증 시 값이 없어도 됨.
    voter = models.ManyToManyField(User, related_name='voter_quesiton') # 다대다

    def __str__(self): #django shell에서 Question.objects.all()하면 이게 반환됨.
        return self.subject

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    #CASCADE 옵션은 질문을 삭제하면 그에 딸린 애들까지 모두 삭제되게 함.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null = True, blank = True)
    voter = models.ManyToManyField(User, related_name='voter_answer')