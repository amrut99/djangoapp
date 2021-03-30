from django.db import models
from userbyemail.models import MyUser
from datetime import datetime

class Quiz(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default = datetime.now())
    def __str__(self):
        return self.name

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    answer = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class TemporaryUser(models.Model):
    temp_username = models.CharField(max_length=20)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=False)

    class Meta:
        unique_together = ['temp_username', 'quiz']
    def __str__(self):
        return self.temp_username

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    participant = models.ForeignKey(TemporaryUser, on_delete=models.CASCADE)
    answer = models.IntegerField(default=0)
