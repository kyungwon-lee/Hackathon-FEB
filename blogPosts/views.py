from django.shortcuts import render, redirect
from .models import Post


def index(request):
    return render(request, 'blogPosts/home.html')

def main(request):
    return render(request, 'blogPosts/main.html')  

def home(request):
    return render(request, 'blogPosts/home.html')  

def textPage(request):
    posts = Post.objects.all()
    return render(request, 'blogPosts/textPage.html') 
    
def new(request) :
    return render(request, 'blogPosts/newTextPage.html')

def show(request, id) :
    post = Post.objects.get(id = id)
    return render(request, 'blogPosts/textPage.html', {'post':post})

def delete(request, id) :
    post = Post.objects.get(id = id)
    post.delete()
    return redirect('blogPosts:main')

def update(request, id) :
    if request.method == 'GET':
        post = Post.objects.get(id=id)
        return render(request, 'blogPosts/updateTextPage.html', {'post':post})
    elif request.method == 'POST':
        section = request.POST['section']
        title = request.POST['title']
        brief_description = request.POST['brief_description']
        content = request.POST['content']
        Post.objects.filter(id=id).update(section = section, title = title, brief_description = brief_description, content = content )
        return redirect('blogPosts:show', id=id)
    



def example(request):
    if request.method == 'GET' :
        posts = Post.objects.all()
        return render(request, 'blogPosts/example.html', {'posts': posts})  
    elif request.method == 'POST':
        section = request.POST['section']
        title = request.POST['title']
        brief_description = request.POST['brief_description']
        content = request.POST['content']
        Post.objects.create(section = section, title = title, brief_description = brief_description, content = content )
        return redirect('blogPosts:example') 







