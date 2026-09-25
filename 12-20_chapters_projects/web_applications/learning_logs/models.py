from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    """The topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        """Return a string representation of the model."""
        return str(self.text)

class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self) -> str:
        """Return a simplet string representing the entry."""
        text = str(self.text)

        if len(text) >= 50:
            return f"{text[:50]}..."
        return text
