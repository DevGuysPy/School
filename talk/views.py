from django.shortcuts import render
from django.http import HttpResponse
from talk.models import Post
from talk.forms import PostForm

import json


def home(request):

    ctx = {
        'all_posts': Post.objects.reverse(),
        'form': PostForm()
    }
    return render(request, 'talk/index.html', ctx)


# def create_post(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             return HttpResponseRedirect('/')
#     else:
#         form = PostForm()
#     return render(request, 'post.html', {'form': form})

def create_post(request):
    if request.method == 'POST':
        post_text = request.POST.get('the_post')
        response_data = {}

        post = Post(text=post_text, author=request.user)
        post.save()

        response_data['result'] = 'Create post successful!'
        response_data['text'] = post.text
        response_data['created'] = post.created.strftime('%b. %d, %Y, %H:%M:%S')
        response_data['author'] = post.author.student.name+' '+post.author.student.surname

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
