from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .models import userProfile, blog
from .forms import contactusForm, userProfileForm, userUpdateForm, userProfileUpdateForm, blogForm, blogEditForm
from django.contrib.auth.decorators import user_passes_test



def home(request):
    return render(request, 'home.html')


def contactus(request):
    form = contactusForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            form.save()
        messages.info(request,'Form submitted successfully')
        return redirect('contactus')
    else:
        return render(request, 'contactus.html', {'form': form})


def please_login(request):
    msg = "You need to be logged-in to view this page"
    messages.info(request, msg)
    return render(request, 'login.html')


def login(request):
    if request.user.is_authenticated:
        messages.info(request,'You are alredy logged in.')
        return redirect('profile')
    else:
        if request.method=='POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.info(request,'You are successfully logged in.')
                return redirect('/')
            else:
                messages.info(request,"Invalid username/password")
                return redirect('login')
        else:
            return render(request,"login.html")


@login_required
def profile (request):
    p_form      = userProfileForm(instance=request.user.userprofile)
    return render(request, 'profile.html', {'p_form': p_form})


@login_required
def editprofile(request):
    if request.method =='POST':
        u_form = userUpdateForm(request.POST or None, instance=request.user)
        p_form = userProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
        messages.info(request,'Your profile successfully saved.')
        return redirect('profile')
    else:
        u_form = userUpdateForm(instance=request.user)
        p_form = userProfileUpdateForm(instance=request.user.userprofile)
        return render(request, 'editprofile.html', {'u_form': u_form, 'p_form': p_form})


@login_required
def logout(request):
    auth.logout(request)
    messages.info(request,'You are successfully logged out.')
    return redirect('login')


def register(request):
    if request.user.is_authenticated:
        messages.info(request,'You are alredy registered.')
        return redirect('profile')
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_num = request.POST['phone_num']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username is not available')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email is alreday registered')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1,
                                      email=email, first_name=first_name, last_name=last_name)
                user.save()
                newuserProfile = userProfile(phone_num=phone_num, user=user)
                newuserProfile.save()
                messages.info(request,'Account created successfully.')
                return redirect('login')
        else:
            messages.info(request,'Password is not matching')
            return redirect('register')
    else:
        return render(request,"register.html")


@login_required
def createblog(request):
    form= blogForm(request.POST or None, request.FILES or None)
    uid = request.user.id
    if request.method=='POST':
        if form.is_valid():
           blog = form.save(commit=False)
           blog.user = request.user
           blog.save()
        messages.info(request,'Blog submitted successfully, it will show after published by admin')
        return redirect('/myblogs') 
    else:
        return render(request, 'createblog.html', {'form': form})



@login_required
def editblog(request, id):
    userblog = blog.objects.get(id=id)
    uid = request.user.id
    b_user = userblog.user_id
    if uid != b_user:
        messages.info(request,'You do not have permisson to edit this item')
        return redirect('/myblogs') 
    else:
        form= blogEditForm(request.POST or None, request.FILES or None, instance=userblog)
        if request.method=='POST':
            if form.is_valid():
                form.save()
            messages.info(request,'Blog edited successfully, it will show after published by admin')
            return redirect('/myblogs') 
        else:
            return render(request, 'editblog.html', {'form': form, 'userblog': userblog})


def blogs(request):
    blogs = blog.objects.all()
    return render(request,'blogs.html', {'blogs': blogs})


def blog_detail(request, id):
    blg = blog.objects.get(id=id)
    uid = request.user.id
    b_user = blg.user_id
    context = {
        'blg': blg,
        'uid': uid,
        'b_user': b_user
    }
    return render(request, 'blog.html', context)


def myblogs(request):
    blogs = blog.objects.filter(user_id=request.user.id)
    return render(request,'myblogs.html', {'blogs': blogs})


@user_passes_test(lambda u: u.is_superuser)
def publishb(request, id):
    bid = id
    blg = blog.objects.get(id=id)
    blg.status = 2
    blg.save()
    return redirect('/dashboard/blog/%s' %bid)


@user_passes_test(lambda u: u.is_superuser)
def unpublishb(request, id):
    bid = id
    blg = blog.objects.get(id=id)
    blg.status = 0
    blg.save()
    return redirect('/dashboard/blog/%s' %bid)


@user_passes_test(lambda u: u.is_superuser)
def deleteb(request, id):
    blg = blog.objects.get(id=id)
    blg.delete()
    return redirect('/dashboard/blogs')


@user_passes_test(lambda u: u.is_superuser)
def dblogs(request):
    blogs = blog.objects.all().order_by('-id')
    return render(request,'dashboard/blogs.html', {'blogs': blogs})


@user_passes_test(lambda u: u.is_superuser)
def dblog(request, id):
    blg = blog.objects.get(id=id)
    return render(request, 'dashboard/blog.html', {'blg': blg})

@user_passes_test(lambda u: u.is_superuser)
def addblog(request):
    form= blogForm(request.POST or None, request.FILES or None)
    if request.method=='POST':
        if form.is_valid():
           blog = form.save(commit=False)
           blog.user = request.user
           blog.status = 2
           blog.save()
        messages.info(request,'Blog submitted successfully')
        return redirect('/dashboard/blogs') 
    else:
        return render(request, 'dashboard/addblog.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def deditblog(request, id):
    blg = blog.objects.get(id=id)
    bid = id
    form= blogEditForm(request.POST or None, request.FILES or None, instance=blg)
    if request.method=='POST':
        if form.is_valid():
            form.save()
        messages.info(request,'Blog edited successfully')
        return redirect('/dashboard/blog/%s' % bid) 
    else:
        return render(request, 'dashboard/editblog.html', {'form': form, 'blg': blg})

@user_passes_test(lambda u: u.is_superuser)
def dashboard(request):
    blogs         = blog.objects.all().order_by('-id')[:5]
    context = {
    'blogs': blogs
    }
    return render(request, 'dashboard/dashboard.html', context)