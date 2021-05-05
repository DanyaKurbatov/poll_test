from django.contrib import admin

from .models import Question, Choice, Poll, Result

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Poll)
admin.site.register(Result)

