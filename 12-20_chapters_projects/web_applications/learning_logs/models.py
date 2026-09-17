from django.db import models

# Create your models here.

class Topic(models.Model):
    """The topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """Return a string representation of the model."""
        return str(self.text)


