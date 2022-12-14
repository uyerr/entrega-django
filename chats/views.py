from django.shortcuts import render, redirect
from django.views.generic import View
from .models import ThreadModel, MessageModel
from django.db.models import Q
from .forms import ThreadForm, MessageForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

# Create your views here.

class ListThreads(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        threads = ThreadModel.objects.filter(Q(user=request.user.id) | Q(receiver=request.user.id))
        
        context = {
            'threads': threads
        }
        
        return render(request, 'inbox.html', context)
    
class CreateThread(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = ThreadForm()
        
        context = {
            'form': form
        }

        return render(request, 'create_thread.html', context)
    
    def post(self, request, *args, **kwargs):
        form = ThreadForm(request.POST)
        
        username = request.POST.get('username')
        
        try:
            receiver = User.objects.get(username=username)
            if ThreadModel.objects.filter(user=request.user, receiver=receiver).exists():
                
                thread = ThreadModel.objects.filter(user=request.user, receiver=receiver)[0]
                return redirect('thread', pk=thread.pk)
            
            elif  ThreadModel.objects.filter(user=receiver, receiver=request.user).exists():
                
                thread = ThreadModel.objects.filter(user=receiver, receiver=request.user)[0]
                return redirect('thread', pk=thread.pk)
        
            if form.is_valid():
                thread = ThreadModel(
                    user=request.user, 
                    receiver=receiver
                )
                thread.save()

                return redirect('thread', pk=thread.pk)
        except:
            messages.error(request, 'El usuario no existe')
            return redirect('create_thread')
        
class ThreadView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        form = MessageForm()
        thread = ThreadModel.objects.get(pk=pk)
        
        message_list = MessageModel.objects.filter(thread__pk__contains=pk)
        context = {
            'thread': thread,
            'form': form,
            'message_list': message_list
        }
        
        return render(request, 'thread.html', context)
    
class CreateMessage(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        
        thread = ThreadModel.objects.get(pk=pk)
        
        if thread.receiver == request.user:
            receiver = thread.user
        else:
            receiver = thread.receiver
            
        message = MessageModel(
            thread=thread,
            sender_user=request.user,
            receiver_user=receiver,
            body=request.POST.get('message')  
        )
        
        message.save()
        return redirect('thread', pk=pk)