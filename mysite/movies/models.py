from django.db import models


# Create your models here.
class Moviedata(models.Model):
    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    # type is a key word, so just use typ instead
    typ = models.CharField(max_length=200, default='action')
    image = models.ImageField(upload_to='Images/', default='Images/default.jpg')

    def __str__(self):
        return self.name


