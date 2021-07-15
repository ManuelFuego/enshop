from django.db import  models
from django.utils import timezone

class Category(models.Model):
    '''категория'''
    name = models.CharField(max_length=100,verbose_name='Название категории')
    #slug = models.SlugField(max_length=150, unique=True,db_index=True, verbose_name='URL')
    def __str__(self):
        return self.name

class Product(models.Model):
    '''продукт'''
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name= 'Название товара')
    description = models.CharField(max_length=250, verbose_name='Описание')
    quantity = models.PositiveIntegerField( verbose_name='Количество', default=0)
    price = models.DecimalField(max_digits=9,decimal_places= 2,verbose_name='Цена', blank=False)
    link = models.CharField(max_length= 250,verbose_name='Ссылка на товар' ,blank=True)
    final_price = models.DecimalField(max_digits=9,decimal_places= 2,verbose_name='Итого',default=0, blank=False)
    #slug = models.SlugField(max_length=150, unique=True,db_index=True, verbose_name='URL')

    def __str__(self):
        return f'{self.category}, {self.name}, {self.description}, {self.price}, {self.quantity},{self.final_price}'

    def save(self, *args, **kwargs):
        self.final_price = self.quantity * self.price
        super().save(*args, **kwargs)


    def get_absolute_url(self):
        return f'/eshop/{self.id}'

class Client(models.Model):
    ''' клиент'''
    first_name = models.CharField(max_length=100,verbose_name='Имя')
    last_name = models.CharField(max_length=100,verbose_name='фамилия')
    phone = models.CharField(max_length=11 , verbose_name='Контакт')
    address = models.CharField(max_length=255, verbose_name='Адрес', null=True, blank=True)
    orders = models.ManyToManyField('Order', verbose_name='Заказы покупателя', related_name='related_order', blank=True)

    def __str__(self):
        return f"Покупатель: {self.first_name} {self.phone}"

    def get_absolute_url(self):
        return f'eshop/{self.id}'



class ShopCart(models.Model):
    '''корзина товаров'''
    owner = models.ForeignKey(Client, null=True, verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, default=0, decimal_places=2, verbose_name='Общая цена')
    in_order = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

class Order(models.Model):
    ''' заказ '''
    STATUS_NEW = 'new'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_READY = 'is_ready'
    STATUS_COMPLETED = 'completed'

    BUYING_TYPE_SELF = 'self'
    BUYING_TYPE_DELIVERY = 'delivery'

    STATUS_CHOICES = (
        (STATUS_NEW, 'Новый заказ'),
        (STATUS_IN_PROGRESS, 'Заказ в обработке'),
        (STATUS_READY, 'Заказ готов'),
        (STATUS_COMPLETED, 'Заказ выполнен')
    )

    BUYING_TYPE_CHOICES = (
        (BUYING_TYPE_SELF, 'Самовывоз'),
        (BUYING_TYPE_DELIVERY, 'Доставка')
    )

    customer = models.ForeignKey(Client, verbose_name='Покупатель', related_name='related_orders', on_delete=models.CASCADE, blank=True)
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    cart = models.ForeignKey(ShopCart, verbose_name='Корзина', on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=1024, verbose_name='Адрес', null=True, blank=True)
    status = models.CharField(
        max_length=100,
        verbose_name='Статус заказ',
        choices=STATUS_CHOICES,
        default=STATUS_NEW
    )
    buying_type = models.CharField(
        max_length=100,
        verbose_name='Тип заказа',
        choices=BUYING_TYPE_CHOICES,
        default=BUYING_TYPE_SELF
    )
    comment = models.TextField(verbose_name='Комментарий к заказу', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания заказа')
    order_date = models.DateField(verbose_name='Дата получения заказа', default=timezone.now)

    def __str__(self):
        return str(self.id)
