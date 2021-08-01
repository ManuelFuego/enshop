from decimal import Decimal
from django.test import TestCase
from .models import *
from .views import *
import unittest
#start test enter command ==python manage.py test
from django.contrib.auth import get_user_model

class TestCreateProductPositive(TestCase):

    def setUp(self) -> None:
        '''создание объектов '''
        self.category = Category.objects.create(name="Тестовая категория")
        self.prod = Product.objects.create(
            category =self.category,
            name = "Тестовая одежда",
            description = "Тестовое описание продукта",
            quantity = 10,
            price= Decimal(50),
            link= "https://www.test.test.coms"
        )

        self.client = Client.objects.create(
            first_name='ТестИван',
            last_name = 'ТестИваныч',
            phone = 86582222,
            address ='BakerStreet'
        )

    def test_checkdata(self):
        self.assertIn(self.prod,Product.objects.all())
        self.assertEqual(self.prod.final_price, Decimal(500.00))

class TestCreateProductNegative(TestCase):
    def setUp(self) -> None:
        self.category = Category.objects.create(name="Тестовая категория")
        self.prod = Product.objects.create(
        category=self.category,
        name="Тестовая одежда1",
        description="Тестовое описание продукта1",
        quantity=-10,
        price=Decimal(50),
        link="https://www.test.test.coms"
    )

        self.client = Client.objects.create(
        first_name='ТестИван',
        last_name='ТестИваныч',
        phone='86582222',
        address='BakerStreet'
    )

    def test_checkdata_negative(self):
        self.assertIn(self.prod,Product.objects.all())
        self.assertEqual(self.prod.final_price, Decimal(500.00))