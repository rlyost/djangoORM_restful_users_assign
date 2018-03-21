from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from time import gmtime, strftime
from .models import User    

def index(request):
    return render(request, 'index.html', { "users": User.objects.all() })

def show(request, id):
    if id != "<id>":
        request.session['id'] = id
    return render(request, 'users/show.html', { 'user': User.objects.get(id=id) })

def new(request):
    return render(request, 'users/new.html')

def edit(request, id):
    return render(request, 'users/edit.html', { 'user': User.objects.get(id=id) })

def create(request):
    if request.method == "POST":
        User.objects.create(name=request.POST['name'], email=request.POST['email'])
        request.session['id'] = User.objects.last().id
    return redirect('ushow', id=request.session['id'])

def update(request):
    if request.method == "POST":
        change = User.objects.get(id=request.POST['id'])
        change.name = request.POST['name']
        change.email = request.POST['email']
        change.save()
        request.session['id'] = request.POST['id']
    return redirect('ushow', id=request.session['id'])

def destroy(request, id):
    destroyit = User.objects.get(id=id)
    destroyit.delete()
    return redirect('in')