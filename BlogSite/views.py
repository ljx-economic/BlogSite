from django.shortcuts import render,redirect
from blog.models import Blog
from django.core.paginator import Paginator
from django.db.models import Q
from userInfo.forms import LoginForm
from django.contrib import auth

def home(request):
    if request.method=='POST':
        login_form=LoginForm(request.POST)
        if login_form.is_valid():
            username=login_form.cleaned_data['username']
            password=login_form.cleaned_data['password']
            user=auth.authenticate(request,username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect(request.GET.get('from','/'))
            else:
                login_form.add_error(None,'用户名或密码不正确')
    else:
        login_form=LoginForm()
    context={}
    context['login_form']=login_form
    return render(request,'home.html',context)
    
def search(request):
    search_word=request.GET.get('wd','').strip()# 清除头和尾的空格字符
    search_blogs=Blog.objects.filter(Q(title__icontains=search_word) | Q(content__icontains=search_word))# 部分匹配，contains区分大小写，加i不区分
    
    # 分页
    page_num=request.GET.get('page',1)#获取页面参数(request.GET是字典)
    paginator=Paginator(search_blogs,5)#每3页进行分页
    page_of_blogs=paginator.get_page(page_num)#django特有的,错误就第一页
    
    context={}
    context['search_word']=search_word
    context['search_blogs']=search_blogs# 模板中没用到
    context['search_blogs_count']=search_blogs.count()
    context['page_of_blogs']=page_of_blogs
    return render(request,'search.html',context)