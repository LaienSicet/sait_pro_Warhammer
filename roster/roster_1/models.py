from django.db import models

# Create your models here.

class Ros(models.Model):
    nazv = models.CharField('название', max_length=200)
    form = models.CharField('формат', max_length=200)
    r = models.TextField('ростер')

    def __str__(self):
        return self.nazv

    def get_absolute_url(self):
        return f"/{self.id}"

    class Meta:
        verbose_name = 'Ростер'
        verbose_name_plural = 'Ростера'


