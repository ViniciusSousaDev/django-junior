import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        """Verifica se a questão foi publicada nos últimos 1 dia."""
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def total_votes(self):
        """Retorna o total de votos da questão."""
        return sum(choice.votes for choice in self.choice_set.all())

    def has_votes(self):
        """Indica se a questão possui ao menos um voto."""
        return self.total_votes() > 0


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
