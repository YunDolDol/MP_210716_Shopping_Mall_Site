from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.utils import timezone
from account.models import User
# Create your views here.

def home (request) :

    shoppings = Shopping.objects.all()

    return render (request, 'home.html', {'shoppings':shoppings})

def make_post (request) :
    if request.method == 'POST' :
        new_item = Shopping()
        new_item.title = request.POST['title']
        new_item.image = request.FILES.get('image')
        new_item.body = request.POST['body']
        user_id = request.user.id
        user = User.objects.get(id = user_id)
        new_item.author = user
        new_item.save()
        return redirect('home')
    else:
        return render(request, 'new.html')

def detail (request, id) :
    shoppings = get_object_or_404(Shopping, pk = id)
    return render(request, 'detail.html', {'shopping':shoppings})

def update (request, id) :
    if request.method == 'POST' :
        update_item = Shopping.objects.get(id = id)
        update_item.title = request.POST['title']
        update_item.body = request.POST['body']
        update_item.save()
        return redirect('detail', update_item.id)
    else :
        shopping = Shopping.objects.get(id = id)
        return render(request, 'edit.html', {'shopping':shopping})

def delete (request, id) :
    delete_item = Shopping.objects.get(id = id)
    delete_item.delete()
    return redirect('home')

def order()