
# Create your models here.



from django.db import models
from apps.users.models import RegisterModel


class TranslationHistory(models.Model):
    user = models.ForeignKey(RegisterModel, on_delete=models.CASCADE)
    source_text = models.TextField()
    target_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class TranslationCorrection(models.Model):
    history = models.ForeignKey(TranslationHistory, on_delete=models.CASCADE)
    correction_text = models.TextField()
