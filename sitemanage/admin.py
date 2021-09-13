from django.contrib import admin
from .models import SiteConfig
from django.contrib.sites.models import Site

@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    #↓管理画面で見たい項目をここに書く。
    list_display = ('id', 'meta_title',)
    list_display_links = ('meta_title',)
    