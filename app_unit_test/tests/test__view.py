from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from app_unit_test.models import Blog, Category

# Test cases for views in app_unit_test/views.py


class test__Views(TestCase):
    # setUp method to create test data
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.category = Category.objects.create(title="Django Testing")
        self.blog = Blog.objects.create(
            title="Unit Testing in Django",
            content="This is a test blog content.",
            author=self.user,
            category=self.category,
        )
    # test_index_view

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    # test_blogs_list_view

    def test_blogs_list_view(self):
        response = self.client.get(reverse('blogs_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogs_list.html')
        self.assertIn(self.blog, response.context['blogs'])
    # test_blog_detail_view

    def test_blog_detail_view(self):
        response = self.client.get(reverse('blog_detail', args=[self.blog.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_detail.html')
        self.assertEqual(response.context['blog'], self.blog)
    # test_create_blog_view

    def test_create_blog_view_get(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('create_blog'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_blog.html')
    # test_create_blog_view_post

    def test_create_blog_view_post(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('create_blog'), {
            'title': 'New Blog Post',
            'content': 'Content of the new blog post.',
            'category': self.category.id,
        })
        self.assertEqual(response.status_code, 302)  # Redirect after creation
        new_blog = Blog.objects.get(title='New Blog Post')
        self.assertIsNotNone(new_blog)
        self.assertEqual(new_blog.author, self.user)

    # test_blog_update_view
    def test_blog_update_view_get(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(
            reverse('blog_update', args=[self.blog.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_update.html')
        self.assertEqual(response.context['form'].instance, self.blog)
        
    # test_blog_update_view_post
    def test_blog_update_view_post(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('blog_update', args=[self.blog.slug]), {
            'title': 'Updated Blog Title',
            'content': 'Updated content of the blog post.',
            'category': self.category.id,
        })
        self.assertEqual(response.status_code, 302)  # Redirect after update
        updated_blog = Blog.objects.get(id=self.blog.id)
        self.assertEqual(updated_blog.title, 'Updated Blog Title')
        self.assertEqual(updated_blog.content,
                         'Updated content of the blog post.')
        self.assertEqual(updated_blog.author, self.user)

    # test_blog_delete_view
    def test_blog_delete_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('blog_delete', args=[self.blog.slug]))
        self.assertEqual(response.status_code, 302)  # Redirect after deletion
        with self.assertRaises(Blog.DoesNotExist):
            Blog.objects.get(id=self.blog.id)
