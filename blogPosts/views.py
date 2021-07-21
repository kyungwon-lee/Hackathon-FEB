from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.conf.urls.static import static
from django.conf import settings
import os
#from .static.blogPosts.json.page_section_info 
import json 
#from .forms import PostForm


class Page_Sections:
    def __init__(self) :
        data_id = 0
        section = ""
        sub_section = []

    def setdata(self, data_id, section, sub_section) :
        self.data_id = data_id
        self.section = section
        self.sub_section = sub_section

    
# def index(request):
#     return render(request, 'blogPosts/home.html')


# def main(request): 
#     if request.method == 'GET' :
#         posts = Post.objects.all()
#         return render(request, 'blogPosts/main.html', {'posts': posts})  
#     elif request.method == 'POST':
#         section = request.POST['section']
#         title = request.POST['title']
#         brief_description = request.POST['brief_description']
#         image = request.FILES.get('image', False)
#         content = request.POST['content']
#         Post.objects.create(section = section, title = title, brief_description = brief_description, image = image,  content = content )
#         return redirect('blogPosts:main') 

def bring_section_data_form_json(id) :
    id = id - 1
    file_path = os.path.join(settings.STATIC_ROOT, 'blogPosts/json/page_section_info.json')
    mainPageInfo_json_data = open(file_path)
    mainPageInfo_data = json.load(mainPageInfo_json_data)
    data_id = mainPageInfo_data[id]['id']
    section = mainPageInfo_data[id]['section']
    sub_section = mainPageInfo_data[id]['subSection']
    sections = Page_Sections()
    sections.setdata(data_id, section, sub_section)
    return sections

def main(request, id) :
    sections = bring_section_data_form_json(id)
    if request.method == 'GET' :
        #posts = Post.objects.get(id = id)
        # print(posts)
        #print(sections.section)
        posts = Post.objects.filter(section=sections.section)
        #print(posts)        
        return render(request, 'blogPosts/main.html', {'sections': sections, 'posts': posts}) # 
    elif request.method == 'POST':
        section = sections.section
        sub_section = request.POST['sub_section']
        title = request.POST['title']
        brief_description = request.POST['brief_description']
        image = request.FILES.get('image', False)
        content = request.POST['content']
        Post.objects.create(section = section, sub_section = sub_section, title = title, brief_description = brief_description, image = image,  content = content )
        return redirect('blogPosts:main', id = id) 


# def mainPage(request) :
#     return render(request, 'blogPosts/main.html')


def home(request):
    return render(request, 'blogPosts/home.html')  

# def textPage(request, id):
#     post = Post.objects.get(id = id)
#     return render(request, 'blogPosts/textPage.html', {'post':post}) 
    
def new(request, id) :
    sections = bring_section_data_form_json(id)
    return render(request, 'blogPosts/newTextPage.html', {'sections': sections})

def show(request, id, rid) : ### 여기서 (request, id) 이 정보는 어디서 받아오고 있는가?
    post = Post.objects.get(id = rid)
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
    



