from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=25)
    email = models.EmailField(max_length=25, unique=True)


class Book(models.Model):
    BOOK_TYPE_CHOICES = (
        ('ED', 'education'),  # 教育
        ('LT', 'literary'),  # 文艺
        ('HM', 'humanities'),  # 人文社科
        ('LF', 'life'),  # 生活
        ('EC', 'economic'),  # 经管
        ('TC', 'tech'),  # 科技
        ('CH', 'child'),  # 少儿
        ('IN', 'Inspirational'),  # 励志
    )
    BOOK_LAN_CHOICES = (
        ('EN', 'english'),  # 英语
        ('ZH', 'chinese'),  # 汉语
        ('OT', 'other'),  # 其他
    )
    TRADE_TYPE = (
        ('OL', 'online'),  # 线上
        ('FL', 'offline'),  # 线下
    )
    seller = models.ForeignKey('User', to_field='id', on_delete=models.CASCADE)  # 卖方
    title = models.CharField(max_length=20)  # 书名
    author = models.CharField(max_length=15)  # 作者
    language = models.CharField(max_length=2, choices=BOOK_LAN_CHOICES)  # 语言
    originPrice = models.DecimalField(max_digits=6, decimal_places=2)  # 原价
    sellingPrice = models.DecimalField(max_digits=6, decimal_places=2)  # 售价
    type = models.CharField(max_length=2, choices=BOOK_TYPE_CHOICES)  # 种类
    info = models.CharField(max_length=255)  # 描述
    img = models.ImageField()  # 图片
    isbn = models.CharField(max_length=20, blank=True)
    url = models.URLField()
    method = models.CharField(max_length=2, choices=TRADE_TYPE)  # 交易方式
    time = models.DateTimeField(auto_now_add=True)


class EDBook(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=1)


class LTBook(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=1)


class HMBook(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=1)


class LFBook(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=1)


class ECBook(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=1)


class TCBook(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=1)


class CHBook(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=1)


class INBook(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=1)


class OrderForm(models.Model):
    TRADE_TYPE = (
        ('OL', 'online'),  # 线上
        ('FL', 'offline'),  # 线下
    )
    seller = models.ForeignKey('User', to_field='id', on_delete=models.CASCADE)
    buyer = models.IntegerField()
    method = models.CharField(max_length=2, choices=TRADE_TYPE)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    book = models.ForeignKey('Book', to_field='id', on_delete=models.CASCADE)


class Want(models.Model):
    user = models.ForeignKey('User', to_field='id', on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=15, null=True, blank=True)
    disc = models.TextField()
    isbn = models.CharField(max_length=20, null=True, blank=True)
    url = models.URLField()
