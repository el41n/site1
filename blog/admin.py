from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    # what to display in admin site
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    # filter options
    list_filter = ('status', 'created', 'publish', 'author')
    # searchable fields
    search_fields = ('title', 'body')
    # auto-filling slug with title
    prepopulated_fields = {'slug': ('title',)}
    # used for lookup widget not drop-down
    raw_id_fields = ('author',)
    # hierarchy under search
    date_hierarchy = 'publish'
    # default ordering
    ordering = ('status', 'publish')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
