from pyexpat import model
from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class BrandModel(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Brand, related_name='brandmodel', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=150)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Product(models.Model):
    CHOICES = (
        ("m", "Men"),
        ("w", "Women")
    )
    brandmodel = models.ForeignKey(BrandModel, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    series = models.CharField(max_length=64, blank=True, null=True)
    gender = models.CharField(choices=CHOICES, max_length=64)
    movement = models.CharField(max_length=150, blank=True, null=True)
    clasp = models.CharField(max_length=155, blank=True, null=True)
    crystal = models.CharField(max_length=155, blank=True, null=True)
    strap = models.CharField(max_length=155, blank=True, null=True)
    size = models.CharField(max_length=155, blank=True, null=True)
    case = models.CharField(max_length=155, blank=True, null=True)
    bazel = models.CharField(max_length=155, blank=True, null=True)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    image1 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    image2 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    image3 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    image4 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/{self.brandmodel.slug}/{self.slug}"
    
    def get_image(self):
        if self.image:
            return self.image.url
    
    def get_image1(self):
        if self.image1:
            return self.image1.url
    
    def get_image2(self):
        if self.image2:
            return self.image2.url
    
    def get_image3(self):
        if self.image3:
            return self.image3.url

    def get_image4(self):
        if self.image4:
            return self.image4.url
            

class FAQ(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()

