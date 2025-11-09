from django.db import models
from unit_test.models import BaseModel
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor.fields import RichTextField


# Table Languague
class Languague(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug or self.slug != slugify(self.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


# Table Framwork
class Framwork(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug or self.slug != slugify(self.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


# Table tags
class tags(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug or self.slug != slugify(self.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


# Table Documentation
class Documentation(BaseModel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_documentation'
    )
    content = RichTextField(blank=True, null=True)
    language = models.ForeignKey(
        Languague, on_delete=models.CASCADE, related_name='language_documentation'
    )
    framwork = models.ManyToManyField(
        Framwork, related_name='framwork_documentation', blank=True, null=True
    )
    tags = models.ManyToManyField(
        tags, related_name='documentation', blank=True, null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Documentation"
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        # update slug if title changes
        if not self.slug or self.slug != slugify(self.title):
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse("model_detail", kwargs={"pk": self.pk})
