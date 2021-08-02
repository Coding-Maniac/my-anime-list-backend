from django.db import models

# Create your models here.

STATUS_OF_ANIME = [
    ('towatch', 'To Watch'),
    ('ongoing', 'Ongoing'),
    ('completed', 'Completed'),
    ('dropped', 'Dropped'),
    ('onhold', 'On Hold'),
]

class Anime(models.Model):
    name = models.CharField(max_length=250)
    episodes = models.IntegerField()
    logo = models.CharField(max_length=250)
    airing = models.BooleanField(default = False)
    rating = models.DecimalField(max_digits=5, decimal_places=3)
    status = models.CharField(choices=STATUS_OF_ANIME,default='towatch', max_length=100)

    class Meta:
        ordering = ['rating']