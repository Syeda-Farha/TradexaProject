from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import post
from .forms import InputPosts

def home(request):
    return render(request, 'home.html')

def user(request):
    return render(request, 'user.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        error_message = None

        if (not firstname):
            error_message = "First Name Required !!"
        elif len(firstname) < 4:
            error_message = "First Name must be more than 4 characters!!"
        elif (not lastname):
            error_message = "Last Name Required !!"
        elif len(lastname) < 4:
            error_message = "Last Name must be more than 4 characters!!"
        elif (not username):
            error_message = "User Name Required !!"
        elif len(username) < 5:
            error_message = "Please Enter Valid Username!!"
        elif (not password):
            error_message = "Password is Required !!"
        elif len(password) < 5:
            error_message = "Password must be more than 5 characters!!"
        elif (not email):
            error_message = "Email is Required !!"
        elif len(email) < 5:
            error_message = "Please Enter Valid Email Id!!"
        elif User.objects.filter(email=email).exists():
            error_message = "Email Address is Already Registered!!"

        # saving
        if not error_message:
            user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email,
                                            password=password)
            user.save()
            print("user created")
            return redirect('/')
        return render(request, 'signup.html', {'error': error_message})
    else:

        return render(request, 'signup.html')


def login(request):
    error_message = None

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # validation

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/userinfo')
        else:
            error_message = "Invalid Username or Password!!"

    return render(request, 'login.html', {'error': error_message})


def inputposts(request,id):

    username = User.objects.get(id=id)
    print(username)

    if request.method == "POST":
        post_form = InputPosts(request.POST or None)
        if post_form.is_valid():
            title = request.POST.get('title')
            detail = request.POST.get('detail')
            post1 = post(user=username, title=title, detail=detail)
            post1.save()
            return HttpResponse("Thanks for your post")
    else:
        post_form=InputPosts()

    context= {'user': username,
              'post_form': post_form,}
    return render(request, 'inputposts.html', context)


def userposts(request):
    posts = None
    posts = post.objects.all()
    data = {}
    data['posts'] = posts

    print(post)

    return render(request, 'userposts.html', data)


def userinfo(request):
    return render(request, 'userinfo.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
