from django.contrib import admin
from .models import Like, Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    #↓管理画面で見たい項目をここに書く。
    list_display = ('id', 'author', 'title', 'created_at')
    list_display_links = ('title',)
    ordering = ('-created_at',) # -（マイナス）　created_atの降順となる
    
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    #↓管理画面で見たい項目をここに書く。
    list_display = ('id', 'user', 'post')
    list_display_links = ('post',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
