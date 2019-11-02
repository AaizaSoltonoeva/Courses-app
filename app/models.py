from django.db import models

STATUS_CHOICES = (
    (1, 'PHONE'),
    (2, 'FACEBOOK'),
    (3, 'EMAIL'),
)


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    imgpath = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.CharField(max_length=100, verbose_name='Описание')
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE,
                                 verbose_name='Категория', null=True,)
    logo = models.CharField(max_length=100, verbose_name='Логотип')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name


class Contact(models.Model):
    type = models.IntegerField(choices=STATUS_CHOICES, default=1)
    value = models.CharField(max_length=150)
    course = models.ForeignKey(Course, related_name='contacts', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.value


class Branch(models.Model):
    latitude = models.CharField(max_length=100, verbose_name='Широта')
    longitude = models.CharField(max_length=100, verbose_name='Долгота')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    course = models.ForeignKey(Course, related_name='branches', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'

    def __str__(self):
        return self.address




