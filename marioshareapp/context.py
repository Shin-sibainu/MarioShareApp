from .models import CourseCategory, SortModel

#　どのページでもデータがとってこれるように別個で作ってる。
def related(request):
  category_list = CourseCategory.objects.all()
  sort_list = SortModel.objects.all()
  context = {
    'category_list':category_list,
    'sort_list': sort_list
  }
  return context