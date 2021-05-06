from django.db import models
from user.models import Account


class Poll(models.Model):
    title = models.CharField(max_length=128, unique=True)
    start_date = models.DateTimeField('date start')
    finish_date = models.DateTimeField('date finish')
    description = models.CharField(max_length=400)

    def __str__(self):
        return self.title


class Question(models.Model):
    QUESTION_TEXT = 'TEXT'
    QUESTION_ONE = 'ONECHOICE'
    QUESTION_MULTI = 'MULTICHOICE'

    choices = (
        (QUESTION_TEXT, 'QUESTION_TEXT'),
        (QUESTION_ONE, 'QUESTION_ONE'),
        (QUESTION_MULTI, 'QUESTION_MULTI'),
    )

    poll = models.ForeignKey('Poll', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=256)
    question_type = models.CharField(max_length=24, choices=choices, default=QUESTION_TEXT)


class Choice(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=256)


class Result(models.Model):
    poll = models.ForeignKey('Poll', on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    choice = models.ForeignKey('Choice', on_delete=models.CASCADE)
