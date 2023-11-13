

from django.http import JsonResponse
from django.views import View
import openai

openai.api_key = "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"

class Mybot(View):
    
    def my_chat_ai(self, prompt):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        message = response.choices[0].text.strip()
        return message

    def post(self, request):
        prompt = request.POST.get('text')
        response = self.my_chat_ai(prompt)
        return JsonResponse({'text': response})





# from django.shortcuts import render

# # Create your views here.

# from django.views import View
# from django.shortcuts import render
# from django.http import JsonResponse
# import openai

# openai.api_key = "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"





# class Mybot(View):
    
#     def my_chat_ai(self, prompt):
#         response = openai.Completion.create(
#             engine="text-davinci-002",
#             prompt=prompt,
#             max_tokens=1024,
#             n=1,
#             stop=None,
#             temperature=0.5,
#         )
#         message = response.choices[0].text.strip()
#         return message

#     def chat(request, self):
#         if request.method == 'POST':
#             prompt = request.POST.get('text')
#             response = self.my_chat_ai(prompt)
#             return JsonResponse({'text': response})
#         else:
#             return JsonResponse({'error': 'Invalid request method'})
