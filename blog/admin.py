from django.contrib import admin
from .models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
class PostAdmin (SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    # fields = ('title', 'content')
    # exclude = ('title',)
    list_display = ('title','author', 'is_published', 'counted_views', 'login_require' , 'created_date')
    # ordering = ['-created_date']
    search_fields = ['title']
    list_filter = ('is_published', 'created_date', 'author')
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('post', 'approved', 'created_date')
    list_filter = ('approved', 'post')

admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category)