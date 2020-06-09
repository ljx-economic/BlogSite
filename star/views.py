from django.shortcuts import render,get_object_or_404,redirect,reverse
from .models import Star
from blog.models import Blog
from django.contrib.auth.models import User
from django.core.paginator import Paginator

# Create your views here.
def star_manage(request):
    user=User.objects.get(username=request.user.username)
    stars=Star.objects.filter(user=user)
    my_stars=[]
    for star in stars:
        star.blog_count=star.blogs.all().count()
        my_stars.append(star)
    
    context={}
    context['my_stars']=my_stars
    context['count']=stars.count()
    return render(request,'star_manage.html',context)
    
def star_add(request):# 新建收藏夹
    if request.method=='POST':
        star_name=request.POST.get('star','')
        star_brief=request.POST.get('brief','')
        user=User.objects.get(username=request.user.username)
        star=Star(name=star_name,brief=star_brief,user=user)# 开始增加收藏夹
        star.save()
        return redirect(reverse('star_manage'))
    context={}
    return render(request,'star_add.html',context)
    
def star_change(request,star_pk):# 编辑收藏夹
    if request.method=='POST':
        star_name=request.POST.get('star','')
        star_brief=request.POST.get('brief','')
        star=get_object_or_404(Star,pk=star_pk)
        if star.user.username==request.user.username:# 验证是否是本用户要编辑收藏夹
            star.name=star_name
            star.brief=star_brief
            star.save()
            return redirect(reverse('star_manage'))
    star=get_object_or_404(Star,pk=star_pk)
    if star.user.username==request.user.username:# 验证是否是本用户要编辑收藏夹
        context={}
        context['star']=star
        return render(request,'star_change.html',context)
        
def star_delete(request,star_pk):# 删除收藏夹
    star=get_object_or_404(Star,pk=star_pk)
    if star.user.username==request.user.username:# 验证是否是本用户要删除收藏夹
        star.delete()
    return redirect(reverse('star_manage'))

# 浏览收藏夹里的博客    
def star_blog_list(request,star_pk):
    # 获得my_stars
    user=User.objects.get(username=request.user.username)
    stars=Star.objects.filter(user=user)
    my_stars=[]
    for star in stars:
        star.blog_count=star.blogs.all().count()
        my_stars.append(star)
    # 获得star    
    star=get_object_or_404(Star,pk=star_pk)
    blogs_all_list=star.blogs.all()
    # 获得page_of_blogs
    page_num=request.GET.get('page',1)#获取页面参数(request.GET是字典)，page_num是字符串
    paginator=Paginator(blogs_all_list,5)#每5个进行分页
    page_of_blogs=paginator.get_page(page_num)
    
    context={}
    context['page_of_blogs']=page_of_blogs
    context['star']=star
    context['my_stars']=my_stars
    return render(request,'star_blog_list.html',context)
    
# 添加博客到收藏夹中
def star_blog(request,blog_pk):
    if request.method=='POST':
        star_pk=int(request.POST.get('star_id',''))
        blog=get_object_or_404(Blog,pk=blog_pk)
        star=get_object_or_404(Star,pk=star_pk)
        if star.user.username==request.user.username:# 验证是否是本用户要添加博客到收藏夹
            star.blogs.add(blog)
            star.save()
            return redirect(reverse('blog_detail',args=[blog_pk]))
    try:# 用户可能没登录
        user=User.objects.get(username=request.user.username)
    except:
        return redirect(reverse('login'))
    stars=Star.objects.filter(user=user)
    my_stars=[]
    for star in stars:
        star.blog_count=star.blogs.all().count()
        my_stars.append(star)
    
    context={}
    context['my_stars']=my_stars
    context['count']=stars.count()
    return render(request,'star_blog.html',context)
    
def star_cancel(request,blog_pk):# 取消收藏
    blog=get_object_or_404(Blog,pk=blog_pk)
    stars=blog.star_set.filter(user=request.user)# 获取这个博客被该用户的哪些收藏夹收藏
    for star in stars:
        star.blogs.remove(blog)
        star.save()
    return redirect(reverse('blog_detail',args=[blog_pk]))