from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from django.contrib import messages
from django.contrib.sessions.models import Session

# Create your views here.

def login(request):
    if request.session.has_key('is_log'):
        return redirect('home')
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email=email,  password=password).count()
        if user > 0:
            request.session['is_log'] = True
            request.session['user_id']= User.objects.values('id').filter(email=email,  password=password)[0]['id']
            return redirect('home')
        else:
            messages.error(request, 'invalid password or email')
            return redirect('login')
    return render(request, 'login.html')
def singup(request):
    return render(request, 'singup.html')
def newaccount(request):
    return render(request, 'newaccount.html')
def datainsert(request):
    if request.POST:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        obj = User(username=username, email=email, password=password)
        obj.save()
        messages.success(request, 'you are register successfully')
        return redirect('login')
    return render(request, 'signup.html')

def home(request):
    if request.session.has_key('is_log'):
       fetch_data= Blog.objects.all()
       return render(request, 'home.html', {'data':fetch_data})
    return redirect('login')

def logout(request):
    del request.session['is_log']
    return redirect('login')
def contact(request):
   # if request.session.has_key('is_log'):
   #     return redirect('contact')
  #  return redirect('login')
    if request.POST:
        name = request.POST['name']
        country = request.POST['country']
        subject = request.POST['subject']

        obj = Contant(name=name, country=country, subject=subject)
        obj.save()

        return redirect('home')
    return render(request, 'contact us.html')

def create(request):
    if request.POST:
        good_name = request.POST['good_name']
        discription = request.POST['discription']
        title = request.POST['title']
        image = request.FILES['image']
        user_id = request.session['user_id']
        obj = Blog(good_name=good_name,
                   discription= discription,
                   title=title,
                   image=image)
        obj.user_id_id = user_id
        obj.save()
        messages.success(request, 'your post is submitt')
        return redirect('home')
    return render(request, 'create_post.html')
def readmore(request, id):
    if request.POST:
        message = request.POST['message']
        user_id = request.POST['user_id']
        post_id = id
        query = Coment(message=message)
        query.post_id_id = post_id
        query.user_id_id = user_id
        query.save()
    data = Blog.objects.get(id=id)
    coment = Coment.objects.all().filter(post_id=id)
    return render(request, 'readmore.html', {'data':data, 'coment': coment})