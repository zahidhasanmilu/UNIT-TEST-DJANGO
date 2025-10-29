from django.db import models
from django.contrib.auth.models import User
# slugify
from django.urls import reverse
from django.utils.text import slugify
# UUID
import uuid


#-------------------- Create your models here.---------------------#

# Base Model
class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Department Model
class Department(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

# Employee Model
class Employee(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    Dob = models.DateField()
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True, blank=True, related_name='department_employees')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def age(self):
        from datetime import date
        today = date.today()
        return today.year - self.Dob.year - ((today.month, today.day) < (self.Dob.month, self.Dob.day))

    def get_absolute_url(self):
        return reverse("employee_detail", kwargs={"pk": self.pk})