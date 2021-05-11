from django.contrib import admin
from .models import MarioShareModel, CourseCategory, SortModel

# Register your models here.
admin.site.register(MarioShareModel)
admin.site.register(CourseCategory)
admin.site.register(SortModel)