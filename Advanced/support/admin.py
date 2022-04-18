from tabnanny import verbose
from django.contrib import admin

from.models import Inquiry, Answer

class AnswerInline(admin.StackedInline):    # TabularInline 가로정렬
    model = Answer
    extra = 5
    min_num = 1
    max_num = 5
    readonly_fields = ('created_date','updated_date')   # 수정은 못하지만 읽기 가능
@admin.register(Inquiry)
class InquiryModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_list', 'question', 'phone_number', 'inquiry_content', 'image','user_email')
    list_filter = ('category_list',)
    search_fields = ('id', 'question')
    search_help_text = '게시판 번호, 질문 검색이 가능합니다.'
    inlines = [AnswerInline]    # Answer주석 처리후 inlines=[]생성

# admin.site.register(Answer)
