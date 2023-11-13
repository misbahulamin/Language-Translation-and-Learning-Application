





from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.urls import reverse_lazy

class SignUpView(CreateView):
    # model = User
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('signup')
    
    def form_valid(self, form):
        
        form.save()
        return redirect('signup')
        
    
    
    
    
    
    
    
    
# from rest_framework import viewsets
# from .models import RegisterModel
# from .serializers import UserSerializer

# from django.shortcuts import render

# from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
# from rest_framework  import viewsets
# from . import models, serializers





# class SignUpView(viewsets.ModelViewSet):
    
#     queryset = models.RegisterModel.objects.all()
#     serializer_class = serializers.UserSerializer








class SignUpView(CreateView):
    # model = User
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('signup')
    
    def form_valid(self, form):
        
        form.save()
        return redirect('signup')