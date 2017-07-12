from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)


class UserText(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()  # blank=False
    user = models.ForeignKey(User, related_name="texts", on_delete=models.CASCADE)
    year = models.IntegerField(null=True, blank = True)

    def __str__(self):
        return "Title: {}, text: {}".format(self.title, self.text)