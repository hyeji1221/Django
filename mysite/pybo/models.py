from django.db import models

# Create your models here.

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Answer(models.Model):
    # 기존 모델을 속성으로 연결하기 위해 ForeignKey 이용 -> 기존 모델을 속성으로 연결하기 위해 사용
    # on_delete=models.CASCADE는 이 답변과 연결된 질문이 삭제될 경우 답변도 함께 삭제
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()