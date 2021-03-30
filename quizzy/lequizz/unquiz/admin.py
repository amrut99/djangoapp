from django.contrib import admin
from .models import Choice, Question, Quiz, Answer
# ...
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Answer)
# Register your models here.
