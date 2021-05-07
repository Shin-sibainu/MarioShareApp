from django.db import models
from django.utils.timezone import now
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User
# MarioShareで扱うデータを登録しよう。
class MarioShareModel(models.Model):
    coursetitle = models.CharField(max_length=100)  
    coursemaker = models.CharField(null=True, max_length=20) 
    courseid = models.CharField(max_length=11)
    # upload_toを空にしておくと、MEDIA_ROOTの中に画像が勝手に格納されるみたい。
    courseimage = models.ImageField(upload_to='', null=True, blank=True)
    coursevideo = EmbedVideoField(null=True)
    comment = models.TextField() 
    post_date = models.DateTimeField(default=now)
    good = models.IntegerField(null=True, blank=True, default=0)
    favorite = models.IntegerField(null=True, blank=True, default=0)
    contributer = models.CharField(max_length=50, null=True)

    def __str__(self):
      return self.coursetitle