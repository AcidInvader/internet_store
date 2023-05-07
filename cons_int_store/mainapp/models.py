from django.db import models



# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя', max_length=200, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя продукта', max_length=200)
    brand = models.CharField(verbose_name='брэнд продукта', max_length=200, default='No Name')
    image = models.ImageField(verbose_name='картинка', upload_to='pictures_of_product', blank=True)
    short_desc = models.CharField(verbose_name='краткое описание', max_length=100, blank=True)
    description = models.TextField(verbose_name='описание', blank=True)
    price = models.DecimalField(verbose_name='цена', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)
    color = models.CharField(verbose_name='цвет', max_length=20, blank=True)
    
    

    def __str__(self):
        return f"{self.name} ({self.category.name})"