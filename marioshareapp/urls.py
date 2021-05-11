from django.contrib import admin
from django.urls import path, include
from .views import signupfunc, loginfunc, logoutfunc, publicfunc, landingfunc, mypagefunc, shareview, postdeleteview, detailfunc, goodfunc, updateview, category, sortfunc

urlpatterns = [
  # 指定したviewにrequestオブジェクト渡している。
  path('landing/', landingfunc, name='landing'),
  path('signup/', signupfunc, name='signup'),
  path('login/', loginfunc, name='login'),
  path('logout/', logoutfunc, name='logout'),
  path('public/', publicfunc, name='public'),
  path('share/', shareview.as_view(), name='share'),
  #path('share/', share_category, name='share'),
  path('public/category/<str:category>', category, name='category'),
  path('public/sort=<str:sort>', sortfunc, name='sort'),
  path('mypage/<int:user_id>/', mypagefunc, name='mypage'),
  # path('mypage/<int:user_id>/category/<str:category>', mypagecategory, name='mypagecategory'),
  path('update/<int:pk>', updateview.as_view(), name='update'),
  path('detail/<int:pk>', detailfunc, name='detail'),
  path('delete/<int:pk>', postdeleteview.as_view(), name='delete'),
  path('good/<int:pk>', goodfunc, name='good'),
]