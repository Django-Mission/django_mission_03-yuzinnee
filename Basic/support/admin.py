from django.contrib import admin

from.models import Faq

@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_date','updated_date')

# 수정은 불가능하나 시간을 보이게 하려면 @admin.register()추가 후 readonly_field추가