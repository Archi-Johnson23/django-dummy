
# Create your models here.
from django.db import models

class Books(models.Model):
    name = models.CharField(
        'Название книги',
        max_length=200,
        blank=False,
        null=False
    )

    # book_photo = models.ImageField(
    #     'Фото обложки',
    #     upload_to='/media/'
    # )


    price = models.DecimalField(
        'Цена (BYN)',
        default=0.0,
        max_digits=10,
        decimal_places=2
    )


    author_book = models.CharField(
        'Автор книги',
        max_length=200,
        blank=False,
        null=False
    )

    # FORMAT_CHOIS = (('1', '84×108/16') , ('2','70×90/8') , ('3','70×90/16'),
    #             ('4' , '75×90/16'), ('5', '60×90/16'), ('6','84×108/32'),
    #             ('7', '70×90/32'), ('8', ' 70×108/32'), ('9','60×90/32'))

    formattt = models.CharField(
        'Формат',
        max_length=200,
        default = 1,
        # choises =FORMAT_CHOIS,
        blank=False,
        null=False
    )


    isbn = models.CharField(
        'ISBN',
        max_length=200,
        default = '',
        blank=False,
        null=False
    )


    genres = models.CharField(
        'Жанры',
        default='Фантастика',
        max_length=200,
        blank=False,
        null=False
    )


    # dat_publich = models.DateField(
    #     'Год издания',
    #     blank=False,
    #     null=False
    # )

    # weight = models.DecimalField(
    #     'Вес(гр)',
    #     default='100гр',
    #     max_length=200,
    #     blank=False,
    #     null=False
    # )
    # pages = models.DecimalField(
    #     'Страниц',
    #     max_length=200,
    #     blank=False,
    #     null=False
    # )

    # age_ogranich = models.DecimalField(
    #     'Возрастные ограничения',
    #     default='+18',
    #     max_length=200,
    #     blank=False,
    #     null=False
    # )

    # col_books = models.DecimalField(
    #     'Количество книг в наличии',
    #     max_length=200,
    #     blank=False,
    #     null=False
    # )



    # publisher = models.CharField(
    #     'Издательство ',
    #     default='',
    #     max_length=200,
    #     blank=False,
    #     null=False
    # )


    # data_catalog = models.DateField(
    #     'Дата внесения в каталог',
    #     blank=False,
    #     null=False
    # )

    # data_carta = models.DateField(
    #     'Дата последнего изменения карточки',
    #     blank=False,
    #     null=False
    # )

    def __str__(self):
        return self.choice_text


