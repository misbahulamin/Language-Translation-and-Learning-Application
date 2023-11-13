



# from django.urls import path
# from .views import TranslateView

# # app_name = 'translation'

# urlpatterns = [
#     path('translate/', TranslateView.as_view(), name='translate'),
#     # path('history/', TranslationHistoryView.as_view(), name='history'),
# ]




from django.urls import path
from .views import TranslateView, VoiceToTextTranslateView

# app_name = 'translation'

urlpatterns = [
    
    path('translate/', TranslateView.as_view(), name='translate'),
    path('voice_translate/', VoiceToTextTranslateView.as_view(), name='voice_translate'),
    # Add other URL patterns as needed
    
]
