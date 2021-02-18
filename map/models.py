from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class UnverifiedTag(models.Model):


    name = models.CharField('Название', max_length=30)
    description = models.TextField('Описание', max_length=100)
    location = models.CharField('Местоположение', max_length=30)
    x_coord = models.FloatField('Координата X')
    y_coord = models.FloatField('Координата Y')
    username = models.CharField('Имя пользователя', max_length=30)
    email = models.EmailField('Email', max_length=30)



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Метка(*)'
        verbose_name_plural = 'Метки(*)'


class Tag(models.Model):

    name = models.CharField('Название', max_length=30)
    description = models.TextField('Описание', max_length=100)
    location = models.CharField('Местоположение', max_length=30)
    x_coord = models.FloatField('Координата X')
    y_coord = models.FloatField('Координата Y')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Метка'
        verbose_name_plural = 'Метки'


def get_image_filename(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)


class Images(models.Model):
    tag_object = models.ForeignKey(Tag, on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to=get_image_filename, null=True, blank=True)


class UImages(models.Model):
    tag_object = models.ForeignKey(UnverifiedTag, on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to=get_image_filename, null=True, blank=True)