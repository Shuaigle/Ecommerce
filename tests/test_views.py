# This can skip test
from unittest import skip
from django import http
from django.http import request
from store.views import all_products
from django.test import TestCase
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.urls import reverse
from store.models import Category, Product

from django.test import Client

class TestViewResponse(TestCase):
    def setUp(self):
        self.c = Client()
        # create in database
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='django beginners', created_by_id=1, 
                                                slug='django-beginners', price='20.00', image='django')


    def test_url_allowed_hosts(self):
        response = self.c.get('/')
        # 200 means OK
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        response = self.c.get(reverse("store:product_detail", args=['django-beginners']))
        self.assertEqual(response.status_code, 200)

    def test_category_list_url(self):
        response = self.c.get(reverse("store:category_list", args=['django']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        request = HttpRequest()
        response = all_products(request)
        # It returns whole html page (use print() to check)
        html = response.content.decode('utf8')
        self.assertIn('<title> Home </title>\n', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))