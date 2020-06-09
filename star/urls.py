from django.urls import path
from . import views

urlpatterns=[
    path('manage/',views.star_manage,name='star_manage'),
    path('add/',views.star_add,name='star_add'),
    path('change/<int:star_pk>',views.star_change,name='star_change'),
    path('delete/<int:star_pk>',views.star_delete,name='star_delete'),
    path('browse/<int:star_pk>',views.star_blog_list,name='star_blog_list'),
    path('blog/<int:blog_pk>',views.star_blog,name='star_blog'),
    path('cancel/<int:blog_pk>',views.star_cancel,name='star_cancel'),
]