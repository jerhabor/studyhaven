from django.db import models


class TutoringRate(models.Model):

    subject = models.CharField(max_length=254, null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.subject
