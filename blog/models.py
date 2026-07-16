from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    # image
    # author
    # tag
    # category
    counted_views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)

    class Meta:
        ordering = ['-created_date']
        # verbose_name = 'تست'
        # verbose_name_plural = 'تست ها'

    def __str__(self):
        return self.title