from django.db import models


class Article(models.Model):
    author = models.CharField(max_length=50, verbose_name='Author name', default='Anonymous')
    title = models.CharField(max_length=100, verbose_name='Article title')
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True, verbose_name='Publication date')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated date')

    def __str__(self):
        return f'{self.pk}. {self.title}: {self.author}'

    class Meta:
        db_table = 'articles'
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
