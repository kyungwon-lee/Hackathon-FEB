from django.shortcuts import render, redirect
from .models import Post, Comment, LikeOrDislike, Editors
from django.http import JsonResponse
from datetime import datetime
from django.utils import timezone
from .models import Post
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.conf.urls.static import static
from django.conf import settings
from django.core import serializers
import os
import random
import json 

sections_dict = {"금융" : 1, "사랑" : 2, "운동" : 3, "취미" : 4, "학습" : 5, "전자기기" : 6, "어플리케이션" : 7, "기타": 8 }

class Page_Sections:
    def __init__(self) :
        data_id = 0
        section = ""
        sub_section = []
        photo_dir = ""

    def setdata(self, data_id, section, sub_section, photo_dir) :
        self.data_id = data_id
        self.section = section
        self.sub_section = sub_section
        self.photo_dir = photo_dir

def bring_section_data_form_json(id) :
    id = id - 1
    file_path = os.path.join(settings.STATIC_ROOT, 'blogPosts/json/page_section_info.json')
    mainPageInfo_json_data = open(file_path, encoding='UTF-8')
    mainPageInfo_data = json.load(mainPageInfo_json_data)
    data_id = mainPageInfo_data[id]['id']
    section = mainPageInfo_data[id]['section']
    sub_section = mainPageInfo_data[id]['subSection']
    photo_dir = mainPageInfo_data[id]['photo_dir']
    sections = Page_Sections()
    sections.setdata(data_id, section, sub_section, photo_dir)
    #print(sections.photo_dir)
    return sections

def main(request, id) :
    sections = bring_section_data_form_json(id)
    posts = Post.objects.all()
    titles = []
    categoryId = []
    rId = []
    section_posts = Post.objects.filter(section=sections.section)
    section_posts_inorder = sorted(section_posts, key=lambda x: x.get_total_like())
    section_posts_inorder_top_ten = section_posts_inorder[0:9]
    for post in posts:
        categoryId.append(sections_dict[post.section])
        rId.append(post.id)
        titles.append(post.title)
    if request.method == 'GET' :
        #posts = Post.objects.get(id = id)
        #print(posts)
        #print(sections.section)
        posts = Post.objects.filter(section=sections.section)
        #print(sections.photo_dir)        
        return render(request, 'blogPosts/main.html', {'sections': sections, 'posts': posts, 'section_posts_inorder_top_ten':section_posts_inorder_top_ten, 'titles' : titles, 'categoryId' : categoryId, 'rId' : rId}) # 
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
    posts = Post.objects.all()
    titles = []
    categoryId = []
    rId = []
    #print(posts)
    for post in posts:
        categoryId.append(sections_dict[post.section])
        rId.append(post.id)
        titles.append(post.title)
    return render(request, 'blogPosts/home.html', {'titles' : titles, 'categoryId' : categoryId, 'rId' : rId})  

def new(request, id) :
    sections = bring_section_data_form_json(id)
    return render(request, 'blogPosts/newTextPage.html', {'sections': sections})

def show(request, id, rid) : ### 여기서 (request, id) 이 정보는 어디서 받아오고 있는가?
    post = Post.objects.get(id = rid)
    sections = bring_section_data_form_json(id)
    comments = post.comment_set.all().order_by('-created_at')
    posts = Post.objects.all()

    titles = []
    categoryId = []
    rId = []
    for each in posts:
        categoryId.append(sections_dict[each.section])
        rId.append(each.id)
        titles.append(each.title) 

    interest_id = random.randrange(1,9)
    temp = list(sections_dict.keys())

    interest = temp[interest_id-1]
    if (request.user.is_authenticated):
        interest = request.user.profile.interest
        interest_id = sections_dict[interest]

    interest_posts = Post.objects.filter(section=interest)
    interest_posts_inorder = sorted(interest_posts, key=lambda x: x.get_total_like())
    interest_posts_inorder_top_ten = interest_posts_inorder[0:10]
    return render(request, 'blogPosts/textPage.html', {'post':post, 'id': id, 'sections':sections, 'comments':comments, 'titles':titles, 'categoryId' : categoryId, 'rId' : rId, 'interest_posts_inorder_top_ten' : interest_posts_inorder_top_ten, 'interest_id': interest_id})


def delete(request, id) :
    post = Post.objects.get(id = id)
    post.delete()
    return redirect('blogPosts:main')

    
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
     
class EditorView:
    def create(request, id):
        post = Post.objects.get(id=id)
        editor_list = post.editors_set.filter(user_id=request.user.id)
        Editors.objects.create(user=request.user, post=post)
        return redirect(request.META.get('HTTP_REFERER'))


class CommentView:
    def create(request, id, rid):
        if request.method == 'POST':
            content = request.POST['content']
            comment = Comment.objects.create(post_id=id, content=content, author=request.user)
            post = Post.objects.get(id=rid)
            KST = datetime.now()
            current_time = KST.strftime('%Y년 %m월 %d일 %H:%M %p'.encode('unicode-escape').decode()).encode().decode('unicode-escape')
            return JsonResponse({
                'commentId': comment.id,
                'commentCount': post.comment_set.count(),
                'createdTime': current_time,
                'author': request.user.profile.email,
                'author_profile' : request.user.profile.profile_image.url
            })
        else:
            return render(f'/mainPage/<int:id>/post/{int:rid}')
    
    def delete(request, id, rid, cid):
        post=Post.objects.get(id=rid)
        comment = Comment.objects.get(id=cid)
        comment.delete()
        return JsonResponse({
            'commentId':comment.id,
            'commentNum':post.comment_set.count()
        })

class LikeView:
    def create_like(request, id, rid):
        sections = bring_section_data_form_json(id)
        print(id)
        if request.method == 'POST':
            #mainPage_section = Sections.########################## 
            post = Post.objects.get(id=rid)
            flag = 0
            like_list = post.likeordislike_set.filter(user = request.user)
            # 이미 좋아요 / 싫어요를 누른 User
            if like_list.count() > 0:
                # 좋아요를 누른 User
                if post.likeordislike_set.get(user=request.user).like == True:
                    post.likeordislike_set.get(user = request.user).delete()
                # 싫어요를 누른 User
                else:
                    flag = 1
                    post.likeordislike_set.filter(user = request.user).update(like = True)
                    post.likeordislike_set.filter(user = request.user).update(dislike = False)
                    post.likeordislike_set.get(user = request.user).save()
            # 좋아요 / 싫어요 를 누르지 않은 User
            else:
                LikeOrDislike.objects.create(user=request.user, post=post, like = True, dislike = False)
            return JsonResponse({
                'postLikeOfUser': like_list.count(), 
                'flag' : flag,
                'voteTotalCount': post.like_dislike.count(),
                'voteLikeCount' : post.get_total_like()
            })
        else:
            return redirect (f'/mainPage/<int:id>/post/{int:rid}')
    
    def create_dislike(request, id, rid):
        if request.method == 'POST':
            post = Post.objects.get(id=rid)
            flag = 0
            like_list = post.likeordislike_set.filter(user = request.user)
            if like_list.count() > 0:
                # 좋아요를 누른 User
                if post.likeordislike_set.get(user=request.user).like == True:
                    flag = 1
                    post.likeordislike_set.filter(user = request.user).update(like = False)
                    post.likeordislike_set.filter(user = request.user).update(dislike = True)
                    post.likeordislike_set.get(user = request.user).save()
                # 싫어요를 누른 User
                else:
                    post.likeordislike_set.get(user = request.user).delete()
            else:
                LikeOrDislike.objects.create(user=request.user, post=post, like = False, dislike = True)
            # return redirect (f'/posts/{id}')
            return JsonResponse({
                'postLikeOfUser': like_list.count(), 
                'flag' : flag,
                'voteTotalCount': post.like_dislike.count(),
                'voteLikeCount' : post.get_total_like()
            })
        else:
            return redirect (f'/mainPage/<int:id>/post/{int:rid}')

class IframeView:
    def content(request, id) :
        post = Post.objects.get(id = id)
        return render(request, 'blogPosts/content.html', {'post':post})

    def update(request, id) :
        if request.method == 'GET':
            post = Post.objects.get(id=id)
            return render(request, 'blogPosts/updateTextPage.html', {'post':post})
        elif request.method == 'POST':
            #section = request.POST['section']
            #title = request.POST['title']
            #brief_description = request.POST['brief_description']
            post = Post.objects.get(id=id)
            Editors.objects.create(user=request.user, post=post)
            content = request.POST['content']
            content = content.replace("\r\n", "<br>")
            Post.objects.filter(id=id).update(content = content)#section = section, title = title, brief_description = brief_description, content = content )
            return redirect('blogPosts:content', id=id)

    def history(request, id) :
        post = Post.objects.get(id = id)
        editor_list = post.editors_set.all().order_by('-edited_at')
        final_list = editor_list
        editor_count = {}
        for editor in editor_list :
            if editor.user.profile.email in editor_count:
                editor_count[editor.user.profile.email] += 1
                final_list = final_list.exclude(edited_at = editor.edited_at)
            else :
                editor_count[editor.user.profile.email] = 1
        
        return render(request, 'blogPosts/history.html', {'post':post, 'editor_list': final_list, 'editor_count' : editor_count})
