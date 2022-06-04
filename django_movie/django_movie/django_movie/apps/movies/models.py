from django.db import models
from django.utils.datetime_safe import date


class Category(models.Model):
    """Категория"""
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Movie(models.Model):
    """Фильм"""
    title = models.CharField("Название", max_length=100, default=None, blank=True)
    tagline = models.CharField("Слоган", max_length=100, default='', blank=True)
    description = models.TextField("Описание", default=None, blank=True)
    poster = models.ImageField("Постер", upload_to="movies/", default=None, blank=True)
    year = models.PositiveSmallIntegerField("Год выхода", default=2022, blank=True)
    country = models.CharField("Страна", max_length=50, default=None, blank=True)
    directors = models.ManyToManyField(Actor, verbose_name="режисер", related_name="film_director", default=None, blank=True)
    actors = models.ManyToManyField(Actor, verbose_name="актёры", related_name="film_director", default=None, blank=True)
    genres = models.ManyToManyField(Genre, verbose_name="жанры", related_name="film_director", default=None, blank=True)
    world_premier = models.DateField("Премьера", default=date.today, blank=True)
    budget = models.PositiveIntegerField("Бюджет", default=0, blank=True, help_text="указать сумму в долларах")
    fees_in_usa = models.PositiveIntegerField("Сборы в США", default=0, blank=True, help_text="указать сумму в долларах")
    fees_in_world = models.PositiveIntegerField("Сборы в мире", default=0, blank=True, help_text="указать сумму в долларах")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True, blank=True)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

class Movie_shots(models.Model):
    """Кадры из фильма"""
    title = models.CharField("название изображения", max_length=150)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="movie_shots/", default=None, blank=True)
    id_movie = models.IntegerField("Категория", default=None, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кадры из фильма"
        verbose_name_plural = "Кадры из фильма"

class Director(models.Model):
    """Режисер"""
    name = models.CharField("Режисер", max_length=150)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="directors/", default=None, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Режисер"
        verbose_name_plural = "Режисеры"


class Actor(models.Model):
    """Актёры и режжисёры"""
    name = models.CharField("Имя", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0, blank=True)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="actors/", default=None, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Актёры и режжисёры"
        verbose_name_plural = "Актёры и режжисёры"


class Rating_stars(models.Model):
    """Звёзды рейтинга"""
    value = models.IntegerField("Значение", default=None, blank=True)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Звёзды рейтинга"
        verbose_name_plural = "Звёзды рейтинга"


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField("Рейтинг", max_length=150)
    # id_rating_stars =
    # id_movie =

    def __str__(self):
        return self.ip

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Reviews(models.Model):
    """Отзывы"""
    name = models.CharField("Отзывы", max_length=150)
    email = models.CharField("email", max_length=150)
    text = models.TextField("Текст отзыва")
    parent = models.IntegerField("parent", default=None, blank=True)
    movie = models.IntegerField("на фильм", default=None, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отзывы"
        verbose_name_plural = "Отзывы"


class Genre(models.Model):
    """Жанры"""
    name = models.CharField("Жанр", max_length=100)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"



