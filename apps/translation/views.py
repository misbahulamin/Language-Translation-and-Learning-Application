from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect
from django.views import View
from deep_translator import GoogleTranslator

class TranslateView(View):
    template_name = 'translate.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        source_text = request.POST.get('source_text')
        target_language = request.POST.get('target_language')

        if source_text and target_language:
            translator = GoogleTranslator(source='auto', target=target_language)
            target_text = translator.translate(source_text, punctuate=False)
        else:
            target_text = "Translation not available. Please provide source text and select a target language."

        return render(request, self.template_name, {
            'source_text': source_text,
            'target_text': target_text
        })


class TranslationHistoryView(View):
    template_name = 'history.html'

    def get(self, request):
        history = TranslationHistory.objects.filter(user=request.user)
        return render(request, self.template_name, {'history': history})