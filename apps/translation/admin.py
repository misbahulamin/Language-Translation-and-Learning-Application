from django.contrib import admin

# Register your models here.



from django.contrib import admin
from .models import TranslationHistory, TranslationCorrection

class TranslationHistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'source_text', 'target_text', 'timestamp']

class TranslationCorrectionAdmin(admin.ModelAdmin):
    list_display = ['history', 'correction_text']

admin.site.register(TranslationHistory, TranslationHistoryAdmin)
admin.site.register(TranslationCorrection, TranslationCorrectionAdmin)
