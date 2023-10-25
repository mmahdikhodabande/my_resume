from django.contrib import admin
from jalali_date import datetime2jalali
from jalali_date.admin import TabularInlineJalaliMixin, ModelAdminJalaliMixin
from .models import Me, Work_samples, work_experience, Educational_records, interests, languages, Skills,Cyberspace


# Register your models here.
class User_visit(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['name', 'family_name', 'phone', 'gender']
    list_editable = ['gender']

    @admin.display(description='تاریخ ایجاد', ordering='created')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created).strftime('%a, %d %b %Y %H:%M:%S')


class date_persian(ModelAdminJalaliMixin, admin.ModelAdmin):
    @admin.display(description='تاریخ ایجاد', ordering='created')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created).strftime('%a, %d %b %Y %H:%M:%S')


admin.site.register(Me, User_visit)
admin.site.register(Work_samples)
admin.site.register(languages)
admin.site.register(Cyberspace)
admin.site.register(Skills)
admin.site.register(interests)
admin.site.register(work_experience, date_persian)
admin.site.register(Educational_records, date_persian)
