from django.db import models
from django.urls.base import reverse
from django.utils.timezone import now
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User
from django.conf import settings
# MarioShareで扱うデータを登録しよう。

class SortModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
      return self.name

class CourseCategory(models.Model):
    # CHOICE = [('danger', 'high'),('warning', 'normal')]
    name = models.CharField(
      max_length=50, 
      )

    def __str__(self):
      return self.name

class MarioShareModel(models.Model):
    coursetitle = models.CharField(max_length=100)  
    coursemaker = models.CharField(null=True, max_length=20) 
    courseid = models.CharField(max_length=11)
    # upload_toを空にしておくと、MEDIA_ROOTの中に画像が勝手に格納されるみたい。
    courseimage = models.ImageField(upload_to='', null=True, blank=True)
    coursevideo = EmbedVideoField(null=True)
    coursecategory = models.ForeignKey(CourseCategory, on_delete=models.PROTECT)
    comment = models.TextField() 
    post_date = models.DateTimeField(default=now)
    good = models.IntegerField(null=True, blank=True, default=0)
    #like_set = models.IntegerField(null=True, blank=True, default=0)
    favorite = models.IntegerField(null=True, blank=True, default=0)
    contributer = models.CharField(max_length=50, null=True)
    #like = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="likes")
    #slug = models.SlugField()

    #def get_absolute_url(self):
      #return reverse('like_page', kwargs={'slug', self.slug})

    #def get_api_like_url(self):
      #return reverse("like_api", kwargs={'slug':self.slug}) 

    def __str__(self):
      return self.coursetitle