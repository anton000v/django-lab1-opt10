from django.db import models

class File(models.Model):
    description = models.CharField(max_length = 150, verbose_name='Описание')
    file_field = models.FileField(max_length = 100, verbose_name='Файл')
    counter = models.PositiveSmallIntegerField(default = 0, verbose_name='Счетчик скачиваний')

    def __str__(self):
        return self.description

    def incr_counter(self):
        self.counter += 1    
    
    
