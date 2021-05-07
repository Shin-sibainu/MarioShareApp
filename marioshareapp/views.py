from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import MarioShareModel
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator


def landingfunc(request):
    return render(request, 'landing.html', {})

# サインアップ機能を実装
def signupfunc(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            return redirect('login')
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'そのユーザーはすでに登録されています。'})
    return render(request, 'signup.html', {})


def loginfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        # もし、認証バッグエンドでNoneが返されなかったら（ユーザーが存在したら）
        if user is not None:
            login(request, user)
            return redirect('public')
        else:
            return render(request, 'login.html', {'error': 'そのユーザーは存在しません。'})
    return render(request, 'login.html', {})

def logoutfunc(request):
    logout(request)
    return redirect('login')


def publicfunc(request):
    object_list = MarioShareModel.objects.all().order_by("-id")
    paginator = Paginator(object_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'public.html', {'object_list':object_list, 'page_obj': page_obj})

def mypagefunc(request, user_id):
    object_list = MarioShareModel.objects.all().order_by("-id")
    paginator = Paginator(object_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # Userオブジェクトはイテラブルじゃないよ！ってエラー吐かれてる。
    # ユーザーオブジェクトをfor文で出しても意味がない。
    # user = get_object_or_404(User, pk=user_id)
    # contributerと現在ログインしているUserが同じであれば、そのUserが投稿したデータをリストで取得する
    # print(MarioShareModel.objects.values_list('contributer', flat=True))
    # object_list = request.user
    return render(request, 'mypage.html', {'object_list': object_list, 'page_obj': page_obj})

def detailfunc(request, pk):
    object = get_object_or_404(MarioShareModel, pk=pk)
    return render(request, 'detail.html',{'object': object})

def goodfunc(request, pk):
    object = MarioShareModel.objects.get(pk=pk)
    # 後でいいねできる数を制限しておきたい。
    object.good += 1
    object.save()
    return redirect('public')

class shareview(CreateView):
    template_name = 'share.html'
    model = MarioShareModel
    fields = ('coursetitle', 'coursemaker', 'courseid', 'courseimage', 'coursevideo', 'comment', 'contributer') 
    def get_success_url(self):
        return reverse('public')

class postdeleteview(DeleteView):
    template_name = 'delete.html'
    model = MarioShareModel
    def get_success_url(self):
        return reverse('public')

class updateview(UpdateView):
    template_name = 'update.html'
    model = MarioShareModel
    fields = ('coursetitle', 'coursemaker', 'courseid', 'courseimage', 'coursevideo', 'comment', 'contributer') 
    def get_success_url(self):
        return reverse('public')
