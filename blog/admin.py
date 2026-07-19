from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin (admin.ModelAdmin):
    date_hierarchy = 'created_date'
    # fields = ('title', 'content')
    # exclude = ('title',)
    list_display = ('title','author', 'is_published', 'counted_views', 'created_date')
    # ordering = ['-created_date']
    search_fields = ['title']
    list_filter = ('is_published', 'created_date', 'author')
admin.site.register(Post, PostAdmin)
