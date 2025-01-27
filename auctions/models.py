from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class AuctionModel(models.Model):

    STATUS_CHOICES = {
        'pending': 'Очікує на підтвердження',
        'active': 'Активний',
        'expired': 'Час аукціону вийшов',
        'cancelled': 'Аукціон скасовано',
        'payment_pending': 'Очікує на оплату',
        'sold': 'Лот продано',
        'finished': 'Аукціон завершено',
    }

    user = models.ForeignKey(User, on_delete=models.CASCADE, 
                             verbose_name='Користувач, що створив лот')
    title = models.CharField(max_length=200, verbose_name='Назва лоту')
    description = models.TextField(max_length=10000, verbose_name='Опис лоту')
    #two last zeros are for cents
    start_price = models.PositiveBigIntegerField(verbose_name='Стартова ціна лоту') 
    start_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, 
                              choices=STATUS_CHOICES, 
                              default='pending', 
                              verbose_name='Статус лоту')
    
    def __str__(self):
        return self.title