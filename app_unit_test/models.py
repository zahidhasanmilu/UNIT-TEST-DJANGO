from django.db import models
from django.contrib.auth.models import User
# slugify
from django.urls import reverse
from django.utils.text import slugify
# UUID
import uuid
# Create your models here.


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Blog(BaseModel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=300)
    content = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_blogs')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='category_blogs')

    def save(self, *args, **kwargs):
        try:
            if self.pk:  # যদি update হয়
                old_blog = Blog.objects.get(pk=self.pk)
                if old_blog.title != self.title:
                    self.slug = slugify(self.title)
            else:
                self.slug = slugify(self.title)  # নতুন blog
        except Blog.DoesNotExist:
            # যদি pk পাওয়া না যায়, নতুন blog ধরে নাও
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})
