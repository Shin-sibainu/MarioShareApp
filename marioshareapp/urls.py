from django.contrib import admin
from django.urls import path, include
from .views import signupfunc, loginfunc, logoutfunc, publicfunc, mypagefunc, shareview, postdeleteview, detailfunc, updateview
from .views import category, mypagecategory, sortfunc, goodfunc, toppagefunc

#app_name = 'marioshareapp'

urlpatterns = [
  # 指定したviewにrequestオブジェクト渡している。
  path('', toppagefunc, name='toppage'),
  path('signup/', signupfunc, name='signup'),
  path('login/', loginfunc, name='login'),
  path('logout/', logoutfunc, name='logout'),
  path('public/', publicfunc, name='public'),
  path('share/', shareview.as_view(), name='share'),
  path('public/category/<str:category>', category, name='category'),
  path('public/sort=<str:sort>', sortfunc, name='sort'),
  path('mypage/<str:user_name>/', mypagefunc, name='mypage'),
  path('mypage/<str:user_name>/category/<str:category>', mypagecategory, name='mypagecategory'),
  path('update/<int:pk>', updateview.as_view(), name='update'),
  path('detail/<int:pk>', detailfunc, name='detail'),
  path('delete/<int:pk>', postdeleteview.as_view(), name='delete'),
  path('good/<int:pk>', goodfunc, name='good'),
  #今回いいねボタンを設置するページ
  #path(r'^(?P[\w-]+)/$', likepage, name="like_page"),
  #いいね情報を格納するページ
  #path(r'^(?P[\w-]+)/like/$', likebutton.as_view(), name='like_api'),
]