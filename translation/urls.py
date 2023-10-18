



from django.urls import path
from .views import TranslateView

# app_name = 'translation'

urlpatterns = [
    path('translate/', TranslateView.as_view(), name='translate'),
    # path('history/', TranslationHistoryView.as_view(), name='history'),
]
