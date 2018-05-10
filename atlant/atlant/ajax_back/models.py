from django.db import models as m
from django.utils.timezone import now
# Create your models here.


class Info(m.Model):
    name = m.CharField(max_length=100, null=True, blank=True)
    description = m.CharField(max_length=3000, null=True, blank=True)
    image = m.ImageField(blank=True, verbose_name=u'Картинка', upload_to='media')
    datetime_add = m.DateTimeField(default=now, null=True)

