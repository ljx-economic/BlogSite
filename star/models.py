from django.db import models
from django.contrib.auth.models import User
from blog.models import Blog

# Create your models here.
class Star(models.Model):
    name=models.CharField(max_length=100,verbose_name='收藏夹')
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name='用户')
    brief=models.TextField(null=True,blank=True,verbose_name='摘要')
    blogs=models.ManyToManyField(Blog,null=True,blank=True,verbose_name='收藏的博客')
    created_time=models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    last_update_time=models.DateTimeField(auto_now=True,verbose_name='上次更新时间')
    def __str__(self):
        return self.name
        
    class Meta:
        ordering=['-created_time']
        verbose_name='收藏'
        verbose_name_plural=verbose_name