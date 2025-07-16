from django.db import models
from django.utils.text import slugify

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение', blank=True, null=True)
    slug = models.SlugField(max_length=50, unique=True, verbose_name='URL', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
            base_slug = self.slug
            counter = 1
            while Bb.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-published']