from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    thumb = models.ImageField(default='default.png', null=True)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'store_products'


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'store_categories'


class Brand(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "store_brands"


class CartProduct(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.title

    def total_price(self):
        return self.product.price * self.quantity


class Slide(models.Model):
    slide = models.ImageField()


DISTRICTS = (
    ("Город Бухара", "Город Бухара"),
    ("Ромитанский район", "Ромитанский район"),
    ("Гиждуванский район", "Гиждуванский район"),
    ("Жондорский район", "Жондорский район"),
    ("Каганский район", "Каганский район"),
    ("Шафирканский район", "Шафирканский район"),
    ("Вабкентский район", "Вабкентский район"),
    ("Алатский район", "Алатский район"),
)


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, choices=DISTRICTS)
    phone = models.IntegerField()
    total_price = models.IntegerField()

    def __str__(self):
        return f"Order #{self.pk}"


class OrderProduct(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='order_products')
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    amount = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return f"{self.product} x{self.amount} - {self.order.customer.username}"


RATE_CHOICES = [
    (1, '⭐️'),
    (2, '⭐️ ⭐️'),
    (3, '⭐️ ⭐️ ⭐️'),
    (4, '⭐️ ⭐️ ⭐️ ⭐️'),
    (5, '⭐️ ⭐️ ⭐️ ⭐️ ⭐️'),
]


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=True, null=True)
    rating = models.PositiveSmallIntegerField(choices=RATE_CHOICES, null=True)

    def str(self):
        return self.user.username
