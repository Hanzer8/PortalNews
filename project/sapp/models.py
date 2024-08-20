from django.db import models
from django.contrib.auth.models import User
from .resources import *
from django.db.models import Sum
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class Autor(models.Model):
   autor_user = models.OneToOneField(User, on_delete=models.CASCADE)
   reting_aut = models.SmallIntegerField(default=0)

   def update_rating(self):
      post_rat = self.post_set.aggregate(poost_reting=Sum('reting'))
      pRat = 0
      pRat += post_rat.get('rating_pos')

      commetn_rat = self.autor_user.comment.user.aggrigate(commentre_rating=Sum('rating'))
      cRat = 0
      cRat += commetn_rat.get('reting_com')

      self.reting_aut = pRat * 3 + cRat
      self.save()


class Category(models.Model):
   name_cat = models.CharField(max_length=64, unique=True)

   def __str__(self):
      return self.name_cat


class Post(models.Model):
   post_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
   post_catagory = models.ManyToManyField(Category, through='PostCategory')
   articles_or_news = models.CharField(max_length=2,
                                       choices=S_OR_N,
                                       default='AR')
   datetime = models.DateTimeField(default=timezone.now)
   title = models.CharField(max_length=255)
   text = models.TextField()
   rating_pos = models.IntegerField(choices=GRADE,
                                    default=0,
                                    editable=True),

   added_at = models.DateTimeField(default=timezone.now)

   def __str__(self):
      return self.title

   def get_absolute_url(self):
      return reverse('posts', args=[str(self.id)])


class PostCategory(models.Model):
   postcategory_post = models.ForeignKey(Post, on_delete=models.CASCADE)
   postcategory_category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
   comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
   comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
   text_com = models.TextField()
   datetimecom = models.DateTimeField(auto_now_add=True)
   reting_com = models.IntegerField(default=0)

   def like(self):
      self.reting_com += 1
      self.save()

   def dislike(self):
      self.reting_com -= 1
      self.save()

   def preview(self):
      return f'{self.text_com[0:123]} ...'
