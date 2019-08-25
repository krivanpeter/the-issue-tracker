from django.db import models


class Package(models.Model):
    # A piece of Feature
    title = models.TextField(max_length=60, default="")
    worth_upvotes = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.title
