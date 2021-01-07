from django.db import models


class Maker(models.Model):
    name = models.CharField('メーカー', max_length=20)

    def __str__(self):
       return self.name


class Product(models.Model):
    maker = models.ForeignKey(Maker, verbose_name='メーカー',  on_delete=models.CASCADE)
    name = models.CharField('機種', max_length=20)
    release_date = models.DateField('発売日')

    def __str__(self):
        return self.name


class SmartPhone(models.Model):
    product = models.ForeignKey(Product, verbose_name='機種', related_name='smartphone',on_delete=models.CASCADE)
    storage = models.IntegerField('データ容量(GB)')
    color = models.TextField('色')

    def __str__(self):
        '''機種名/データ容量/色'''
        return str(self.product) + '/' + str(self.storage) + '(GB)' + '/' + self.color


class Stock(models.Model):
    smartphone = models.ForeignKey(SmartPhone, verbose_name='機種', related_name='stock', on_delete=models.CASCADE)
    version = models.TextField('OSバージョン')
    price = models.IntegerField('販売価格(円)')

    def __str__(self):
        return str(self.smartphone) + '/' + str(version) + '/' +price

