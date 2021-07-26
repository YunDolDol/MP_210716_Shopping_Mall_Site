from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.utils import timezone
from account.models import User
from django.core.paginator import Paginator

# Create your views here.

def home (request) :
    shoppings = Shopping.objects.all()
    paginator = Paginator(shoppings, 3)
    page_number = request.GET.get('page')
    shoppings = paginator.get_page(page_number)

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

def search(request) :
    searchs = Shopping.objects.all()
    search_text = request.GET.get('search_text')
    if search_text:
        searchs = searchs.filter(title__icontains = search_text)
        return render(request, 'search.html', {'searchs': searchs})
    
    return render(request, 'search.html', {'searchs': searchs})

def order(request) :
    if request.method == 'POST' :

        return ##
    else :
        ordering = Shopping.objects.get(id = id)
        return render(request, 'order.html', )

## 21.07.26 18:36 
## 로그인 된 상태가 아니라면 주문하기을 눌렀을 때 로그인 페이지로 이동한다.
## 주문하기 버튼을 누르면 로그인 된 유저의 주문 내역에 기록된다.
## 요거 개발중이었음.
