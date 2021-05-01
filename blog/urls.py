from django.conf.urls import url
from django.urls import path, re_path, include
from . import views


urlpatterns =[
    path('', views.home, name='home'),
    path('contactus', views.contactus, name='contactus'),

    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name="profile"),
    path('editprofile', views.editprofile, name="editprofile"),

    path('createblog', views.createblog, name='createblog'),
    path('editblog/<int:id>', views.editblog, name='editblog'),
    path('myblogs', views.myblogs, name='myblogs'),
    path('blog/<int:id>', views.blog_detail, name='blog_detail'),
    path('blogs', views.blogs, name='blogs'),

    path('dashboard', views.dashboard, name='dashboard'),
    path('dashboard/login', views.dlogin, name='dlogin'),
    path('dashboard/logout', views.dlogout, name='dlogout'),
    path('dashboard/blogs', views.dblogs, name='dblogs'),
    path('dashboard/blog/<int:id>', views.dblog, name='dblog'),
    path('dashboard/addblog', views.addblog, name='addblog'),
    path('dashboard/editblog/<int:id>', views.deditblog, name='deditblog'),

    path('publishb/<int:id>', views.publishb, name='publishb'),
    path('unpublishb/<int:id>', views.unpublishb, name='unpublishb'),
    path('deleteb/<int:id>', views.deleteb, name='deteleb')
]