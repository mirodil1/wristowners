from django.contrib import admin
from .models import Brand, BrandModel, Product, FAQ
# Register your models here.
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class BranModeldAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Brand, BrandAdmin)
admin.site.register(BrandModel, BranModeldAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(FAQ)