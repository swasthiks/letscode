from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Contact
from blog.models import Post


def home(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'home/home.html', context)


def about(request):
    messages.success(request, "Profile details updated.")
    return render(request, 'home/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if(len(name) < 2 or len(phone) < 10 or len(email) < 10 or len(content) < 4):
            messages.error(request, "Fill all details properly")
        else:
            contact = Contact(name=name, email=email,
                              phone=phone, content=content)
            contact.save()
            messages.success(request, "Thank you.Will connect soon")
    return render(request, 'home/contact.html')


def search(request):
    query = request.GET['query']
    if len(query) > 90:
        allPosts = Post.objects.none()
    # allPosts=Post.objects.all()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPostsAuthor = Post.objects.filter(author__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count() == 0:
        messages.warning(request, "Nosearch results found")
    params = {'allPosts': allPosts, "query": query}
    return render(request, 'home/search.html', params)


def handleSigup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if len(username) > 10:
            messages.warning(
                request, "Username should be less than 10 characters")
            return redirect('/')
        if not username.isalnum():
            messages.warning(
                request, "Username contain only alphanumeric character")
            return redirect('/')
        if pass1 != pass2:
            messages.warning(request, "Password Mismatch")
            return redirect('/')
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "User Created")
        return redirect('/')
    else:
        return HttpResponse('404 not found')


def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful")
            return redirect('/')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('/')
    else:
        return HttpResponse(f'<b><h1>404 not found</h1></b>')

def handleLogout(request):
    logout(request)
    messages.success(request, "Logout Successful")
    return redirect('/')
