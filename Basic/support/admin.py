from django.contrib import admin

from.models import Faq

@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_date','updated_date')
    list_display = ('question', 'category_list', 'updated_date')
    list_filter = ('category_list',)
    search_fields = ('question',)
    search_help_text = '제목 검색이 가능합니다.'