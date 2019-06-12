from django.contrib import admin

# Register your models here.

from .models import Family, Member, MedicalRecord


class FamilyAdmin(admin.ModelAdmin):
    list_display = ('folder_number', 'address',)
    search_fields = ('folder_number', 'address',)
    list_filter = ('address', )


class MemberAdmin(admin.ModelAdmin):
    list_display = ('age','education', 'occupation', 'income', 'marital_status',
                    'immunization', 'remarks', 'family')
    search_fields = ('member_name','family__folder_number',)
    list_filter = ('family',)


class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('date', 'member', 'clinical_details', 'diagnosis')
    list_filter = ('member', )
    search_fields = ('date',)


admin.site.register(Family, FamilyAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(MedicalRecord, MedicalRecordAdmin)
