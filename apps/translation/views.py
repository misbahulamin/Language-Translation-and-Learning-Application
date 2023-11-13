from django.shortcuts import render

# Create your views here.


from googletrans import Translator
import speech_recognition as sr

from django.shortcuts import render, redirect
from django.views import View
from deep_translator import GoogleTranslator
#from playsound import playsound 
import speech_recognition as sr 
from googletrans import Translator 
from gtts import gTTS 
import os 
flag = 0




dic = ('afrikaans', 'af', 'albanian', 'sq',  
       'amharic', 'am', 'arabic', 'ar', 
       'armenian', 'hy', 'azerbaijani', 'az',  
       'basque', 'eu', 'belarusian', 'be', 
       'bengali', 'bn', 'bosnian', 'bs', 'bulgarian', 
       'bg', 'catalan', 'ca', 'cebuano', 
       'ceb', 'chichewa', 'ny', 'chinese (simplified)', 
       'zh-cn', 'chinese (traditional)', 
       'zh-tw', 'corsican', 'co', 'croatian', 'hr', 
       'czech', 'cs', 'danish', 'da', 'dutch', 
       'nl', 'english', 'en', 'esperanto', 'eo',  
       'estonian', 'et', 'filipino', 'tl', 'finnish', 
       'fi', 'french', 'fr', 'frisian', 'fy', 'galician', 
       'gl', 'georgian', 'ka', 'german', 
       'de', 'greek', 'el', 'gujarati', 'gu', 
       'haitian creole', 'ht', 'hausa', 'ha', 
       'hawaiian', 'haw', 'hebrew', 'he', 'hindi', 
       'hi', 'hmong', 'hmn', 'hungarian', 
       'hu', 'icelandic', 'is', 'igbo', 'ig', 'indonesian',  
       'id', 'irish', 'ga', 'italian', 
       'it', 'japanese', 'ja', 'javanese', 'jw', 
       'kannada', 'kn', 'kazakh', 'kk', 'khmer', 
       'km', 'korean', 'ko', 'kurdish (kurmanji)',  
       'ku', 'kyrgyz', 'ky', 'lao', 'lo', 
       'latin', 'la', 'latvian', 'lv', 'lithuanian', 
       'lt', 'luxembourgish', 'lb', 
       'macedonian', 'mk', 'malagasy', 'mg', 'malay', 
       'ms', 'malayalam', 'ml', 'maltese', 
       'mt', 'maori', 'mi', 'marathi', 'mr', 'mongolian', 
       'mn', 'myanmar (burmese)', 'my', 
       'nepali', 'ne', 'norwegian', 'no', 'odia', 'or', 
       'pashto', 'ps', 'persian', 'fa', 
       'polish', 'pl', 'portuguese', 'pt', 'punjabi',  
       'pa', 'romanian', 'ro', 'russian', 
       'ru', 'samoan', 'sm', 'scots gaelic', 'gd', 
       'serbian', 'sr', 'sesotho', 'st', 
       'shona', 'sn', 'sindhi', 'sd', 'sinhala', 'si', 
       'slovak', 'sk', 'slovenian', 'sl', 
       'somali', 'so', 'spanish', 'es', 'sundanese', 
       'su', 'swahili', 'sw', 'swedish', 
       'sv', 'tajik', 'tg', 'tamil', 'ta', 'telugu', 
       'te', 'thai', 'th', 'turkish', 
       'tr', 'ukrainian', 'uk', 'urdu', 'ur', 'uyghur', 
       'ug', 'uzbek',  'uz', 
       'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh', 
       'yiddish', 'yi', 'yoruba', 
       'yo', 'zulu', 'zu') 


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

        return render(request, self.template_name, { 'source_text': source_text, 'target_text': target_text } ) 
    
    
   

class VoiceToTextTranslateView(View):
    
    template_name = 'translate.html'
    
    
    def get(self, request):
        return render(request, self.template_name)
    
    
    def post(self, request):
        
        
        #query = request.POST.get('source_text')
        to_lang = request.POST.get('target_language')
        
        
        query = self.takecommand()

        if query == "None":
            
            return render(request, 'translate.html', {'source_text': 'Could not recognize speech'})

        #to_lang = self.destination_language()
    

        # while to_lang not in dic:
            
        #     return render(request, 'translate.html', {'source_text': 'Language not available'})

        #translator = Translator()
        translator = GoogleTranslator(source='auto', target=to_lang)
        #text_to_translate = translator.translate(query, dest=dic[dic.index(to_lang) + 1])
        text_to_translate = translator.translate(query,punctuate=False)
        text = text_to_translate.text

        return render(request, 'translate.html', {'source_text': query, 'target_text': text})



    def takecommand(self):
        
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening.....")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing.....")
            query = r.recognize_google(audio, language='en-in')
            print(f"The User said {query}\n")
        except Exception as e:
            print("say that again please.....")
            return "None"
        return query

    def destination_language(self):
        print("Enter the language in which you want to convert : Ex. Hindi, English, etc.")
        print()

        to_lang = self.takecommand()
        while to_lang == "None":
            to_lang = self.takecommand()

        to_lang = to_lang.lower()
        return to_lang

    
    
    
    
    
    # def takecommand(self):   
    #     r = sr.Recognizer() 
    #     with sr.Microphone() as source: 
    #         print("listening.....") 
    #         r.pause_threshold = 1
    #         audio = r.listen(source) 
  
    #     try: 
    #         print("Recognizing.....") 
    #         query = r.recognize_google(audio, language='en-in') 
    #         print(f"The User said {query}\n") 
    #     except Exception as e: 
    #         print("say that again please.....") 
    #         return "None"
    #     return query 
  
 
    # query = takecommand()
     
    # while (query == "None"): 
    #     query = takecommand() 
  
  
    # def destination_language(self): 
    #     print("Enter the language in which you want to convert : Ex. Hindi , English , etc.") 
    #     print() 
     
    #     to_lang = self.takecommand() 
    #     while (to_lang == "None"): 
    #         to_lang = self.takecommand() 
            
    #     to_lang = to_lang.lower() 
    #     return to_lang 
  
    # to_lang = destination_language() 
  
 
    # while(to_lang not in dic): 
    #     print("Language in which you are trying to convert is currently not available , please input some other language") 
    #     print() 
    #     to_lang = destination_language() 
  
    # to_lang = dic[dic.index(to_lang)+1] 
  
  

    # translator = Translator()
   
    # text_to_translate = translator.translate(query, dest=to_lang) 
  
    # text = text_to_translate.text 
 
    # speak = gTTS(text=text, lang=to_lang, slow=False) 
  
    # # speak.save("captured_voice.mp3") 
  

    # # playsound('captured_voice.mp3') 
    # # os.remove('captured_voice.mp3') 
  
    # print(text) 
    
    
    
    
    
         
    
# class VoiceToTextTranslateView(View):
#     template_name = 'voice_to_text_translate.html'

#     def get(self, request):
#         return render(request, self.template_name)

#     def post(self, request):
#         # Create an instance of the Recognizer class
#         recognizer = sr.Recognizer()

#         # Get the audio file from the form input
#         audio_file = request.FILES.get('audio_file')

#         if audio_file:
#             try:
#                 # Use the recognizer to convert audio to text
#                 with sr.AudioFile(audio_file) as source:
#                     audio_text = recognizer.record(source)
#                 source_text = recognizer.recognize_google(audio_text)

#                 target_language = request.POST.get('target_language')

#                 if source_text and target_language:
#                     translator = Translator()
#                     translation = translator.translate(source_text, src='auto', dest=target_language)
#                     target_text = translation.text
#                 else:
#                     target_text = "Translation not available. Please provide source text and select a target language."
#             except sr.UnknownValueError:
#                 source_text = "Could not understand the audio."
#                 target_text = ""
#             except sr.RequestError:
#                 source_text = "Could not request results; check your network connection."
#                 target_text = ""
#         else:
#             source_text = "No audio file provided."
#             target_text = ""

#         return render(request, self.template_name, {'source_text': source_text, 'target_text': target_text})



# class TranslationHistoryView(View):
#     template_name = 'history.html'

#     def get(self, request):
#         history = TranslationHistory.objects.filter(user=request.user)
#         return render(request, self.template_name, {'history': history})