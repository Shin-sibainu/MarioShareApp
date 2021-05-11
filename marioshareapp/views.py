from django.shortcuts import render, redirect, reverse, resolve_url
from urllib import parse
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from django.urls import reverse_lazy
from .models import MarioShareModel, CourseCategory
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
    # object_listは全データを取得し、投稿順と逆順で取得。
    object_list = MarioShareModel.objects.all().order_by("-post_date")
    # 逆順で取得したデータを6つまで取得。
    paginator = Paginator(object_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'public.html', context)

def mypagefunc(request, user_id):
    object_list = MarioShareModel.objects.all().order_by("-post_date")
    paginator = Paginator(object_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # Userオブジェクトはイテラブルじゃないよ！ってエラー吐かれてる。
    # ユーザーオブジェクトをfor文で出しても意味がない。
    # user = get_object_or_404(User, pk=user_id)
    # contributerと現在ログインしているUserが同じであれば、そのUserが投稿したデータをリストで取得する
    # print(MarioShareModel.objects.values_list('contributer', flat=True))
    # object_list = request.user
    context = {
        'object_list': object_list,
        'page_obj': page_obj
    }
    return render(request, 'mypage.html', context)

def detailfunc(request, pk):
    object = get_object_or_404(MarioShareModel, pk=pk)
    return render(request, 'detail.html',{'object': object})

def goodfunc(request, pk):
    object = MarioShareModel.objects.get(pk=pk)
    # 後でいいねできる数を制限しておきたい。
    object.good += 1
    object.save()

    #public_page = resolve_url('public')
    #referer_page = request.META.get('HTTP_REFERER') 
    #print(referer_page)
    #if referer_page:
    #    parse_result = parse.urlparse(referer_page)
    #    print(parse_result.netloc)
    #    print(request.get_host())
    #    print(referer_page)
    #    if request.get_host() == parse_result.path:
    #        return redirect(referer_page)
    #return redirect(referer_page)
    return redirect('public')

class shareview(CreateView):
    template_name = 'share.html'
    model = MarioShareModel
    fields = ('coursetitle', 'coursemaker', 'courseid', 'courseimage', 'coursevideo', 'coursecategory', 'comment', 'contributer')    
    def get_success_url(self):
        return reverse('public')

#def share_category(request):
#    category_list = CourseCategory.objects.all()
#    print("a")
#    print(category_list)
#    return render(request, 'public.html', {'category_list':category_list})

class postdeleteview(DeleteView):
    template_name = 'delete.html'
    model = MarioShareModel
    def get_success_url(self):
        return reverse('public')

class updateview(UpdateView):
    template_name = 'update.html'
    model = MarioShareModel
    fields = ('coursetitle', 'coursemaker', 'courseid', 'courseimage', 'coursevideo', 'coursecategory', 'comment', 'contributer') 
    def get_success_url(self):
        return reverse('public')

def category(request, category):
    the_object_list = MarioShareModel.objects.all()
    #print(the_object_list)
    #for the_category in the_object_list:
    #    print(the_category.coursecategory.name)
    #mariosharemodel = MarioShareModel.objects.filter(coursecategory=category)
    #return render(request, 'public.html', {'category': category, 'mariosharemodel': mariosharemodel})
    return render(request, 'category.html', {'the_object_list': the_object_list, 'category_name':category})

def sortfunc(request, sort):
    # goodが多い順にデータをとってきたい。
    good_sort_list = MarioShareModel.objects.all().order_by("-good")
    new_sort_list = MarioShareModel.objects.all().order_by("-post_date")
    print(sort)
    context ={
        'good_sort_list':good_sort_list,
        'new_sort_list':new_sort_list,
        #'sort_name':sort,
     }
    return render(request, 'sort.html', context)


