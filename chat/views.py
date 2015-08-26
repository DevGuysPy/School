from .models import Message
from django.shortcuts import render
from django.contrib.auth.models import User


def chat(request):
    messages = reversed(Message.objects.all())
    users = User.objects.all()

    if request.method == "POST":
        messages_text = request.POST['text']
        Message.objects.create(author=request.user,
                               text=messages_text)

    ctx = {
        'messages': messages,
        'users': users,
    }

    return render(request, 'chat/chat.html', ctx)

