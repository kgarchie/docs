from django.shortcuts import render, redirect
from .models import docs
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm
from django.contrib.auth.models import User


# Create your views here.

@login_required(login_url='app:login')
def index(request):
    doc_all = docs.objects.all()
    context = {
        'docs': doc_all
    }
    return render(request, 'index.html', context)


def doc(request, id):
    document = docs.objects.get(id=id)
    context = {
        'doc': document
    }
    return render(request, 'doc.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('app:index')
        else:
            context = {
                'errors': "User does not exist",
            }
            return render(request, 'login.html', context)
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('app:login')


def register(request):
    form = UserCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = form.save(commit=False)
            if user is not None:
                User.objects.create_user(username=username, email=email, password=password)
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('app:index')
    return render(request, 'register.html', {'form': form})


def add_doc(request):
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        docs.objects.create(title=title, text=text)
        return redirect('app:index')
    return render(request, 'add_doc.html')


def delete(request, id):
    document = docs.objects.get(id=id)
    document.delete()
    return redirect('app:index')
