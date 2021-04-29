from django.db import models


class Review(models.Model):

    name = models.CharField(max_length=254, null=False, blank=False)
    occupation = models.CharField(
        max_length=254, null=False, blank=False, default='')
    heading = models.CharField(max_length=254, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.occupation
