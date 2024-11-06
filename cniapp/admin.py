from django.contrib import admin
from .models import Review
from django_summernote.admin import SummernoteModelAdmin
from .models import Movies


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on', )
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

admin.site.register(Movies)