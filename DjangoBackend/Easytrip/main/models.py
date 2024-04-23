from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

class places(models.Model):
    title = models.CharField('Название', max_length=100)
    descrip = models.TextField('Описание', max_length=1200)
    rating = models.IntegerField('Рейтинг', default=0 , validators=[MaxValueValidator(10), MinValueValidator(0)])
    image = models.ImageField(upload_to='images', default='default_image.png')

    def __str__ (self):
        return self.title

    class Meta:
        verbose_name = 'Достопримечательность'
        verbose_name_plural = 'Достопримечательности'