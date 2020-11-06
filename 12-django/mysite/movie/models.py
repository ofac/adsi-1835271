from django.db import models
from django.utils.text import slugify

CATEGORY_CHOICES = (
    ('A', 'Action'),
    ('D', 'Drama'),
    ('C', 'Comedy'),
    ('R', 'Romance'),
    ('F', 'Fiction'),
)

LANGUAGE_CHOICES = (
    ('EN', 'English'),
    ('ES', 'Spanish'),
    ('GR', 'German'),
)

STATUS_CHOICES = (
    ('RA', 'Recently Added'),
    ('MW', 'Most Watched'),
    ('TR', 'Top Rated'),
)

# Create your models here.

class Movie(models.Model):
    title       = models.CharField(max_length=128)
    description = models.TextField(max_length=256)
    image       = models.ImageField(upload_to='movies')
    category    = models.CharField(choices=CATEGORY_CHOICES, max_length=1)
    language    = models.CharField(choices=LANGUAGE_CHOICES, max_length=2)
    status      = models.CharField(choices=STATUS_CHOICES, max_length=2)
    year        = models.DateField()
    views_count = models.IntegerField(default=0)
    trailer     = models.URLField(default='')
    slug        = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs)


    def __str__(self):
        return self.title