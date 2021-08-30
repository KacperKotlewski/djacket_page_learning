from django.db import models
from django.core.files import File

from io import BytesIO
from PIL import Image

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

class Product(models.Model):
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="uploded/", blank=True, null=True)
    thumbnail = models.ImageField(upload_to="uploded/", blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-date_added",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'


    def __get_img_url(self, img):
        if img:
            return f'http://localhost:8000' + img.url
        return ""

    def get_image(self):
        return self.__get_img_url(self.image)

    def get_thumbnail(self):
        thumbnail = self.__get_img_url(self.thumbnail)
        if thumbnail:
            return thumbnail
        else:
            self.thumbnail = self.make_thumbnail(self.image)
            self.save()
            return self.__get_img_url(self.thumbnail)

    def make_thumbnail(self, image, size=(600,400)):
        img = Image.open(image)
        img.convert("RGB")
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, "JPEG", quality=85)

        thumbnail = File(thumb_io, name=image.name)
        return thumbnail
