from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('marioshareapp.urls'))
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 

#開発環境ではDebug＝＝Trueだよね。そんときはMediaを読み込む。
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#本番環境ではFalse。そんときはSTATICを読み込む。
if settings.DEBUG == False:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
