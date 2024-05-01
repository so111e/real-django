from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField() 
    writer = models.CharField(max_length=10)
    def __str__(self):
        return str(self.title)
    
class ListView(models.Model):
    model = Post
    template_name = 'blog/post_list.html' #템플릿
    context_object_name = 'posts' #변수 값의 이름