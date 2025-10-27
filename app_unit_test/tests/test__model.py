#test
from django.test import TestCase
from app_unit_test.models import Category, Blog
from django.contrib.auth.models import User


class test__CategoryModel(TestCase):
    def setUp(self):
        self.category = Category.objects.create(title="Django Testing")
        
    def test_category_creation(self):
        self.assertEqual(self.category.title, "Django Testing")
        self.assertEqual(self.category.slug, "django-testing")
        self.assertIsNotNone(self.category.created_at)
        self.assertIsNotNone(self.category.updated_at)
        
class test__BlogModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.category = Category.objects.create(title="Django Testing")
        
        self.blog = Blog.objects.create(
            title="Unit Testing in Django",
            content="This is a test blog content.",
            author=self.user,
            category = self.category,
        )
        
    def test_blog_creation(self):
        self.assertEqual(self.blog.title, "Unit Testing in Django")
        self.assertEqual(self.blog.slug, "unit-testing-in-django")
        self.assertEqual(self.blog.content, "This is a test blog content.")
        self.assertEqual(self.blog.author.username, "testuser")
        self.assertEqual(self.blog.category.title, "Django Testing")
        self.assertIsNotNone(self.blog.created_at)
        self.assertIsNotNone(self.blog.updated_at)
        
    def test_blog_str_method(self):
        self.assertEqual(str(self.blog), "Unit Testing in Django")