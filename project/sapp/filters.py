from django_filters import FilterSet, DateTimeFilter
from .models import Post, Category, PostCategory
from django.forms import DateTimeInput


class PostFilter(FilterSet):
   added_after = DateTimeFilter(
      field_name='added_at',
      lookup_expr='gt',
      widget=DateTimeInput(
         format='%Y-%m-%dT%H:%M',
         attrs={'type': 'datetime-local'},
      ),
   )
   class Meta:
      model = Post
      fields = {
         'title': ['exact'],
         'post_catagory': ['exact'],
      }
