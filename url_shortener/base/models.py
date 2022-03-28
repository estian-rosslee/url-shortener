import textwrap
from django.db import models

class ShortenedURL(models.Model):
    url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'URL({self.short_code}): {textwrap.shorten(f"{self.url}", width=10, placeholder="...")}'

    class Meta:
        ordering = ['created_at']
